from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from beanlibapi.apps.core import views, views_temp

app_name = 'core'

urlpatterns = []

urlpatterns += [
    path('bean/', views.BeanListCreateView.as_view()),
    path('bean/<str:pk>/', views.BeanRetrieveUpdateDestroyView.as_view()),
    path('bean/upload/', views.BeanImageUploadView.as_view()),
    path('attachments/uploads/', views.AttachmentUploadView.as_view()),

]

# temp
urlpatterns += [
    path('books/', views_temp.protected_view, name='books_temp'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
