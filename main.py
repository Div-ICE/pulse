from http import HTTPStatus
import requests


api_addr = ['https://jsonplaceholder.typicode.com',
            'http://188.127.251.4:8240', ]
count = 0
mirror = 0
max_mirror = len(api_addr)


def api_answer(id):
    """Функция делает максимум 30 запросов на каждое из зеркал"""
    global count
    global mirror
    count += 1
    if count == 29:
        count = 1
        mirror += 1
        if mirror == len(api_addr):
            mirror = 0
    url = api_addr[mirror]+'/posts/'+str(id)
    try:
        response = requests.get(url)
    except requests.RequestException as exeption:
        raise ConnectionError(f'Error: {exeption}')
    if response.status_code != HTTPStatus.OK:
        chek_message = (
            f'URL {url} is not availible',
            f'HTTP status: {response.status_code}'
        )
        raise Exception(chek_message)
    userid = response.json()['userId']
    id = response.json()['id']
    title = response.json()['title']
    body = response.json()['body']
    return userid, id, title, body


if __name__ == "__main__":
    print(api_answer(1000))
