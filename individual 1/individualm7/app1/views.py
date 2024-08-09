from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from app1.forms import LoginForm

# Create your views here.



def principal(request):
    return render(request,'principal/index.html')

def Home(request):
    return render(request,'principal/home.html')

class loginview(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, { "form": form })
    
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
            form.add_error('username', 'Credenciales incorrectas')
            return render(request, self.template_name, { "form": form })
        else:
            return render(request, self.template_name, { "form": form })
