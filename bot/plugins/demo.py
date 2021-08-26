from nonebot import on_command, CommandSession


@on_command('demo', aliases='演示')
async def demo(session: CommandSession):
    msg = session.get('demo', prompt='请输入文字')
    r_msg = await get_msg(msg)
    await session.send('演示测试!!'+r_msg)


async def get_msg(msg: str) -> str:
    return msg
