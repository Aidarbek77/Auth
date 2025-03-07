from django.urls import path
from .views import quiz_list, quiz_detail, add_question

urlpatterns = [
    path('quizzes/', quiz_list, name='quiz-list'),
    path('quizzes/<int:pk>/', quiz_detail, name='quiz-detail'),
    path('quizzes/<int:quiz_id>/questions/', add_question, name='add-question'),
]
