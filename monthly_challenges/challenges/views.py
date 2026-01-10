from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

challenges_monthly = {
    "january": "January Eat",
    "february": "February Drink",
    "march": "March Sleep",
    "april": "April Relax",
    "june": "June Code",
    "july": "July Run",
    "august": "August Exercise",
    "september": "September Read",
    "october": "October Practice",
    "november": "November Enjoy",
    "december": "December Type",
    "thirteen": "New month challenge",
}


# Create your views here.
def challenges(request):
    """This function returns the main challenges page"""
    month_list = list(challenges_monthly.keys())
    context = {"months": month_list}
    return render(request, "challenges/challenges.html", context)


def challenge_by_number(request, month: int):
    """This function redirects monthly challenges by number to the corresponding month"""

    months = list(challenges_monthly.keys())

    if month < 1 or month > len(months):
        return render(request, "404.html", status=404)

    redirect_month = months[month - 1]
    redirect_path = reverse("challenge", args=[redirect_month])

    return HttpResponseRedirect(redirect_path)


def challenge(request, month: str):
    """This function returns the monthly challenge page"""

    try:
        text = challenges_monthly[month]
        context = {"month": month, "text": text}
        return render(request, "challenges/challenge.html", context)
    except KeyError:
        return render(request, "404.html", status=404)

