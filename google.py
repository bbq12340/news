from bs4 import BeautifulSoup
import requests
import pandas as pd

user_agent = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
}

title_class = "JheGif"
company_class = "XTjFC"
summary_class = "Y3v8qd"
href_class = "dbsr"

TITLE = []
COMPANY = []
SUMMARY = []
HREF = []


def query_google(q: str, p: int, enable_recent: bool):
    if enable_recent == False:
        r =requests.get(f'https://www.google.com/search?q={q}&source=lnms&tbm=nws&start={p*10}', headers=user_agent)
        soup = BeautifulSoup(r.text, 'html.parser')
    else: 
        r =requests.get(f'https://www.google.com/search?q={q}&source=lnms&tbm=nws&tbs=sbd:1&start={p*10}', headers=user_agent)
        soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_function(soup):
    s = soup.find_all("div", {"class": f"{title_class}"})
    for t in s:
        TITLE.append(t.text)

    s = soup.find_all("div", {"class": f"{company_class}"})
    for t in s:
        COMPANY.append(t.text)

    s = soup.find_all("div", {"class": f"{summary_class}"})
    for t in s:
        SUMMARY.append(t.text.replace("\n", ""))
        
    s = soup.find_all("div", {"class": f"{href_class}"})
    for u in s:
        h = u.find('a')['href']
        HREF.append(h)
    return 

def search_google(num, query, enable_recent = False):
    if enable_recent == False:
        for i in range(0, num):
            soup = query_google(query, i, enable_recent=False)
            get_function(soup)
    else:
        for i in range(0, num):
            soup = query_google(query, i, enable_recent=True)
            get_function(soup)
    data = {
        '제목': TITLE,
        '보도사': COMPANY,
        '요약': SUMMARY,
        '링크': HREF
    }
    df = pd.DataFrame(data)
    #df.to_csv('google.csv')
    return df
