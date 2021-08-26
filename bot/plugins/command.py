from nonebot import on_command, CommandSession
import requests
import os
import re

__plugin_name__ = '命令行'
__plugin_usage__ = r"""
天气查询

天气  [城市名称]
"""
from nonebot.permission import SUPERUSER

from config import SUPERUSERS


@on_command('command', aliases=('命令', '命令行'))
async def weather(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    command_t = session.get('command', prompt='请输入命令')
    # 获取城市的天气预报
    weather_report = await get_weather_of_city(command_t)
    # 向用户发送天气预报
    await session.send(weather_report)


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@weather.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['command'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要输入的命令不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def get_weather_of_city(command_t: str) -> str:
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API，并拼接成天气预报内容
    a = re.findall('rm', command_t)
    ping = re.findall('ping', command_t)
    shutdown = re.findall('shutdown', command_t)
    curl = re.findall('curl', command_t)
    wget = re.findall('wget', command_t)
    passwd = re.findall('passwd', command_t)
    ython = re.findall('ython', command_t)
    if a:
        print(a[0])
        return f'你想干什么'
    elif ping:
        return f'[CQ:at,qq=3464330059]太笨了不会写ping'
    elif shutdown:
        return f'未找到命令'+command_t
    elif curl:
        return f'想访问什么？'
    elif wget:
        return f'想下载什么？'
    elif passwd:
        return f'滚，你知道我旧密码？'
    elif ython:
        return f'你可以试试"小艾运行Python"'
    else:
        f = os.popen(command_t, "r")
        d = f.read()
        with open('command','w') as x:
            x.write(d)  # 读文件
        x_1 = open('command','r')
        x_2 = open('command.txt','w')
        lines = x_1.readlines()
        for line in lines:
            if line.split():
                x_o = lines[len(lines)-1].replace('\n', '').replace('\r', '')
                if lines[-1] == '\n':
                    line = lines[len(lines)-1].replace('\n', '').replace('\r', '')
                x_2.writelines(x_o)
            else:
                x_2.writelines("")
        print()
        f.close()
        x.close()
        x_1.close()
        x_2.close()
        x_read = open('command.txt','r')
        d_1 = x_read.read()
        if str(d) == '':
            return f'未找到命令/没权限运行此命令'+command_t
        return f'运行结果:\n' + str(d_1)
