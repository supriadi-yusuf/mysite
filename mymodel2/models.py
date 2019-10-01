from django.db import models

from mymodel import models as model1

# Create your models here.

class ChildB(model1.Descendant):
    age = models.PositiveIntegerField()
