from nonebot import on_command, CommandSession
import requests
import json

__plugin_name__ = '新冠查询'

apikey = '750ff6d4dcac62de36a64e0d08927b7a'
url = 'http://api.tianapi.com/txapi/ncov/index?key='


@on_command('nCoV', aliases='疫情')
async def nCoV(session: CommandSession):
    nCoV_info = await get_nCoV_info()
    await session.send(nCoV_info[0])
    await session.send(nCoV_info[1])


def get_nCoV_news():
    r_s = requests.get(url + apikey).json()
    r = r_s["newslist"][0]
    return [r["news"][0]["title"], r["news"][0]["summary"]]


async def get_nCoV_info():
    nCoV_news = get_nCoV_news()
    return nCoV_news
