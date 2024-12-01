from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from beanlibapi.apps.core import views

app_name = 'core'

urlpatterns = []

urlpatterns += [
    path('bean/', views.BeanListCreateView.as_view()),
    path('bean/<str:pk>/', views.BeanRetrieveUpdateDestroyView.as_view()),
    # path('bean/upload/', views.BeanImageUploadView.as_view()),
    # path('attachments/uploads/', views.AttachmentUploadView.as_view()),
    # path('attachments/uploads/confirm/', views.AttachmentUploadConfirmView.as_view()),
    path('cafe/', views.CafeView.as_view()),
    path('cafe/<str:uid>/attach/', views.CafeDetailView.as_view())
    # path('/cafe/<str:pk>/', )
]


urlpatterns = format_suffix_patterns(urlpatterns)
