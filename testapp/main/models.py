from django.db import models
from django.contrib.auth.models import User


class QuizCategory(models.Model):
    """
    Категория тестов
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default.png') 

    class Meta:
        verbose_name_plural = 'Категории тестов'

    def __str__(self):
        return self.title


class QuestionsCategory(models.Model):
    """
    Вопросы в категориях
    """
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question = models.TextField()
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    level = models.CharField(max_length=100)
    time_limit = models.IntegerField()
    right_option = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question


class UserSubmittedAnswer(models.Model):
    """
    Отправленные пользователем ответы
    """
    question = models.ForeignKey(QuestionsCategory, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    right_answer = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Отправленные пользователем ответы'
