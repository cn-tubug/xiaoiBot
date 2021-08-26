from nonebot import on_command, CommandSession
import os
import re

__plugin_name__ = '运行Python'


@on_command('compile_python', aliases='运行Python')
async def code(session: CommandSession):
    code_ = session.get('code', prompt='请输入python代码')
    code_run = await get_python_run(code_)
    await session.send(code_run)
    await session.send(
        '[pic,hash=551A12CABC2F10C3D91890B4A8E652ED,wide=2900,high=1555,cartoon=false]' + '\n本程序由pacman开发如有问题请联系：3464330059')


@code.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['code'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要输入的代码不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg


async def get_python_run(code_: str) -> str:
    while_ = re.findall('while', code_)
    for_ = re.findall('for', code_)
    os.system('touch a.py')
    os.system('echo ' + "'" + code_ + "'" + " >> a.py")
    f = os.popen('python3 a.py')
    f_d = f.read()
    f.close()
    os.system('rm -rf a.py')
    if while_:
        return f'给爷爬'
    elif for_:
       return f'👴的电脑撑不住'
    else:
        if f_d == '':
            return f'编译失败，请检查代码完整性'
        else:
            return f'编译成功!!!\n' + '运行结果：\n' + f_d
