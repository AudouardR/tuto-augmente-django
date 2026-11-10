from django import forms


class QuestionForm(forms.Form):
    question_text = forms.CharField(label="Question", max_length=200)
    choice1 = forms.CharField(label="Proposition 1", max_length=200)
    choice2 = forms.CharField(label="Proposition 2", max_length=200)
    choice3 = forms.CharField(label="Proposition 3", max_length=200, required=False)
    choice4 = forms.CharField(label="Proposition 4", max_length=200, required=False)
    choice5 = forms.CharField(label="Proposition 5", max_length=200, required=False)