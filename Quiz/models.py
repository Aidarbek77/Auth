from django.db import models
from django.conf import settings

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    question_text = models.TextField()
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    answer_text = models.TextField()

    def __str__(self):
        return self.answer_text

class UserAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.quiz.title} - {self.score}"
