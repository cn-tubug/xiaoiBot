import socket
from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER

__plugin_name__ = 'socket测试'


@on_command('socketTest', aliases='socket测试', permission=SUPERUSER)
async def get_version(session: CommandSession):
    await session.send('启动连接...')
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect('192.168.0.155')
    server.bind(('192.168.0.155', 8888))  # 绑定要监听的端口
    server.listen(5)  # 开始监听 表示可以使用五个链接排队
    conn, addr = server.accept()  # 等待链接,多个链接的时候就会出现问题,其实返回了两个值
    while True:
        try:
            data = conn.recv(1024)  # 接收数据
            await session.send(data.decode())  # 打印接收到的数据
            conn.send(data.upper())  # 然后再发送数据
        except ConnectionResetError as e:
            await session.send('关闭了正在占线的链接！')
            break
    conn.close()
