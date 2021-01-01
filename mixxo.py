import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

TOKEN = ### YOUR TOKEN ###
TARGET_URL = 'https://notify-api.line.me/api/notify'

requests.post(TARGET_URL, headers={'Authorization':'Bearer ' + TOKEN}, data={'message': '할인 알리미'})

def job():
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }

    url = "http://mixxo.elandmall.com/goods/initGoodsDetail.action?goods_no=2011314422"
    res = session.get(url, headers=headers).content
    soup = BeautifulSoup(res, 'html.parser')
    price = soup.find('meta', property = 'recopick:sale_price')
    TOKEN = ### YOUR TOKEN ###
    TARGET_URL = 'https://notify-api.line.me/api/notify'
    
    if int(price["content"].replace(',','')) < 49000:
        response = requests.post(TARGET_URL,
                headers={'Authorization': 'Bearer ' + TOKEN},
                data={'message': '할인 시작!'}
        )
        
        sched.pause()

sched = BlockingScheduler()
sched.add_job(job, 'interval', seconds=86400)
sched.start()
