from nonebot import on_natural_language, NLPSession, IntentCommand, on_command, CommandSession


@on_natural_language(keywords={'天气'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(60.0, 'weather')


@on_command('weather', aliases='天气')
async def weather(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    city = session.get('city', prompt='你的城市是')

    weather_report = await get_weather(city)
    # 向用户发送天气预报
    await session.send(weather_report)


async def get_weather(city: str) -> str:
    # 这里简单返回一个字符串
    return city + "的天气不错"