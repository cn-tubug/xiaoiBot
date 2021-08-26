from nonebot import on_command, CommandSession


@on_command('show_info', aliases='介绍作者')
async def show_info(session: CommandSession):
    await session.send('作者小名叫东旭（网名pacman/花姑娘）\n'
                       '作者性别男爱好女（敲代码）\n'
                       '作者15岁了（卑微初中生）\n'
                       '机器人售卖网址aihj.top\n'
                       '介绍的作者目前网址还没有做好\n'
                       '机器人主要功能：智能聊天！\n'
                       '疫情查询，每日英语，管理系统\n'
                       '查q绑，抓鸭子，终端模拟器\n'
                       '运行python，编译java，连接数据库\n'
                       'socket连接，其他的。。。你们用不上\n'
                       '[CQ:image,file={2A94A318-AD77-F1C4-9B92-6B049308FC7B}.jpg,'
                       'url=http://gchat.qpic.cn/gchatpic_new//--2A94A318AD77F1C49B926B049308FC7B/0]')
