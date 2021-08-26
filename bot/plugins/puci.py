from nonebot import on_command, CommandSession

__plugin_name__ = '噗呲噗呲'


@on_command('puci', aliases='噗呲噗呲')
async def get_version(session: CommandSession):
    await session.send('噗呲噗呲')
    await session.send('切克切克')
    await session.send('木啊木啊')
    await session.send('啊~')
