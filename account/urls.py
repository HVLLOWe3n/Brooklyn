from django.urls import path, re_path

from account.views import SignUpView, ConfirmLinkView

urlpatterns = [
    path('login/', SignUpView.as_view(), name='login'),
    path('confirm/', ConfirmLinkView.as_view(), name='confirm')

]
