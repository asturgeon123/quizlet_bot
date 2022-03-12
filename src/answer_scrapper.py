from src.google_scrape import get_quizlet_links
from src.quizlet_scrapper import get_quizlet_pairs
#from fuzzywuzzy import process
from thefuzz import process #Updated Version


def get_best(query,questions,answers):
    question = "Not Found"
    answer = "Not Found"


    highest_question = process.extractOne(query,questions)
    highest_answer = process.extractOne(query,answers)

    if highest_question > highest_answer:
        index = highest_question.index(highest_question[0])
        answer = answers[index]
        question = questions[index]

    elif highest_question < highest_answer:
        index = highest_answer.index(highest_answer[0])
        answer = questions[index]
        question = answer[index]

    #print("THE ANSWER")
    #print(answer,question)
    #print(questions)
    return (question,answer)

def get_page_pair(query,url): #A function to get the best match pair on the quizlet page
        questions,answers = get_quizlet_pairs(url)
        highest_question = process.extractOne(query,questions)
        highest_answer = process.extractOne(query,answers)

        if highest_question > highest_answer:
            index = highest_question.index(highest_question[0])
            answer = answers[index]
            question = questions[index]

        elif highest_question < highest_answer:
            index = highest_answer.index(highest_answer[0])
            answer = questions[index]
            question = answer[index]

        #print("THE ANSWER")
        #print(answer,question)
        #print(questions)
        return (question,answer,url)



def find_answer(query):
    answers = []
    questions = []
    for url in get_quizlet_links("quizlet"+query):
        try:
            questions,answers = get_quizlet_pairs(url)
            pair1, pair2 = get_best(query,questions,answers)

            questions.append(pair1)
            answers.append(pair2)
        except TypeError:
            pass

    question, answer = get_best(query,questions,answers)
    print("Final Answer")
    print(question,answer)
    return (question, answer)




if __name__ == "__main__":
    question = """2. A flight instructor's certificate with multi-engine and instrument ratings expires. What will reinstate the certificate?

    A. A practical test in a single engine airplane will renew all the ratings.
    B. A practical test in a multi-engine airplane reinstates both single and multi-engine privileges but not instrument.
    C. An instrument practical test in a multi-engine airplane is required to reinstate the certificate and the ratings."""


    find_answer(question)