import requests
import urllib
from requests_html import HTML
from requests_html import HTMLSession

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)


def scrape_google(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)
    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')
    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)
    return links

def get_quizlet_links(query):
    print("[1] Scraping Google")
    scrapper = scrape_google(query)
    links = []
    for i in scrapper:
        if "quizlet.com" in i:
            print(i)
            links.append(i)
    print("    -- Returned {0} links".format(len(links)))
    return links












if __name__ == "__main__":

    query_test = "quizlet Different dynamics (from softest to loudest)"
    get_quizlet_links(query_test)