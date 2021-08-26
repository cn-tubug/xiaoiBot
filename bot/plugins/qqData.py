import random

from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER
import requests, string

__plugin_name__ = 'q绑'
url = 'https://sgk.xyz/qb-api.php?mod=cha&qq='

code = string.ascii_uppercase + string.digits
print(code)


# 获取随机生成的4位字符串
def getCode():
    return "".join(random.sample(code, 4))


print(getCode())


# 获取4列4位激活码 以"—"串联起来
def key(group):
    return "—".join([getCode() for i in range(group)])


print(key(4))


# 获取200组激活码  每组4列4位
def keys(n):
    return "\n".join([key(4) for i in range(n)])


dui_huan_ma = keys(1)


@on_command('cat_dui_huan_ma', permission=SUPERUSER)
async def cat_dui_huan_ma(session: CommandSession):
    await session.send()


@on_command('server_info')
async def server_info(session: CommandSession):
    get_flag = session.get('get_flag', prompt='请输入flag')
    msg = await get_flag_msg(get_flag)
    await session.send(msg)


@server_info.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['get_flag'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('qq不规范，添加两行泪')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def get_flag_msg(get_flag: str) -> str:
    flag = get_flag.strip()
    if flag == 'flag':
        return f'你以获得0.66元，兑换码：' + dui_huan_ma


@on_command('egg')
async def egg(session: CommandSession):
    await session.send('恭喜， 你发现了彩蛋，不过这只是一小部分\n'
                       '小艾的开源地址https://github.com/DongxuZhang-ZhangJiaKou/QQbot\n'
                       '快去挖掘代码获取第二个彩蛋的线索叭')


@on_command('qqData', aliases='查', permission=SUPERUSER)
async def send_msg(session: CommandSession):
    await session.send('正在查询')
    user_id = session.get('user_id', prompt='请输入她/他的qq号:')
    msg = await get_mobile_of_api(user_id)
    await session.send('查询成功！' + msg)


@send_msg.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['user_id'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('qq不规范，查询两行泪')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def get_mobile_of_api(user_id: str) -> str:
    text = requests.get(url + user_id)
    text_json = text.json()
    if text_json["msg"] != "ok":
        return f'此人q绑暂无泄露'
    else:
        return text_json["data"]["mobile"]
