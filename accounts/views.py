from .forms import *
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView as DefaultLoginView

# Create your views here.
class RegistrationView(CreateView,):
    model = CUser
    form_class = AccountCreationForm
    success_url = '/accounts/login'
    template_name = 'registration/register.html'

    def form_valid(self, form):
        # inactive_user = send_verification_email(self.request, form)
        # send verification mail
        return super().form_valid(form)
    
    # def test_func(self):
    #     print(self.request.is_authenticated())
    #     return True

class LoginView(DefaultLoginView):
    form_class = LoginForm


