import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200828&screencodes=&screenratingcode=&regioncode='

TOKEN = 'PK'
TARGET_URL = 'https://notify-api.line.me/api/notify'

def job_function():
    print('Still running')
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')

    print(imax)

    if(imax):
        imax = imax.find_parent('div',class_='col-times')
        title = imax.select_one('div.info-movie>a>strong').text.strip()
        message = {'message' : 'OPEN'}
        try:

            TARGET_URL = 'https://notify-api.line.me/api/notify'
            TOKEN = 'xstdws1s3PP8c6Bjznq0PX7EkACXld07uvi8qFoV9HS'

            response = requests.post(
                TARGET_URL,
                headers={
                    'Authorization': 'Bearer ' + TOKEN
                },
                data={
                    'message': '영화가 오픈했다 예매하러 뛰어가라'
                }
            )

        except Exception as ex:
            print(ex)
            
        sched.pause()


sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=15)
sched.start()
