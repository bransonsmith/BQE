from ..models import Answer, Entry, Word

def score_answer(answer: Answer):
    score = 0

    word = Word.objects.filter(name=answer.word).first()
    book_entries = Entry.objects.filter(word=word, book=answer.book)
    if len(list(book_entries)):
        score += 10

    return score
