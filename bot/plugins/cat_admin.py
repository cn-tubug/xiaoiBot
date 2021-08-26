from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER

from config import SUPERUSERS

import re


@on_command('remove_admin', aliases='删除管理员', permission=SUPERUSER)
async def remove_admin(session: CommandSession):
    user_id = session.get('get_user_id', prompt='请输入她/他的qq')
    msg = await remove_admin_msg(user_id)
    await session.send(msg)


@on_command('add_admin', aliases='添加管理员', permission=SUPERUSER)
async def add_admin(session: CommandSession):
    user_id = session.get('get_user_id', prompt='请输入她/他的qq：')
    msg = await add_admin_msg(user_id)
    await session.send(msg)


@on_command('cat_admin', aliases='查看管理员')
async def look_admin(session: CommandSession):
    await session.send('小艾的管理：'+str(SUPERUSERS))


@add_admin.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['get_user_id'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('qq不规范，添加两行泪')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def add_admin_msg(user_id: int) -> str:
    pattern = re.compile(r'\d+')  # 查找数字
    re_msg = pattern.findall(str(SUPERUSERS))

    print(re_msg)
    if re_msg[0] == str(user_id):
        return f'此人已经是小艾的管理员啦'
    else:
        SUPERUSERS.add(int(user_id))
        return f'已将'+str(user_id)+'添加到小艾的管理员'


@remove_admin.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['get_user_id'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('qq不规范，添加两行泪')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def remove_admin_msg(user_id: int) -> str:
    pattern = re.compile(r'\d+')  # 查找数字
    re_msg = pattern.findall(str(SUPERUSERS))

    print(re_msg)
    for i in re_msg:
        if str(user_id) == i:
            SUPERUSERS.remove(int(user_id))
            return f'成功删除'+str(user_id)
        else:
            return f'此人不是管理员哦'
