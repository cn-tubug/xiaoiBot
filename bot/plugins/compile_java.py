from nonebot import on_command, CommandSession
import os
import time

__plugin_name__ = '编译Java'


@on_command('compile_java', aliases='编译Java')
async def code(session: CommandSession):
    code_ = session.get('code', prompt='请输入Java代码')
    code_run = await get_java_run(code_)
    await session.send(code_run)
    await session.send('&#91;吃番茄&#93;'+'\n本程序又pacman开发如有问题请联系：3464330059')


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


async def get_java_run(code_: str) -> str:
    os.system('touch HelloWorld.java')
    os.system('echo '+"'"+code_+"'"+' >> '+'HelloWorld.java')
    f = os.popen('javac HelloWorld.java', 'r')
    time.sleep(3)
    f_1 = os.popen('java HelloWorld', 'r')
    f_d = f.read()
    f_1_d = f_1.read()
    print(f_d)
    print(f_1_d)
    f.close()
    f_1.close()
    os.system('rm -rf HelloWorld.java HelloWorld.class')
    if str(f_d) == '':
        return f'编译成功' + '\n' + '运行结果：' + '\n' + f_1_d
    else:
        return f'编译失败,请检查代码完整性'