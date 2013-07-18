# Create your views here.
from django.shortcuts import render_to_response
from django.http import Http404,HttpResponseRedirect
from polls.models import Poll
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    poll_list = Poll.objects.all()
    args = {'poll_list':poll_list}
    return render_to_response('index.html',args)

def detail(request, poll_id):
    try:
        p = Poll.objects.get(id=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render_to_response('detail.html',{'poll':p})

@csrf_exempt
def vote(request, poll_id):
    p = Poll.objects.get(id=poll_id)
    choice = p.choice_set.get(id=request.POST['choice'])

    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('polls.views.detail',args=(p.id,)))

def home(request):
    data = {}
    data['woohyeon'] = 'hello'
    return render(request, 'home.html', data)

def polls(request):
    data = {}
    data['polls'] = Poll.objects.all()
    return render(request, 'polls.html', data)