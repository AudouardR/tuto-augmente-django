import datetime

from django.db import models
from django.db.models import Max
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def age(self):
        age = timezone.now() - self.pub_date
        return f"{age.days} days ago"

    def get_max_choice(self):
        choices = Choice.objects.filter(question=self)
        max_choice = choices.order_by("-votes").first()
        total_votes = 0
        for choice in choices:
            total_votes += choice.votes
        if max_choice is None:
            return "Aucun choix"
        elif total_votes == 0:
            return "Aucun vote"
        else:
            return f"{max_choice}: {((max_choice.votes / total_votes) * 100):.1f} %"


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text