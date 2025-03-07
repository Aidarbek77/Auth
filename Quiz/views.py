from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import Quiz, Question, Answer
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer

# === CRUD для Админа ===

# 1. Получение списка квизов / Создание нового
@api_view(['GET', 'POST'])
@permission_classes([IsAdminUser])
def quiz_list(request):
    if request.method == 'GET':
        quizzes = Quiz.objects.all()
        serializer = QuizSerializer(quizzes, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 2. Детали квиза / Обновление / Удаление
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def quiz_detail(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)

    if request.method == 'GET':
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuizSerializer(quiz, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        quiz.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 3. CRUD для вопросов
@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_question(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(quiz=quiz)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
