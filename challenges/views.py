from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january": "In january read a book",
    "february": "Run a marathon",
    "march": "Learn french",
    "april": "Learn russian",
    "may": "Go to the Tibet",
    "june": "Meet some friends",
    "july": "Stay in bed the entire month",
    "august": "Don't sleep any day until you dye",
    "september": "Live in a coffin",
    "october": "Wake up as a zombie",
    "november": "Kill all your friends",
    "december": "Celebrate with blood and raw meat"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]

    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request,'challenges/challenge.html', {
            "text": challenge_text,
            "month": month
        })
    except:
        raise Http404()


def index(request):
    months=list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {"months": months})
