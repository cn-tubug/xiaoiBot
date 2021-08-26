import requests
import json
from os import path
import datetime


async def get_hpic_website(canshu, sub_type):
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API，并拼接成天气预报内容
    if sub_type == 'group':
        return "禁止偷偷康色图哟，好东西大家一起分享ヾ(≧ ▽ ≦)ゝ"

    rsp = ''
    with open(path.join(path.dirname(__file__), 'config.json')) as json_config:
        config = json.load(json_config)
    if canshu == '色图' or canshu == '图':
        today_now = str(datetime.date.today())
        # 判断一天的调用的次数
        if today_now == config['today']:
            config['today_times'] = config['today_times'] + 1
        else:
            config['today'] = today_now
            config['today_times'] = 0

        if config['today_times'] < config['limits']:
            long_urls = get_hpic_links(config)
            short_urls = generate_shout_links(long_urls)

            url = 'http://www.qianyucat.top/show_image/?'
            for short_url in short_urls:
                url = url + "imageID[]=" + short_url[14:] + "&"
            url = url[:-1]
            rspurl = [url]
            rspurl = generate_shout_links(rspurl)
            rsp = '涩图来啦ヾ(≧▽≦*)o\n\n' + rspurl[0]
        else:
            rsp = "少年，要有节制，今天的次数已经用完了つ﹏⊂。"

    elif canshu == '壁纸':
        rsp = "该功能还没有实现"

    # 把数据保存到config.json
    config['index'] = config['index'] + config['num']
    config = json.dumps(config)
    with open(path.join(path.dirname(__file__), 'config.json'), 'w') as json_config:
        json_config.write(config)

    return rsp


def generate_shout_links(long_urls):
    key = "5f1a4a13b1b63c55182a9be4@d2957d1cab4eb6679c456a1b8f7e2af6"
    url = "http://suo.im/api.htm"
    short_urls = []

    # 请求短网址
    for long_url in long_urls:
        querystring = {
            "url": long_url,
            "key": key
        }

        try:
            response = requests.request("GET", url, params=querystring)
        except Exception:
            print('请求出错')

        short_urls.append(response.text)

    return short_urls


def get_hpic_links(config):
    try:
        f = open(path.join(path.dirname(__file__), 'list.txt'), "r")
        picname = f.readlines()
    finally:
        if f:
            f.close()

    print(config)

    # 初始化变量
    base_url = "https://olaindex.qianyucat.top/v/pic/picture/"
    i = config['index']
    n = i + config['num']
    url = []

    # 获取完整URL
    while i < n:
        picname[i] = picname[i][:-1]
        url.append(base_url + picname[i])
        i = i + 1

    return url