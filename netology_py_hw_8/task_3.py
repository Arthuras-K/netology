import requests
import datetime
import time

from pprint import pprint


def get_questions(tag, tm):
    url = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'
    prm = {'fromdate': tm, 'tagged': tag}
    response = requests.get(url, params=prm)
    print('Код ответа:', response.status_code)
    return response.json()


if __name__ == '__main__':
    # Проверка методов со временем
    # print(datetime.datetime.now())
    # print(datetime.date.today())
    # print(time.time())

    tag = 'Python'
    tm = int(time.time() - 2*(24*60*60)) #из актуального времени вычитается два дня

    pprint(get_questions(tag, tm))

