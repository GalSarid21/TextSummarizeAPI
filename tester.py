import urllib.request as req
from bs4 import BeautifulSoup
import requests

TEST_ENDPOINT_DEBUG = 'http://127.0.0.1:5000/summarize-text'
TEXT_MAX_LEN = 5000

def run_test():
    yahoo_requset = req.Request(
        url='https://sports.yahoo.com/nba-fact-or-fiction-have-the-los-angeles-lakers-failed-le-bron-james-204051194.html',
        data=None, 
        headers={ 
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }
    )

    html = req.urlopen(yahoo_requset).read().decode('utf-8')
    text = BeautifulSoup(html, features='html.parser').text
    
    if len(text) > TEXT_MAX_LEN:
        text = text[:TEXT_MAX_LEN]
    print('\noriginal text:\n' + text)
    
    summarizer_request_body = {'text': text}
    response = requests.post(TEST_ENDPOINT_DEBUG, json=summarizer_request_body)
    
    print('\nsummarized text:\n') 
    print(response.text)

if __name__ == '__main__':
    run_test()