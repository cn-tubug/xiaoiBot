from nonebot import on_command, CommandSession
import psutil, datetime

__plugin_name__ = '运行状态'

from nonebot.permission import SUPERUSER


@on_command('GoGoGoState', aliases=['运行状态', ''])
async def GoGoGoState(session: CommandSession):
    await session.send('当你看到此条消息时，说明小艾已经正常运行啦')


@on_command('GoGoGoState_admin', permission=SUPERUSER)
async def GoGoGoState_admin(session: CommandSession):
    await session.send(f'详细信息以发给[CQ:at,qq=3464330059]啦')
    await session.bot.send_private_msg(user_id=3464330059, message=get_state())


def get_state():
    cpu_times = psutil.cpu_times()
    mem = psutil.virtual_memory().free
    swap_mem = psutil.swap_memory()
    disk_usage = psutil.disk_usage('/')['free']
    data_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H: %M: %S")
    return f'{cpu_times}\n' \
           f'{mem}\n' \
           f'{swap_mem}\n' \
           f'{disk_usage}\n' \
           f'{data_time}'
