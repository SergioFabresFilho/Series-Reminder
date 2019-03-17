from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from series.forms import SeriesForm
from series.models import Series

from series_reminder.funcs import generic_message


@login_required
def create_series(request):

    if request.method == 'POST':
        series_form = SeriesForm(data=request.POST)

        if series_form.is_valid():
            series = series_form.save(commit=False)
            series.user = request.user
            series.save()

            return HttpResponseRedirect(reverse('series:list_series'))

        else:
            return generic_message(request, 'Invalid form')

    else:
        series_form = SeriesForm()
        return render(request, 'series/create_series.html', context={
            'series_form': series_form,
        })


@login_required
def list_series(request):

    user = request.user
    series_list = Series.objects.get_by_user(user).order_by('name')

    return render(request, 'series/list_series.html', context={
        'series_list': series_list,
    })


@login_required
def delete_series(request, series_id):

    series = Series.objects.get_by_id(series_id)

    if series.user == request.user:
        series.delete()
        return HttpResponseRedirect(reverse('series:list_series'))

    else:
        return generic_message(request, 'You are not allowed to do this.')


@login_required
def update_series(request, series_id):

    series = Series.objects.get_by_id(series_id)

    if series.user == request.user:
        if request.method == 'POST':
            series.episode = request.POST.get('episode_input')
            series.season = request.POST.get('season_input')
            series.save()

            return HttpResponseRedirect(reverse('series:list_series'))

        else:
            return generic_message(request, 'Error. Expected POST method.')

    else:
        return generic_message(request, 'You are not allowed to do this.')
