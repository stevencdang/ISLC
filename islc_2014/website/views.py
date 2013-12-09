from django.shortcuts import render, render_to_response
from website.forms import RegistrationForm
from django.core.context_processors import csrf


# Create your views here.
def home(request):
    return render(request, 'website/home.htm')


def proposal(request):
    return render(request, 'website/proposal.htm')


def registration(request):
    return registration_open(request)


def registration_open(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_registration = form.save()
            return render(request, 'website/registration_confirm.htm',
                          {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'website/registration_open.htm',
                  {'form': form})


def registration_closed(request):
    return render(request, 'website/registration.htm')


def schedule(request):
    return render(request, 'website/schedule.htm')


def participants(request):
    return render(request, 'website/participants.htm')


def travel(request):
    return render(request, 'website/travel.htm')


def slc_info(request):
    return render(request, 'website/slc_information.htm')


def planning(request):
    return render(request, 'website/planning_committee.htm')


def alumni_panel(request):
    return render(request, 'website/alumni.htm')
