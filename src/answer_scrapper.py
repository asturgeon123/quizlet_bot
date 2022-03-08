from src.google_scrape import get_quizlet_links
from src.quizlet_scrapper import get_quizlet_pairs
from fuzzywuzzy import process




def find_answer(query):
    quiz_links = get_quizlet_links(query) #Get First Link
    try:
        questions,answers = get_quizlet_pairs(quiz_links[0])
        highest = process.extractOne(query,questions)
        print(highest)

        index = questions.index(highest[0])
        answer = answers[index]

        print("THE ANSWER")
        print(answer)
        #print(questions)
        return (questions,answer)
        
    except IndexError:
        return ("Not Found","Not Found")



if __name__ == "__main__":
    question = """2. A flight instructor's certificate with multi-engine and instrument ratings expires. What will reinstate the certificate?

    A. A practical test in a single engine airplane will renew all the ratings.
    B. A practical test in a multi-engine airplane reinstates both single and multi-engine privileges but not instrument.
    C. An instrument practical test in a multi-engine airplane is required to reinstate the certificate and the ratings."""


    find_answer(question)