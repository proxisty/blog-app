# Мы используем еще не созданное представление с именем RegistrationView, которое, как
# мы уже знаем, основано на классе, так как оно написано заглавными буквами и имеет
# суффикс as_view (). Его путь просто signup/ поэтому общим путем будет accounts/
# signup/.Сейчас представление, которое использует встроенную UserCreationForm и
# универсальный CreateView.

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
