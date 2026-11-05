
# 2.2 Exercices sur les parties 1 et 2

## 2.2.1 Exercice d'administation


1. 

In [5]: from django.utils import timezone

In [6]: q = Question(question_text="Quel candidat doit être délégué ?", pub_date=timezone.now())

In [9]: q.save()

In [10]: q.choice_set.create(choice_text="Margaux Rossi", votes=5)  
Out[10]: <Choice: Margaux Rossi>

In [11]: q.choice_set.create(choice_text="Severine Diribarne", votes=7)  
Out[11]: <Choice: Severine Diribarne>

In [16]: q.choice_set.create(choice_text="Severine Hori Maitrehut", votes=
       ⋮ 4)  
Out[16]: <Choice: Severine Hori Maitrehut>

In [19]: q.save()

2. 

In [20]: q2 = Question(question_text="Préférez-vous les chats ou les chien
       ⋮ s ?", pub_date=timezone.now())

In [22]: q2.save()

In [23]: q2.choice_set.create(choice_text="Chiens", votes=11)  
Out[23]: <Choice: Chiens>

In [24]: q2.choice_set.create(choice_text="Chats", votes=10)  
Out[24]: <Choice: Chats>

In [29]: q2.choice_set.create(choice_text="Les deux", votes=7)  
Out[29]: <Choice: Les deux>

In [30]: q2.save()

In [31]: q3 = Question(question_text="Quel est votre type de console préfé
       ⋮ ré ?", pub_date=timezone.now())

In [32]: q3.save()

In [33]: q3.choice_set.create(choice_text="Nintendo", votes=32)  
Out[33]: <Choice: Nintendo>

In [34]: q3.choice_set.create(choice_text="Playstation", votes=36)  
Out[34]: <Choice: Playstation>

In [35]: q3.choice_set.create(choice_text="Xbox", votes=29)  
Out[35]: <Choice: Xbox>

In [36]: q3.save()

In [37]: q4 = Question(question_text="Quelle est votre couleur primaire pr
       ⋮ éférée ?", pub_date=timezone.now())

In [39]: q4.save()

In [40]: q4.choice_set.create(choice_text="Rouge", votes=6)  
Out[40]: <Choice: Rouge>

In [41]: q4.choice_set.create(choice_text="Jaune", votes=4)  
Out[41]: <Choice: Jaune>

In [42]: q4.choice_set.create(choice_text="Bleu", votes=5)  
Out[42]: <Choice: Bleu>

In [43]: q4.save()

In [44]: q5 = Question(question_text="Quel système d'exploitation utilisez
       ⋮ -vous le mieux ?", pub_date=timezone.now())

In [45]: q5.save()

In [46]: q5.choice_set.create(choice_text="Windows", votes=8)  
Out[46]: <Choice: Windows>

In [47]: q5.choice_set.create(choice_text="MacOS", votes=3)  
Out[47]: <Choice: MacOS>

In [48]: q5.choice_set.create(choice_text="Linux", votes=4)  
Out[48]: <Choice: Linux>

In [49]: q5.save()

In [50]: q6 = Question(question_text="Comment ça va aujourd'hui ?", pub_da
       ⋮ te=timezone.now())

In [51]: q6.save()

In [52]: q6.choice_set.create(choice_text="Très bien", votes=6)  
Out[52]: <Choice: Très bien>

In [53]: q6.choice_set.create(choice_text="Plutôt bien", votes=3)  
Out[53]: <Choice: Plutôt bien>

In [54]: q6.choice_set.create(choice_text="Bof", votes=5)  
Out[54]: <Choice: Bof>

In [55]: q6.save()

3) 

In [58]: q6  
Out[58]: <Question: Comment ça va aujourd'hui ?>

In [59]: q6.choice_set.all()  
Out[59]: <QuerySet [<Choice: Très bien>, <Choice: Plutôt bien>, <Choice: Bof>]>

4) 

### 2.2.2.2. Questions

8) 

In [1]: q = Question.objects.get(pk=1)

In [2]: d = q.choice_set.get(choice_text__contains="Not")

In [3]: d  
Out[3]: <Choice: Not much>

9)  
