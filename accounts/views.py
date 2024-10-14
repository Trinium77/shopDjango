from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Inscription réussie ! Bienvenue.")
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Connexion réussie !")
                return redirect('home')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = CustomUserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = '/accounts/password_change/done/'

def logout_user(request):
    logout(request)
    return redirect('home')

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        users = CustomUser.objects.filter(email=email)  # Utilisation de filter ici

        if users.exists():
            for user in users:
                # RÉINITIALISATION DU MOT DE PASSE
                current_site = get_current_site(request)
                mail_subject = "Réinitialiser votre mot de passe."
                message = render_to_string('accounts/reset_password_email.html', {
                    'user': user,
                    'domain': current_site,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                send_email = EmailMessage(mail_subject, message, to=[email])
                send_email.send()

            messages.success(request, "Nous vous avons envoyé un mail pour réinitialiser votre mot de passe.")
        else:
            messages.error(request, "Aucun utilisateur trouvé avec cet e-mail.")
        
        return redirect('login')

    return render(request, 'accounts/forgotPassword.html')
