from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def index(request):
    data = {
        "slackUsername": "edoka",
        "backend": True,
        "age": 22,
        "bio": "I love breaking things so as to better fix them"
    }
    return JsonResponse(data)
