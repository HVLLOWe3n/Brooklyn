from django.urls import path, re_path

from account.views import SignUpView, activate_link

urlpatterns = [
    path('login/', SignUpView.as_view(), name='signup'),
    path('activate/<str:uidb64>/<str:token>/', activate_link, name='activate')
]
