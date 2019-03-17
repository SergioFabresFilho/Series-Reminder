from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from series_reminder.funcs import generic_message

from core.forms import UserForm


def register(request):

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            return HttpResponseRedirect(reverse('series:list_series'))

        else:
            print(user_form.errors)
            return generic_message(request, 'Invalid form')

    else:
        user_form = UserForm()

        return render(request, 'core/register.html', context={
            'user_form': user_form,
        })


def user_login(request):

    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('series:list_series'))

            else:
                return generic_message(request, 'Invalid login.')

        else:
            return render(request, 'core/user_login.html', context={})

    else:
        return generic_message(request, 'You already are logged in.')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:user_login'))
