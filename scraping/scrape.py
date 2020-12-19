import requests
from bs4 import BeautifulSoup
import pprint


def sort_stories_by_votes(hn):
    return sorted(hn, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'href': href, 'link': title, 'votes': points})
    return sort_stories_by_votes(hn)


i = 1
isContains = False
while(isContains != True):

    res = requests.get(f'https://news.ycombinator.com/news?p={i}')
    bs = BeautifulSoup(res.text, 'html.parser')
    links = bs.select('.storylink')
    subtext = bs.select('.subtext')
    print(create_custom_hn(links, subtext), f'page={i}')
    if len(links) == 0:
        isContains = True
    i = i + 1
# print(bs.body)
# print(bs.find_all('div'))
# print(bs.select('.score'))
# print(bs.select('.score'))
# print(bs.find(id='score_25468887'))
# print(bs.a)
# print(links)

# pprint.pprint(create_custom_hn(links, subtext))
