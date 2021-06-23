from .models import Answer, Entry, Word
from django.test import TestCase
from .services import score_service

class ScoreAnswerTests(TestCase):

    # This is the bare minimum, we can add more entries especially to test other parts of the logic.
    @classmethod
    def setUpTestData(cls):
        word = Word(name='TestWord')
        word.save()
        entry = Entry(word=word, book='TestBook', chapter=1, verse=1)
        entry.save()

    def test_no_part_of_answer_correct(self):
        expected_score = 0
        answer = self.get_answer_with_nothing_correct()
        result = score_service.score_answer(answer)
        self.assertIs(result, expected_score)

    def test_only_book_correct(self):
        expected_score = 10
        answer = self.get_answer_with_only_book_correct()
        result = score_service.score_answer(answer)
        self.assertIs(result, expected_score)

#### Answer Factory (Functions that generate different types of answers to use in tests)
    def get_answer_with_nothing_correct(self):
        return Answer('TestWord', 'BadBook', 0, 0)

    def get_answer_with_only_book_correct(self):
        return Answer('TestWord', 'TestBook', 0, 0)
