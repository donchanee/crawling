import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
}
plus_url = "http://www.dunkindonuts.co.kr/"

for i in range(0, 4135):
    pagenum = i
    print(pagenum)
    URL = 'http://www.dunkindonuts.co.kr/event/view.php?S='+str(pagenum)+'&flag='
    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')

    try:
        target=soup.select_one('div.event_view_content > p > img')
        print(target['src'])
    except:
        continue

    urlretrieve(plus_url+target['src'], 'C:/Users/dongchan/Downloads/a'+str(pagenum)+'.jpg') 

