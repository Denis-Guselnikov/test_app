from django.contrib import admin

from . import models



@admin.register(models.QuizCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image'] 
    empty_value_display = '-empty-'   


@admin.register(models.QuestionsCategory)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['question', 'level', 'time_limit', 'category']
    list_filter = ['category', 'level']    
    empty_value_display = '-empty-'
