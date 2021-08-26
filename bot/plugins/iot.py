from nonebot import on_command, CommandSession
import os

__plugin_name__ = '智能家具'


@on_command('iot', aliases='开灯')
async def get_version(session: CommandSession):
    os.system('curl http://192.168.0.109:8899/cmd?led=on')
    await session.send('已经打开了主人～ 工作累了记得找我聊天哦～')

@on_command('iot', aliases='关灯')
async def get_version(session: CommandSession):
    os.system('curl http://192.168.0.109:8899/cmd?led=on')
    await session.send('呜哇～ 关灯睡觉，祝主人晚安喽 拜拜～')