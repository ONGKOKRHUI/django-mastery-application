from django.shortcuts import render
from django.db.models import F

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question

"""
Each view is responsible for doing one of two
 things: returning an HttpResponse object containing
 the content for the requested page, or raising an 
 exception such as Http404. The rest is up to you.
"""

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    # (dummy) return HttpResponse("You're voting on question %s." % question_id)


from .models import Question
#from django.template import loader (can use render shortcut instead)

""" 
displays the latest 5 poll questions in the system, 
separated by commas, according to publication date:
"""
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #template = loader.get_template("polls/index.html")
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


from django.http import Http404
"""
The new concept here: The view raises the Http404 
exception if a question with the requested ID doesn’t exist.
"""

"""def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
"""

"""
It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist.
 Django provides a shortcut. Here’s the detail() view, rewritten:
"""
from django.shortcuts import get_object_or_404, render
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

"""
There’s also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() 
instead of get(). It raises Http404 if the list is empty.
"""