import requests, json
from apscheduler.schedulers.blocking import BlockingScheduler

TOKEN = '[YOUR_TOKEN]'
TARGET_URL = 'https://notify-api.line.me/api/notify'

requests.post(TARGET_URL,
              headers={'Authorization':'Bearer ' + TOKEN},
              data={'message': '롯시 알리미 시작'})
cnt = 0

def job_function():
    global cnt
    cnt += 1
    url = "https://www.lottecinema.co.kr/LCWS/Ticketing/TicketingData.aspx"
    dic = {"MethodName":"GetPlaySequence",
           "channelType":"HO",
           "osType":"W",
           "osVersion":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
           "playDate":"2021-02-27",
           "cinemaID":"1|0001|1016",
           "representationMovieCode":"16888"}
    param = {"paramList": str(dic)}
    response = requests.post(url, data = param).json()
    if response['PlaySeqsHeader']['Items'][0]['BookingSeatCount'] > 0:
        requests.post(TARGET_URL,
                      headers={'Authorization':'Bearer ' + TOKEN},
                      data={'message': '취소표 열림'})
    if cnt % 10000 == 0:
        requests.post(TARGET_URL,
                      headers={'Authorization':'Bearer ' + TOKEN},
                      data={'message': '동작중...'})
        
sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=3)
sched.start()
