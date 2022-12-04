from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from . import models

@login_required
def index(request):
    """Выводит шаблон главной страницы"""
    catData = models.QuizCategory.objects.all()    
    context = {
        'catData': catData,               
    }
    return render(request, 'main/home.html', context)


def cat_question(request, cat_id):
    """Вопросы Категории"""    
    category = get_object_or_404(models.QuizCategory, id=cat_id)       
    questions = models.QuestionsCategory.objects.filter(category=category)
    context = {        
        'questions': questions,
        'category': category,
    }
    return render(request, 'main/category_question.html', context)


def result(request):
    return render(request, 'main/result.html')
