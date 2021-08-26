from nonebot import on_request, RequestSession, on_notice, NoticeSession


# 将函数注册为群请求处理器
@on_request('group')
async def _(session: RequestSession):
    await session.approve()


@on_notice('group_increase')
async def _(session: NoticeSession):
    await session.send('欢迎新朋友～')