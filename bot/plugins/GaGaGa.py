from nonebot import on_command, CommandSession
import re
__plugin_name__ = '抓鸭子'


@on_command('GaGaGa', aliases=('抓鸭子', '鸭子'))
async def GaGaGa(session: CommandSession):
    num = session.get('抓鸭子', prompt='抓几只')
    GaGaGa_send = await get_GaGaGa(num)
    await session.send(GaGaGa_send)


@GaGaGa.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['抓鸭子'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('你要抓几只鸭子啊')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def get_GaGaGa(num: str) -> str:
    result1 = re.findall(r'\d+', num)
    GaGaGa_num = ['嘎', '嘎嘎', '嘎嘎嘎', '嘎嘎嘎嘎', '嘎嘎嘎嘎嘎', '嘎嘎嘎嘎嘎嘎', '嘎嘎嘎嘎嘎嘎嘎', '嘎嘎嘎嘎嘎嘎嘎嘎', '嘎嘎嘎嘎嘎嘎嘎嘎嘎', '嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎', '嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎嘎还在等？，没有了']
    if result1:
        for x in result1[0]:
            
            return f'' + str(GaGaGa_num[int(x)-1])
    else:
        return f'没抓住'
