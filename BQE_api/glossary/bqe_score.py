from .models import *

def find_correct_answer(answer):
    word_id = []
    word = answer['answer']['word_name']
    words = Word.objects.filter(name__startswith=word)
    for allwords in words:
        word_id += [allwords.id,]
        
    for entry in word_id:
        results = Entry.objects.filter(word_id=entry)
        
    return results
    
def get_score_for_answer(answer):
    score = 0
    results = find_correct_answer(answer)
    guess_book = answer['answer']['book']
    guess_chapter = answer['answer']['chapter'] 
    guess_verse = answer['answer']['verse']
    result_book = results.filter(book=guess_book)
    result_chapter = results.filter(book=guess_book, chapter=guess_chapter)
    result_verse = results.filter(book=guess_book, chapter=guess_chapter,verse= guess_verse)
    if len(results) == 0:
        return score 
    if len(result_book) >= 1:
        score +=3
    if len(result_chapter) >= 1:
        score +=7
    if len(result_verse) >= 1:
        score += 40
    
    return score


############################
# Defining Test Cases for the function
############################

correct_answer= [
    {
        'answer': { 
            'word_name': 'ABBA', 
            'book': 'Genesis',
            'chapter': 1,
            'verse': 1
        },
    },
    { 
        'answer': { 
            'word_name': 'ABBA', 
            'book': 'Romans',
            'chapter': 8,
            'verse': 15
        },  
    }
]


test_cases = [
    { 
        "test_name": correct_answer[0],
        'answer': { 
            'word_name': 'ABBA', 
            'book': 'Genesis',
            'chapter': 1,
            'verse': 1
        },
        'expected_score': 0
    },
    { 
        'test_name':  correct_answer[1],
            'answer': { 
            'word_name': 'ABBA', 
            'book': 'Romans',
            'chapter': 8,
            'verse': 10
        },
        'expected_score': 10
    }
]

#######################
# Running the tests
#######################
def test_case():
    test_passes = 0

    print('\n_______________________________________')
    print('  Running Tests: get_score_for_answer')
    print('_______________________________________\n')

    for test_case in test_cases:
        result = get_score_for_answer(test_case)
        if result == test_case["expected_score"]:
            test_passes += 1
            print(f'PASS | {test_case["test_name"]} | Score: {result}')
        else:
            print(f'FAIL | {test_case["test_name"]} Expected: {test_case["expected_score"]} | Actual: {result}')

    print('\n______________________________________')
    print(f'Passed {test_passes} / {len(test_cases)} tests.\n')
