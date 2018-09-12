from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.CategoryList.as_view(), name='category'),
    path('<int:pk>/', views.QuestionList.as_view(), name='questions')
]