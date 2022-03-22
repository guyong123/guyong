import execjs
import requests

url = 'https://match.yuanrenxue.com/api/match/1?{}m={}'

def get_1(i,sum):
    headers = {
        'user-agent': 'yuanrenxue.project'
    }
    cookies={
        'sessionid':'kt9295elxmrk4qfcgbv7m5dknwqwttku'
    }
    with open('1.js','r',encoding='utf-8') as f:
        js = f.read()
    m = execjs.compile(js).call('jiemi')
    if i == 1:
        url_data = url.format('',m)
    else:
        url_data = url.format('page='+str(i)+'&',m)
    data = requests.get(url_data,headers=headers,cookies=cookies)
    print(data.headers)
    data = data.json()
    print(data['data'])
    for temp in data['data']:
        sum += temp['value']
    print(i,sum)
    return sum

def main():
    sum = 0
    for i in range(1,6):
        sum = get_1(i,sum)
    return sum

print(main())