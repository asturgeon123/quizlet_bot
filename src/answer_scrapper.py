from src.google_scrape import get_quizlet_links
from src.quizlet_scrapper import get_quizlet_pairs
#from fuzzywuzzy import process
from thefuzz import process #Updated Version


class answer:
    def __init__(self, query):

        self.query = query
        

    def find_best(self):
        #highest = process.extractOne(query,questions)
        pass


    def find(self):
        quiz_links = get_quizlet_links("quizlet"+self.query) #Get First Link
        try:
            questions,answers = get_quizlet_pairs(quiz_links[0])
            highest = process.extractOne(self.query,questions)
            print(highest)

            index = questions.index(highest[0])
            final_answer = answers[index]

            print("THE ANSWER")
            print(final_answer)
            #print(questions)
            return_data = {"questions":questions,"answers":answers,"final_question":highest[0],"final_answer":final_answer,"answer_link":quiz_links[0]}
            return return_data
            
        except IndexError:
            return ("Not Found","Not Found")




if __name__ == "__main__":
    question = """mitrocondria"""

    a = answer(question).find()
    print(a)