from django.conf import settings
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from dj_rest_auth.app_settings import api_settings
from dj_rest_auth.forms import AllAuthPasswordResetForm as _AllAuthPasswordResetForm

if 'allauth' in settings.INSTALLED_APPS:
    from allauth.account import app_settings as allauth_account_settings
    from allauth.account.adapter import get_adapter
    from allauth.account.forms import default_token_generator
    from allauth.account.utils import (
        user_pk_to_url_str,
        user_username,
    )
    from allauth.utils import build_absolute_uri


def default_url_generator(request, user, temp_key):
    path = reverse(
        'authx:password_reset_confirm',
        args=[user_pk_to_url_str(user), temp_key],
    )

    if api_settings.PASSWORD_RESET_USE_SITES_DOMAIN:
        url = build_absolute_uri(None, path)
    else:
        url = build_absolute_uri(request, path)

    url = url.replace('%3F', '?')

    return url


class AllAuthPasswordResetForm(_AllAuthPasswordResetForm):
    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data['email']
        token_generator = kwargs.get('token_generator', default_token_generator)

        for user in self.users:

            temp_key = token_generator.make_token(user)

            # save it to the password reset model
            # password_reset = PasswordReset(user=user, temp_key=temp_key)
            # password_reset.save()

            # send the password reset email
            url_generator = kwargs.get('url_generator', default_url_generator)
            url = url_generator(request, user, temp_key)
            uid = user_pk_to_url_str(user)

            context = {
                'current_site': current_site,
                'user': user,
                'password_reset_url': url,
                'request': request,
                'token': temp_key,
                'uid': uid,
            }
            if (
                    allauth_account_settings.AUTHENTICATION_METHOD != allauth_account_settings.AuthenticationMethod.EMAIL
            ):
                context['username'] = user_username(user)
            get_adapter(request).send_mail(
                'account/email/password_reset_key', email, context
            )
        return self.cleaned_data['email']


class PasswordResetForm(_AllAuthPasswordResetForm):
    def get_users(self, email):
        UserModel = get_user_model()

        if not validate_email(email, verify=False, check_mx=False):
            raise exc.InvalidEmailFormat({'email': [_('Not a valid email address')]})

        active_users = UserModel._default_manager.filter(**{
            '%s__iexact' % UserModel.get_email_field_name(): email,
            'is_active': True,
        })
        users = (u for u in active_users)

        if not users:
            raise exc.UserNotFound({'email': [_('User who has the email address is not found')]})
        if settings.CHECK_EMAIL_MX and not validate_email(email, check_mx=True, smtp_timeout=5):
            raise exc.MxServerNotFound({'email': [_('Mail server does not respond')]})

        return users


def save(self, domain_override=None,
         subject_template_name='registration/password_reset_subject.txt',
         email_template_name='registration/password_reset_email.html',
         use_https=False, token_generator=default_token_generator,
         from_email=None, request=None, html_email_template_name=None,
         extra_email_context=None):
    email = self.cleaned_data["email"]
    for user in self.get_users(email):
        context = {
            'email': email,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'user': user,
            'token': token_generator.make_token(user),
            'protocol': 'https' if use_https else 'http',
            'app_domain': settings.APP_DOMAIN,
        }
        super().send_mail(
            subject_template_name, email_template_name, context, from_email,
            email, html_email_template_name=html_email_template_name,
        )
