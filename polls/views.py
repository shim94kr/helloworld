# Create your views here.
from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect,HttpResponse
from polls.models import Poll,Choice
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
"""
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
"""
def home(request):
    data = {}
    data['woohyeon'] = 'hello'
    return render(request, 'home.html', data)

def polls(request):
    data = {}
    data['polls'] = Poll.objects.all()
    return render(request, 'polls.html', data)

def polls_process(request):
    data = {}

    if request.method == "POST" :
        choice_id = request.POST["choice"]
        print "Choice ID submitted %d" % int(choice_id)
        choice_obj = Choice.objects.get(id=choice_id)
        choice_obj.votes += 1
        choice_obj.save()

    return HttpResponseRedirect(reverse("polls_list"))

@csrf_exempt
def polls_radio(request):
    import json
    data = {}

    if request.method == "POST":
        radio_id = request.POST["radio_id"]
        print "We received radio ID : %s " % radio_id
        choice_id = int(radio_id[1:])
        choice_obj = Choice.objects.get(id=choice_id)
        choice_obj.votes += 1
        choice_obj.save()

        data["radio_id"] = "v%d" % choice_id
        data["votes"] = choice_obj.votes
    else:
        print "Invalid radio button request"
    return HttpResponse(json.dumps(data),mimetype="application/json")
