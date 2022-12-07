from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from . import models


@login_required
def index(request):
    """Выводит шаблон главной страницы"""
    catData = models.QuizCategory.objects.all()
    context = {'catData': catData}
    return render(request, 'main/home.html', context)


@login_required
def cat_question(request, cat_id):
    """Вопросы Категории"""
    category = get_object_or_404(models.QuizCategory, id=cat_id)
    question = models.QuestionsCategory.objects.filter(category=category).order_by('id').first()
    context = {'question': question, 'category': category}
    return render(request, 'main/category_question.html', context)


@login_required
def submit_answer(request, cat_id, quest_id):
    """Отправка ответа"""
    if request.method == 'POST':
        category = get_object_or_404(models.QuizCategory, id=cat_id)
        question = models.QuestionsCategory.objects.filter(
            category=category, id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
        quest = models.QuestionsCategory.objects.get(id=quest_id)
        user = request.user
        answer = request.POST['answer']
        models.UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
        if question:
            context = {'question': question, 'category': category}
            return render(request, 'main/category_question.html', context)
        else:
            result = models.UserSubmittedAnswer.objects.filter(user=request.user)
            rightAnswer = 0
            percentage = 0
            for row in result:
                if row.question.right_option == row.right_answer:
                    rightAnswer += 1
            percentage = (rightAnswer*100)/result.count()
            context = {'result': result, 'rightAnswer': rightAnswer, 'percentage': percentage}
            return render(request, 'main/result.html', context)
    else:
        return HttpResponse('Метод не разрешен!')
