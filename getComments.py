import requests
import re
import json
import time
from requests.exceptions import RequestException

def getHtml(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_13+3) '
                          + 'Applewebit/537.36(KHTML,like Gecko) Chorme/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def Write_To_Text(content):
    with open("E:\豆瓣影评\差评.txt",'a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n\n')

def Parse_One_Page(html):
    partern='<span class="short">(.*?)</span>'
    items =re.findall(partern, html)
    for item in items:
        Write_To_Text(item)

def main(offset):
    url='https://movie.douban.com/' \
        +'subject/25882296/comments?start='+str(offset)\
        + '&limit=20&sort=new_score&status=P&percent_type=l'
    html = getHtml(url)
    Parse_One_Page(html)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*20)
        time.sleep(0)

