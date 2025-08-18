from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import FormView

from user.forms import UserRegisterationForm


# Create your views here.

class RegisterView(FormView):
    template_name = 'user/register.html'
    form_class = UserRegisterationForm
    success_url = reverse_lazy('books:home')

    def form_valid(self, form):
        # user = form.save(commit = False)
        # user.set_password(form.cleaned_data['password'])
        # user.is_active = False
        # user.save()
        send_mail("Welcome", "Welcome to BookStore", "amirmallaei@gmail.com", ['amirmallaei@gmail.com'])
        return super().form_valid(form)