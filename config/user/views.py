
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.urls import reverse_lazy
from django.views.generic import FormView, View
from django.shortcuts import render
from user.forms import UserRegisterationForm
from user.tasks import send_activation_link, greet_user_email
from user.models import UserProfile
# Create your views here.

User = get_user_model()


class RegisterView(FormView):
    template_name = 'user/register.html'
    form_class = UserRegisterationForm
    success_url = reverse_lazy('books:home')

    def form_valid(self, form):
        user = form.save(commit = False)
        user.set_password(form.cleaned_data['password'])
        user.is_active = False
        user.save()
        user_object = User.objects.filter(id=user.id).first()
        UserProfile(user=user_object, role=0).save()

        send_activation_link.delay(user.id)
        return super().form_valid(form)
    

class ActiveUserView(View):
    def get(self, request, token):
        try:
            user_id = cache.get(token)
            user = User.objects.filter(id=user_id).first()
            if user and not user.is_active:
                user.is_active = True
                user.save()
                greet_user_email.delay(user_id)
                msg = {"status": "success", "text": "Your account has been activated successfully 🎉"}
            elif user and user.is_active:
                msg = {"status": "info", "text": "Your account is already activated ✅"}
            else:
                msg = {"status": "danger", "text": "Activation link expired or invalid"}
        except:
            msg = {"status": "danger", "text": "Something went wrong!"}

        return render(request, "user/active.html", {"msg": msg})