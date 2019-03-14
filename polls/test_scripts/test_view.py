from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

import datetime

from polls import models

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return models.Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        """
        if no questions exist, an approprite message is displayed
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_questions'], [])

    def test_past_question(self):
        """
        questions with pub_date in the past are displayed on the index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_questions"],
        ["<Question: Past question.>"])

    def test_future_question(self):
        """
        questions with pub_date in the future are not displayed on
        the index page.
        """
        create_question(question_text="future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_questions"],[])

    def test_future_question_and_past_question(self):
        """
        event if both past and future question exist, only past question are
        displayed on the index page.
        """
        create_question(question_text="Future question.", days=30)
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_questions"],
        ["<Question: Past question.>"])

    def test_two_past_question(self):
        """
        index page can display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_questions"],
        ["<Question: Past question 2.>", "<Question: Past question 1.>"])

class QuestionDetailViewTest(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="future question.", days=30)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual( response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text
        """
        past_question = create_question(question_text="Past question.", days=-30)
        url = reverse("polls:detail", args=(past_question.id, ))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
