from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from .models import Question


@require_GET
def index(request):
    """
    Affiche la page d'accueil
    :param request: Requête
    :return: index.html
    """
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


@require_GET
def detail(request, question_id):
    """
    Affiche les détails de la question dont l'ID est donné en paramètre
    :param request: Requête
    :param question_id: ID de la question
    :return: detail.html (question_id)
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


@require_GET
def results(request, question_id):
    """
    Affiche les résultats de la question dont l'ID est donné en paramètre
    :param request: Requête
    :param question_id: ID de la question
    :return: Résultat de la question donnée
    """
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


@require_GET
def vote(request, question_id):
    """
    Affiche le vote de la question dont l'ID est donné en paramètre
    :param request: Requête
    :param question_id: ID de la question
    :return: Vote de la question donnée
    """
    return HttpResponse("You're voting on question %s." % question_id)

