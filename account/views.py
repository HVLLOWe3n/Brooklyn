from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView, RedirectView, CreateView
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

from account.forms import UserForms
from account.tokens import account_activation_token
from account.models import User


class SignUpView(CreateView):
    template_name = 'account/signin.html'
    form_class = UserForms
    success_url = '/'

    def post(self, request, *args, **kwargs):
        email = self.request.POST.get('email')
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        self.request.user.is_active = False
        # self.request.user.save()

        current_site = get_current_site(self.request)
        mail_subject = 'Activate you ©Brooklyn Profile.'
        message = render_to_string('account/acc_active_email.html', {
            'user': self.request.user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(self.request.user.pk)),
            'token': account_activation_token.make_token(self.request.user),
        })
        sended_email = EmailMessage(
            mail_subject, message, to=[email]
        ).send()

        return HttpResponse('Cool')

    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     valid = super(SignUpView, self).form_valid(form)
    #     email, username, password = form.cleaned_data.get('email'), \
    #                                 form.cleaned_data.get('username'), \
    #                                 form.cleaned_data.get('password')
    #     self.request.user.is_active = False
    #     # self.request.user.save()
    #
    #     current_site = get_current_site(self.request)
    #     mail_subject = 'Activate you Brooklyn Profile.'
    #     message = render_to_string('account/confirm_email.html', {
    #         'user': self.request.user,
    #         'domain': current_site.domain,
    #         'uid': urlsafe_base64_encode(force_bytes(self.request.user.pk)),
    #         'token': account_activation_token.make_token(self.request.user),
    #     })
    #     sended_email = EmailMessage(
    #         mail_subject, message, to=[email]
    #     ).send()
    #
    # def form_invalid(self, form):
    #     print('Yes, form invalid')
    #     return HttpResponse('Invalid')


def activate_link(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

        print(uid)
        print(user)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    return HttpResponse('Activation link is invalid!')


class ConfirmYouActivateView(CreateView):
    template_name = 'account/confirm_email.html'
