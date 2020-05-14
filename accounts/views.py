from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms


def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('accounts:profile')
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            if username.lower() in password.lower():
                messages.error(
                    request,
                    "Password is too similar to the username."
                )
            else:
                user = authenticate(
                    username=username,
                    password=password
                )
                login(request, user)
                messages.success(
                    request,
                    "You're now a user! You've been signed in, too."
                )
                return HttpResponseRedirect(reverse('accounts:profile'))
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile(request):
    profile = request.user.profile
    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def edit_profile(request):
    profile = request.user.profile
    form = forms.ProfileForm(
        instance=profile,
        initial={
            'confirm_email': profile.email
        }
    )

    if request.method == 'POST':
        form = forms.ProfileForm(
            instance=profile, data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Updated the Profile Successfully!')
            return HttpResponseRedirect(reverse('accounts:profile'))
    return render(request, 'accounts/edit_profile.html', {'form': form, 'profile': profile})


@login_required
def change_password(request):
    form = PasswordChangeForm(request.user)
    profile = request.user.profile

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            new_password = form.cleaned_data['new_password1']
            if profile.user.username.lower() in new_password.lower():
                messages.error(
                    request,
                    "Password is too similar to the username."
                )
            elif profile.first_name.lower() in new_password.lower():
                messages.error(
                    request,
                    "Password is too similar to the first name."
                )
            elif profile.last_name.lower() in new_password.lower():
                messages.error(
                    request,
                    "Password is too similar to the last name."
                )
            else:
                user = form.save()
                update_session_auth_hash(request, user)

                messages.success(
                    request, 'Your password was successfully updated!')
                return HttpResponseRedirect(reverse('accounts:change_password'))
        else:
            messages.error(
                request,
                "Password is incorrect."
            )
    return render(request, 'accounts/change_password.html', {'form': form})
