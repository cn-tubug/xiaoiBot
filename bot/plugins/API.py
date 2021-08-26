from nonebot import on_command, CommandSession
import requests

__plugin_name__ = 'api测试'

url = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'


@on_command('nmsl')
async def nmsl(session: CommandSession):
    for i in range(10):
        await session.send('[CQ:at,qq:2254662339]'+str(requests.get(url).text))


@on_command('get_', aliases='主人qq')
async def get_version(session: CommandSession):
    a = await session.bot.get_stranger_info(user_id=3464330059)
    await session.send(str(a['user_id']))
    await session.send(str(a['nickname']))
