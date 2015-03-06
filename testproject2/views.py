from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from testproject2.models import Questions, Answers
import urlparse
import random
# Create your views here.

def splash_page(request):
    number_questions = Questions.objects.count()
    question_ids = Questions.objects.values_list('id', flat=True)
    question_count = len(question_ids)
    question_id = question_ids[random.randint(1, number_questions) - 1]
    random_question = Questions.objects.get(pk = question_id)
    context = {'random_question' : random_question}

    return render(request, 'testproject2/index.html', context)

def submit_results(request):
    try:
        user_ip = request.META['REMOTE_ADDR']
    except KeyError:
        user_ip = 'unknown'
    a = Answers(answer_text=request.POST['question_response'], answer_ip=user_ip)
    a.save()

    return HttpResponseRedirect(reverse('results_page',))

def results_page(request):
    
    try:
        urlparse.parse_qs(request.META['QUERY_STRING'])['new_question']
        context = {'header' : 'Thanks for helping!'}
    except KeyError:
        context = {'header' : 'Thanks for answering!'}

    return render(request, 'testproject2/results.html', context)

def post_new_question(request):
    q = Questions(question_text=request.POST['new_question'])
    q.save()
    
    qDict = QueryDict('', mutable=True)
    qDict.update({'new_question' : True})
    query_string = qDict.urlencode()
    reverse_url = reverse('results_page',)
    redirect_url = "%s%s%s" % (reverse_url,'?', query_string)
    return HttpResponseRedirect(redirect_url)
