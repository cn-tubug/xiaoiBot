import urllib

from nonebot import CommandSession, on_command
import requests


@on_command('douyin', aliases='去水印')
async def douyin(session: CommandSession):
    url = session.get('url', prompt='请输入视频地址')
    msg = await dwz(url)
    await session.send('视频封面:'+msg[0])
    await session.send('去水印视频:'+msg[1])


@douyin.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['url'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def dwz(url: str) -> list:
    dwz_ = 'http://api.k780.com/?app=shorturl.set&appkey=10003&sign=b59bc3ef6191eb9f747dd4e83c99f2a4&format=json&url='
    qu_sui_yin = 'http://admin.feeprint.com/dsp?key=490F5F7529OETZ45FD3353&token=021341OD55044MQOETZ&url='
    qu_sui_yin_img = requests.get(qu_sui_yin + urllib.parse.quote(url)).json()['data']['img']
    qu_sui_yin_url = requests.get(qu_sui_yin + urllib.parse.quote(url)).json()['data']['url']
    dwz_img = requests.get(dwz_+qu_sui_yin_img).json()['result']['short_url']
    dwz_url = requests.get(dwz_ + qu_sui_yin_url).json()['result']['short_url']
    print("['"+dwz_img+", '"+dwz_url+"']")
    return [dwz_img, dwz_url]
