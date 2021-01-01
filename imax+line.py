#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200828&screencodes=&screenratingcode=&regioncode='
url2 = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20200826&screencodes=&screenratingcode=&regioncode='

TOKEN = 'your token'
TARGET_URL = 'https://notify-api.line.me/api/notify'
cnt = 0

requests.post(TARGET_URL, headers={'Authorization':'Bearer ' + TOKEN}, data={'me
ssage': '아이맥스 알리미 시작'})

response = requests.post(
                TARGET_URL,
                headers={
                    'Authorization': 'Bearer ' + TOKEN
                },
                data={
                    'message': '용산 아이맥스 테넷 오픈예정'
                }
            )

def job_function():
    global cnt
    cnt += 1
    print(str(cnt) + ' Still running')
    html = requests.get(url)
    html2 = requests.get(url2)
    soup = BeautifulSoup(html.text, 'html.parser')
    soup2 = BeautifulSoup(html2.text, 'html.parser')
    imax = soup.select_one('span.imax')
    imax2 = soup.select_one('span.imax')
    TARGET_URL = 'https://notify-api.line.me/api/notify'
    TOKEN = 'your token'

    print(imax)
    if(imax2):
        requests.post(TARGET_URL, headers={'Authorization':'Bearer ' + TOKEN}, d
ata={'message': '26일 열림'})
        
    if(imax):
        imax = imax.find_parent('div',class_='col-times')
        title = imax.select_one('div.info-movie>a>strong').text.strip()
        try:
            response = requests.post(
                TARGET_URL,
                headers={'Authorization': 'Bearer ' + TOKEN},
                data={'message': '영화가 오픈했다 예매하러 뛰어가라'}
            )
            response = requests.post(
                TARGET_URL,
                headers={'Authorization': 'Bearer ' + TOKEN},
                data={'message': '빨리가 빨리'}
            )
            response = requests.post(
                TARGET_URL,
                headers={'Authorization': 'Bearer ' + TOKEN},
                data={'message': '빨리!!!!!!!!!!!!!!!!!!!!!!!'}
            )

        except Exception as ex:
            print(ex)

        sched.pause()

    if (cnt%1000) == 0:
        response = requests.post(TARGET_URL,
                                 headers={'Authorization': 'Bearer ' + TOKEN},
                                 data={'message': '아직 안열렸습니다'})

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=15)
sched.start()
