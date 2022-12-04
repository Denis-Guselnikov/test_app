from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('cat_question/<int:cat_id>/', views.cat_question, name='cat_question'),
    path('result/', views.result, name='result'),
]