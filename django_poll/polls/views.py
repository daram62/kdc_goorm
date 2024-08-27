from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    # Question.objects.all()
    # id 오름차순, -id 내림차순
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    context = {'latest_question_list':latest_question_list}

    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You are looking at question {}.".format(question_id))

def vote(request, question_id):
    response = "You are voting on question {}."
    return HttpResponse(response.format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))
