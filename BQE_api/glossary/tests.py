from .models import Answer, Entry, Word
from django.test import TestCase
from .services import score_service

class ScoreAnswerTests(TestCase):

    ### SET THESE FOR THE TESTS TO CHECK THESE SPECIFIC VALUES
    WRONG_SCORE = 0
    BOOK_SCORE = 10
    BOOK_AND_CHAPTER_SCORE = 25
    BOOK_CHAPTER_AND_VERSE_SCORE = 50

    # This is the bare minimum, we can add more entries especially to test other parts of the logic.
    @classmethod
    def setUpTestData(cls):
        word = Word(name='TestWord')
        word.save()
        entry = Entry(word=word, book='TestBook', chapter=1, verse=1)
        entry.save()
        entry = Entry(word=word, book='TestBook2', chapter=2, verse=2)
        entry.save()
        entry = Entry(word=word, book='TestBook3', chapter=3, verse=3)
        entry.save()
        entry = Entry(word=word, book='TestBook2', chapter=1, verse=1)
        entry.save()

    def test_no_part_of_answer_correct(self):
        expected_score = self.WRONG_SCORE
        answer = self.get_answer_with_nothing_correct()
        result = score_service.score_answer(answer)
        self.assertIs(result, expected_score)

    def test_only_book_correct(self):
        expected_score = self.BOOK_SCORE
        answer = self.get_answer_with_only_book_correct()
        result = score_service.score_answer(answer)
        self.assertIs(result, expected_score)

    def test_only_book_correct_lowercase(self):
        expected_score = self.BOOK_SCORE
        answer = self.get_answer_with_only_book_correct_lowercase()
        result = score_service.score_answer(answer)
        self.assertIs(result, expected_score)

    def test_only_book_and_chapter_correct(self):
        expected_score = self.BOOK_AND_CHAPTER_SCORE
        answer = self.get_answer_with_only_book_and_chapter_correct()
        result = score_service.score_answer(answer)
        self.assertIs(result, expected_score)

    def test_all_correct(self):
        expected_score = self.BOOK_CHAPTER_AND_VERSE_SCORE
        answer = self.get_answer_with_all_correct()
        result = score_service.score_answer(answer)
        self.assertIs(result, expected_score)

    def test_only_chapter_verse_correct(self):
        expected_score = self.WRONG_SCORE
        answer = self.get_answer_with_only_chapter_verse_correct()
        result = score_service.score_answer(answer)
        self.assertIs(result, expected_score)

    def test_only_book_and_verse_correct(self):
        expected_score = self.BOOK_SCORE
        answer = self.get_answer_with_only_book_and_verse_correct()
        result = score_service.score_answer(answer)
        self.assertIs(result, expected_score)

    def test_word_does_not_exist(self):
        expected_score = self.WRONG_SCORE
        answer = self.get_answer_with_word_that_is_not_in_db()
        result = score_service.score_answer(answer)
        self.assertIs(result, expected_score)

#### Answer Factory (Functions that generate different types of answers to use in tests)
    def get_answer_with_nothing_correct(self):
        return Answer('TestWord', 'BadBook', 0, 0)

    def get_answer_with_only_book_correct(self):
        return Answer('TestWord', 'TestBook', 0, 0)

    def get_answer_with_only_book_and_chapter_correct(self):
        return Answer('TestWord', 'TestBook', 1, 0)

    def get_answer_with_all_correct(self):
        return Answer('TestWord', 'TestBook', 1, 1)

    def get_answer_with_only_book_correct_lowercase(self):
        return Answer('TestWord', 'testbook', 0, 0)

    def get_answer_with_only_chapter_verse_correct(self):
        return Answer('TestWord', 'BadBook', 1, 0)
    
    def get_answer_with_only_book_and_verse_correct(self):
        return Answer('TestWord', 'TestBook', 0, 1)

    def get_answer_with_chapter_verse_of_another_entry_correct(self):
        return Answer('TestWord', 'TestBook', 2, 2)

    def get_answer_with_word_that_is_not_in_db(self):
        return Answer('BadWord', 'TestBook', 1, 1)
