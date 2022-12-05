from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('cat_question/<int:cat_id>/', views.cat_question, name='cat_question'),
    path('submit-answer/<int:cat_id>/<int:quest_id>/', views.submit_answer, name='submit_answer'),    
]