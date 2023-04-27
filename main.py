import requests
import json

url = 'https://zhibo.sina.com.cn/api/zhibo/feed?zhibo_id=152&id=&tag_id=0&page=1&page_size=30&type=0'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36 Edg/112.0.1722.58 '
}

f = open('README.md', 'w')
f.write('# 新浪财经新闻\n')
r = requests.get(url=url, headers=headers)
json_data = json.loads(r.text)
print(json_data['result']['timestamp'])
print(json_data['result']['status'])
data_list = json_data['result']['data']['feed']['list']
for item in data_list:
    date = item['create_time']
    text = item['rich_text']
    f.write('`' + date + '` ' + text + '\n\n')
f.close()
