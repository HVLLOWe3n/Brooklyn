from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from django.views.generic import TemplateView, RedirectView, CreateView
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site

from account.forms import UserForms
from account.tokens import account_activation_token


class SignUpView(CreateView):
    template_name = 'account/signin.html'
    form_class = UserForms
    success_url = 'confirm/'

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        email, username, password = form.cleaned_data.get('email'), form.cleaned_data.get('username'), form.cleaned_data.get('password')
        self.request.user.is_active = False
        # self.request.user.save()

        current_site = get_current_site(self.request)
        mail_subject = 'Activate you Brooklyn Profile.'
        message = render_to_string('account/confirm_email.html', {
            'user': self.request.user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(self.request.user.pk)),
            'token': account_activation_token.make_token(self.request.user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        ).send()


class ConfirmLinkView(LoginRequiredMixin, CreateView):
    pass
