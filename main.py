from bs4 import BeautifulSoup as bs
import requests
from requests.exceptions import HTTPError

import TimeTest as tt
import settings as ss

host = ss.host
url = ss.url_find_field
url_result = ss.url_result
page = requests.get(url)
cad_num_list = ss.cadastral_numbers_list
search_params = ss.search_params

headers = ss.headers

# pages_phrase = 'online_request_search_page='20'#' id='js_es4'


def GetHtml(url, params=''):
    r = requests.get(url, headers=headers, params=params)
    return r

def GetContent(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('td', class_='brdw1111')
    real_estate_object = []
    print(items)

    # for item in items:
    #     kek = item.find_all('td', class_='td')
    #     for k in kek:
    #         asd = k.find_all('a')
    #         a.append(asd)

    for item in items:
        real_estate_object.append(
            {
                'title': item.find('a').get_text(strip=True),
                'link' : url + item.find('a').get('href'),
            }
        )

def Parser():
    html = GetHtml(url)
    if html.status_code == 200:
        name = []
        num_pages = GetNumPages()
        for page in range(1, num_pages):
            print(f'Парсинг страницы №: {page}')
            html = GetHtml(url, params='online_request_search_page=7#')
    else:
        print('Parser error: ', html.status_code)

def FindCadList(url):
    f = requests.get(url, headers=headers, params=search_params)
    print(f.status_code)
    return f


def GetNumPages(html):
    td = html.find('td', {'id': 'js_es1'})
    onclick = td.get('onclick')
    # td = soup.find('td', {'id': 'js_es1'})
    td.split('online_request_search_page=')[1].split('#')[0] # get string and search MAX page number in <td onclick=>
    print(td)

    return 0


def Main():
    time1 = tt.Start('1')
    html = FindCadList(url_result)
    tt.End(time1)
    # GetContent(html.text)
    print(html.text)


if __name__ == '__main__':
    Main()