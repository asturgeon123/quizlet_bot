
try:
    from src.google_scrape import get_quizlet_links
    from src.quizlet_scrapper import get_quizlet_pairs
except ModuleNotFoundError:
    from google_scrape import get_quizlet_links
    from quizlet_scrapper import get_quizlet_pairs

#from fuzzywuzzy import process
from thefuzz import process #Updated Version
import os
import multiprocessing as mp


import time

def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print('Function:{0} ExTime: {3} sec'.format(f.__name__, args, kw, round(te-ts,3)))
        return result
    return timed



class answer:
    def __init__(self):
        self.num_searchpages = 50 #Number of pages to search for answers on
        self.mode = "duel" #simple = Search only questions, duel = search questions & answers
        self.multi_threading = False #multithreading on or off


    @timeit
    def find_best(self,query):
        self.query = query
        quiz_links = get_quizlet_links("quizlet"+self.query)


        print("[2] Levinsteining Pages...")
        if len(quiz_links) > self.num_searchpages:
            quiz_links = quiz_links[:self.num_searchpages]

        if self.multi_threading == True:
            pool = mp.Pool(processes=os.cpu_count())
            results = pool.map(self.find, quiz_links)
        elif self.multi_threading == False:
            results = []
            for link in quiz_links:
                results.append(self.find(link))


        index = 0
        highest = 0
        count = 0
        for i in results:
            try:
                if i['match_score'] > highest:
                    highest = i['match_score']
                    index = count
                
            except TypeError:
                continue
            count += 1   
        print("    -- Processed {0} pages".format(count))
        return results[index]


    def find(self,link):
        #Find best answer or question on page and return it
        try:
            questions,answers = get_quizlet_pairs(link)
            highest_questions = process.extractOne(self.query,questions)

            if self.mode == "simple":
                highest = highest_questions
            else:
                highest_answers = process.extractOne(self.query,answers)
                if highest_questions > highest_answers:
                    highest = highest_questions
                else:
                    highest = highest_answers
                    answers, questions = questions, answers #swap question and answer variables
                    print("SWAPPED")

            index = questions.index(highest[0])
            final_answer = answers[index]


            #print("THE ANSWER ==",final_answer)
            return_data = {"match_score":highest[1],"questions":questions,"answers":answers,"final_question":highest[0],"final_answer":final_answer,"answer_link":link}

            return return_data
        except (IndexError, TypeError):
                return_data = {"final_question":"","final_question":"NOT FOUND","answer_link":""}



if __name__ == "__main__":
    question = """Different dynamics (from softest to loudest)"""

    a = answer().find_best(question)
    #print("====================================================")
    #print(a)
    print("====================================================")
    print(a['final_question'],"\n",a['final_answer'])