from time import sleep
import fake_useragent
import requests
from bs4 import BeautifulSoup as BS


def json_responce(js: str) -> list[dict] | dict:
    ses = requests.Session()

    responce = ses.get('https://www.jsonkeeper.com/')
    soup = BS(responce.text, 'lxml')
    csrf_token = soup.find('form', method='post').find('input').get('value')

    user = fake_useragent.UserAgent().random
    res = ses.post('https://www.jsonkeeper.com/hostings',
                   headers={'User-Agent': user},
                   allow_redirects=True,
                   data={"json": js, "commit": "Save", "_csrf": csrf_token}
                   )

    soup = BS(res.text, 'lxml')
    link = 'https://www.' + soup.find('div', class_="alert alert-primary").text.split(':')[-1].strip(' /')
    sleep(1)
    result = ses.get(link.strip()).json()

    return result


def correction(versions: list[str], count: int) -> str:
    bad_round = range(11, 15)
    st_cn = '0' + str(count)
    last_number = st_cn[-1]
    last_numbers = st_cn[-2:]

    if int(last_numbers) not in bad_round and last_number == '1':
        return versions[0]
    elif int(last_numbers) not in bad_round and last_number in '234':
        return versions[1]
    else:
        return versions[2]
