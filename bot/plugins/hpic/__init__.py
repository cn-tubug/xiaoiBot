from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg

from .data_source import get_hpic_website

__plugin_name__ = '一份色图'
__plugin_usage__ = r"""色图机器人使用方法
@机器人 来一份色图/涩图
@机器人 一份色图 /色图一份
（只要包含一份和色图即可）
1.1.3 更换了短网址服务器，出问题的可能性应该会变小
1.1.2 修复了私发色图的bug(特性)
1.1.1 稍微优化了点图片查看的排版，增加了命令'来份色图','我要色图'
"""


# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('setu', aliases=('来一份', '一份'))
async def hpic(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    canshu = session.get('canshu', prompt='兄弟，你想要什么？')
    # 获取城市的天气预报
    sub_type = session.event.sub_type
    hpic_website = await get_hpic_website(canshu, sub_type)
    # 向用户发送天气预报
    await session.send(hpic_website)


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@hpic.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['canshu'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('姐妹，你想要什么？')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'一份', '来份', '我要'})
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.strip()
    # 对消息进行分词和词性标注
    words = posseg.lcut(stripped_msg)

    canshu = None
    # 遍历 posseg.lcut 返回的列表
    for word in words:
        # 每个元素是一个 pair 对象，包含 word 和 flag 两个属性，分别表示词和词性
        if word.flag == 'n':
            # ns 词性表示地名
            if word.word == '色图' or word.word == '壁纸' or word.word == '图':
                canshu = word.word
                break

    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'setu', current_arg=canshu or '')
