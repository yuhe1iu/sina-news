import requests
import json
from requests.adapters import HTTPAdapter

url = 'https://zhibo.sina.com.cn/api/zhibo/feed?zhibo_id=152&id=&tag_id=0&page=1&page_size=30&type=0'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36 Edg/112.0.1722.58 '
}
MAX_RETRIES = 5
s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=MAX_RETRIES))
s.mount('https://', HTTPAdapter(max_retries=MAX_RETRIES))


def get():
    r = None
    try:
        r = s.get(url=url, headers=headers)
    except requests.exceptions.RequestException as e:
        print(e)
    return r


def render(html):
    data_list = None
    try:
        json_data = json.loads(html)
        print(json_data['result']['timestamp'])
        print(json_data['result']['status'])
        data_list = json_data['result']['data']['feed']['list']
    except Exception as e:
        print(e)
    if data_list is None:
        print('数据解析失败')
        return
    f = open('README.md', 'w')
    f.write('# 新浪财经新闻\n')
    for item in data_list:
        date = item['create_time']
        text = item['rich_text']
        f.write('`' + date + '` ' + text + '\n\n')
    f.close()


if __name__ == '__main__':
    resp = get()
    if resp is None:
        print('获取数据失败')
    else:
        render(resp.text)
