from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    """A signup page signup.html is created using a usercreation form
    and redirects to the login page when done
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"
