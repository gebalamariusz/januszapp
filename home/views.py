from django.shortcuts import render
from django.views import generic
from django.http import HttpRequest
from .models import Category, Question
import random


class CategoryList(generic.ListView):
    model = Category
    template_name = 'home/index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['title'] = 'Kategorie'
        return context


class QuestionList(generic.DetailView):
    queryset = Category.objects.all()
    template_name = 'home/questions.html'

    def get_context_data(self, **kwargs):
        answerCounter = Question.objects.filter(category=self.kwargs['pk']).count()
        # Wyfiltruj wszystkie odpowiedzi, których kategoria jest równa ilości kategorii z kluczem głównym tabeli Category, a następnie policz je
        context = super(QuestionList, self).get_context_data(**kwargs)
        context['rndAns'] = random.randint(1, answerCounter)
        context['title'] = 'Test'
        return context
