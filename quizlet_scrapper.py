import requests
from bs4 import BeautifulSoup

def get_quizlet_pairs(url):

    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')

    question_list = []
    answer_list = []

    for i, (question, answer) in enumerate(zip(soup.select('a.SetPageTerm-wordText'), soup.select('a.SetPageTerm-definitionText')), 1):
        question_list.append(question.get_text(strip=True, separator='\n'))
        answer_list.append(answer.get_text(strip=True, separator='\n'))


    return (question_list,answer_list)
