from nonebot import on_command, CommandSession
import requests
import json

url = 'http://api.tianapi.com/txapi/ensentence/index?key='
api_key = '750ff6d4dcac62de36a64e0d08927b7a'


@on_command('english_day', aliases='英语一句话')
async def english_day(session: CommandSession):
    get_msg = await r_english_day()
    await session.send(get_msg[0])
    await session.send(get_msg[1])


def get_english_day():
    text = requests.get(url+api_key).json()
    newslist = text['newslist'][0]
    return [newslist["en"], newslist["zh"]]


async def r_english_day():
    english_day_ = get_english_day()
    return english_day_
