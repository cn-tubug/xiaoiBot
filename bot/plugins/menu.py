from nonebot import on_command, CommandSession

__plugin_name__ = '获取陌生人信息'

@on_command('get_stranger_info', aliases='获取陌生人信息')
async def menu(session: CommandSession):
    user_id = await session.get('userid')