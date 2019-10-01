from django.db import models

# Create your models here.

TITLE_CHOICES = (
   ('MR', 'Mr.'),
   ('MRS', 'Mrs.'),
   ('MS', 'Ms.'),
)

from django.core.exceptions import ValidationError

def title_validator(value):
    print('test validation')
    #if value not in [p[0] for p in TITLE_CHOICES]:
    #raise ValidationError('title is not valid')


class Author(models.Model):
    name = models.CharField(max_length=100, validators=[title_validator])
    title = models.CharField( max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

class Journal(models.Model):
    from django.utils import timezone
    title = models.CharField(max_length=100)
    pub_date = models.DateField( default=timezone.now(), editable=False)

class Article(models.Model):
    headline = models.CharField(
         max_length=200,
         null=True,
         blank=True,
         help_text='Use puns liberally')
    content = models.TextField()
