from django.test import TestCase

import datetime
from django.utils import timezone
from . import models

# Create your tests here.

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently returns False for question whose pub_date  is
        in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = models.Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently returns False for question whose pub_date is
        older than 1 day.
        """
        time = timezone.now() + datetime.timedelta(days=1,seconds=1)
        old_question = models.Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently return True for question whose pub_date is
        within the last_day
        """
        #time = timezone.now()
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = models.Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
