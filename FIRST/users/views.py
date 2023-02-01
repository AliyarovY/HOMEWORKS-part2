from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.conf import settings
from .services import *

from .models import *
from .forms import *


class Login(LoginView):
    redirect_authenticated_user = True
    form_class = LoginForm
    template_name = 'user/login.html'


    def get_success_url(self):
        return reverse_lazy('home:main')


class Registration(CreateView):
    form_class = RegistrationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('user:verify')


class VerifyPage(CreateView):
    model = VerificationModel
    template_name = 'user/verify.html'
    fields = '__all__'


    def get(self, request, *args, **kwargs):
        user = User.objects.order_by('id').last()
        email, id = user.email, user.id
        code = randint(1000, 9999)
        send(email, code)
        settings.CODE = str(code)
        return super(VerifyPage, self).get(request, *args, **kwargs)


    def form_valid(self, form):
        user_code = self.request.POST.get('code')
        user = User.objects.order_by('id').last()

        if user_code != settings.CODE:
            user.delete()
        else:
            login(self.request, user)

        VerificationModel.objects.all().delete()
        return redirect('home:main')


def logout_user(request):
    logout(request)
    return redirect('home:main')



class Recovery(PasswordChangeView):
    template_name = 'user/recovery.html'

    def get_success_url(self):
        return redirect('home:main')


# def recovery(request):
#     if request.method == 'POST':
#         form = PassRecForm(request.POST)
#         if form.is_valid():
#             email, password = form.cleaned_data.items()
#
#     else:
#         form = PassRecForm()
#
#     return render(request, 'user/recovery.html', {'form': form})
