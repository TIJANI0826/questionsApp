from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Question, Subjects


# Create your views here.


def listsubjects(request):
    questions = Question.objects.filter()
    subjects = []
    for question in questions:
        subjects.append(question.subject)

    context = {'question':questions, 'subjects': subjects}
    return render(request,'ischolar/question_list.html', context)