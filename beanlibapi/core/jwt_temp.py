import jwt
import time

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpRequest

from jwt.exceptions import ExpiredSignatureError, DecodeError, InvalidTokenError


def generate_jwt_token_payload(user) -> dict:
    current_time = time.time()
    expiration_timestamp = current_time + settings.JWT_ACCESS_TOKEN_LIFETIME

    return {
        "id": int(user.id),
        "expire": int(expiration_timestamp)
    }


def generated_jwt_token(payload) -> str:
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


def authenticate_jwt(request: HttpRequest):
    auth_header = request.META.get('HTTP_AUTHORIZATION', None)

    if auth_header is None:
        return None

    try:
        token = auth_header.split()[-1]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_model = get_user_model()
        user = user_model.objects.get(id=payload['id'])
        return user
    except (ExpiredSignatureError, DecodeError, InvalidTokenError):
        return None



# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             return Response({
#                 'token': token.key,
#                 'user_id': user.pk,
#                 'username': user.username
#             })
#         else:
#             return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
#
#
# def logout_view(request):
#     logout(request)
#     messages.success(request, 'You have been logged out.')
#     return redirect('home')
#
#
# class SignUpFormView(FormView):
#     template_name = 'signup_form.html'
#     form_class = SignupForm
#     success_url = '/'
#
#     def form_valid(self, form):
#         # 폼이 유효할 때 실행되는 메서드
#         print(form.cleaned_data)
#         username = form.cleaned_data['username']
#         password1 = form.cleaned_data['password1']
#         password2 = form.cleaned_data['password2']
#         email = form.cleaned_data['email']
#         # 추가적인 로그인 로직을 처리
#         return super().form_valid(form)
#
#
# def signin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         # 사용자 인증
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             # 인증 성공 시 로그인 처리
#             login(request, user)
#             messages.success(request, 'Login successful!')
#             # return redirect('home')  # 로그인 후 리다이렉트할 페이지 설정
#             return redirect('/')  # 로그인 후 리다이렉트할 페이지 설정
#         else:
#             # 인증 실패 시 메시지 추가
#             messages.error(request, 'Invalid username or password')
#
#     return render(request, 'signin.html')
#
#
# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user_model = get_user_model()
#             user = user_model.objects.create_user(
#                 username=request.POST['username'],
#                 password=request.POST['password1'],
#                 email=request.POST['email'], )
#             auth.login(request, user)
#             return redirect('/')
#         return render(request, 'signup.html')
#     return render(request, 'signup.html', {'key': 'value'})
#
#
# class UserRegisterAPIView(APIView):
#     def post(self, request: Request):
#         serializer = UserRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             token: Token = TokenObtainPairSerializer.get_token(user)
#             access_token = str(token.access_token)
#             refresh_token = str(token)
#             response = Response(
#                 {
#                     "user": serializer.data,
#                     "message": "register successs",
#                     "token": {
#                         "access": access_token,
#                         "refresh": refresh_token,
#                     },
#                 },
#                 status=status.HTTP_200_OK,
#             )
#             response.set_cookie("access", access_token, httponly=True)
#             response.set_cookie("refresh", refresh_token, httponly=True)
#             return response
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)