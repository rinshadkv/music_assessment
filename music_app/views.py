from django.contrib import messages
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Music, AllowedEmail,User
from .forms import UserRegistrationForm, UserLoginForm
from .custom_auth_backend import EmailBackend


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            email_backend = EmailBackend()
            user = email_backend.authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Invalid email or password.'
                messages.error(request, error_message)
    else:
        form = UserLoginForm()
        
    return render(request, 'login.html', {'form': form})


def home(request):
    public_music_files = Music.objects.filter(access_type='public')
    context = {
        'public_music_files': public_music_files
    }
    return render(request, 'home.html', context)


def my_playlist(request):
    my_playlist = Music.objects.filter(user_id=request.user.id)
    context = {
        'my_playlist': my_playlist
    }
    return render(request, 'myPlayList.html', context)


def shared_with_me(request):
    user = request.user
    shared_with_email = Music.objects.filter(access_type='protected', allowed_emails__email=user.email)
    
    context = {
        'shared_with_email': shared_with_email
    }
    return render(request, 'sharedWithMe.html', context)


def upload_music(request):
    if request.method == 'POST':
        music_file = request.FILES.get('musicFile')  
        access_type = request.POST.get('accessType')
        music = Music(user_id=request.user.id, music_file=music_file, access_type=access_type)
        music.save()
        
        if access_type == 'protected':
            emails = request.POST.get('emails')
            email_list = [email.strip() for email in emails.split(',') if email.strip()]
            
            for email in email_list:
                email_exists = check_email(email)
                if not email_exists:
                    messages.error(request, f"Invalid email: {email}")
                    music.delete()
                    return redirect('home')
            allowed_email = AllowedEmail(music_id=music.id, email=email)
            allowed_email.save()
        
        return redirect('home')
    
    return HttpResponse("Invalid request method.")


def custom_logout(request):
    logout(request)
    return redirect('login')

def check_email(email):
    return User.objects.filter(email=email).exists()

def delete_music(request):
    if request.method == 'POST':
        music_id = request.POST.get('musicId')
        try:
            music = Music.objects.get(id=music_id)
            if music.user_id != request.user.id:
                
                messages.error(request, "You are not authorized to delete this music file.")
            else:
                music.delete()
                return redirect('home')
        except Music.DoesNotExist:
            messages.error(request, "Music file not found.")
    else:
        messages.error(request, "Invalid request method.")
    return redirect('home')