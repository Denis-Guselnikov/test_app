from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from . import models

@login_required
def index(request):
    """Выводит шаблон главной страницы"""
    catData = models.QuizCategory.objects.all()    
    context = {'catData': catData}
    return render(request, 'main/home.html', context)


def cat_question(request, cat_id):
    """Вопросы Категории"""    
    category = get_object_or_404(models.QuizCategory, id=cat_id)       
    question = models.QuestionsCategory.objects.filter(category=category).order_by('id').first()
    context = {'question': question,'category': category}
    return render(request, 'main/category_question.html', context)


def submit_answer(request, cat_id, quest_id):
    """"""    
    if request.method == 'POST':
        category = get_object_or_404(models.QuizCategory, id=cat_id)       
        question = models.QuestionsCategory.objects.filter(
            category=category, id__gt=quest_id).exclude(id=quest_id).order_by('id').first()

        if 'skip' in request.POST:
            if question:
                context = {'question': question,'category': category}
                return render(request, 'main/category_question.html', context) 
        if question:
            context = {'question': question,'category': category}
            return render(request, 'main/category_question.html', context)       
        else:
            return HttpResponse('Больше нет вопросов!')
    else:
        return HttpResponse('Метод не разрешен!')


def result(request):
    return render(request, 'main/result.html')
