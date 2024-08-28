from django.shortcuts import render, get_object_or_404, redirect
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
    
    # try: 
    # q = Question.objects.get(id=question_id)
    # except Question.DoesNotExist:
    # raise Http404('Question {} does not exist.'.format(question_id))

    q = get_object_or_404(Question, id=question_id)

    return render(request, 'polls/detail.html', {'question' : q})
    

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # print(request.POST)
    # return HttpResponse('vote')
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice_select'])
        # request.POST['choice_select'] :
        # detail.html의 <input type="radio" name="choice_select" value="{{ choice.id }}">에서 날라온 값
        # form으로 제출된 POST Request 전체에서 'choice_select'가 name인 HTML 태그의 value를 꺼내는 코드
        # request.POST 는 {~~~, 'choice_select':7} 와 같은 dictionary 형태
    except:
        # request.POST['choice_select']값이 없을 경우, error_message를 가지고 details.html로 되돌아감
        context = {'question': question, 'error_message': "You didn't select a choice."}
        return render(request, 'polls/detail.html', context)
    else: # try 문에서 에러가 발생하지 않았을 경우 마지막에 실행됩니다.
        selected_choice.votes += 1
        selected_choice.save() # 실제 DB 저장
        return redirect('polls:results', question_id=question.id)


def results(request, question_id):
    response = "You're looking at the results of question {}."
    return HttpResponse(response.format(question_id))
