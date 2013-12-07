from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'website/home.htm')


def proposal(request):
    return render(request, 'website/proposal.htm')


def registration(request):
    return registration_open(request)


def registration_open(request):
    return render(request, 'website/registration_open.htm')


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
