from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello Rifqi")

def detail(request, question_id):
    return HttpResponse(f"You Look At The Question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You Look At The Results of Question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're Voting on Question {question_id}")