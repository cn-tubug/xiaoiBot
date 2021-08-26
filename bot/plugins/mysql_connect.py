import pymysql
from nonebot import on_command, CommandSession
from nonebot.permission import SUPERUSER

# 打开数据库连接
db = pymysql.connect(passwd='dxz070730', user='root', host='localhost', db='CHFMN')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()


@on_command('mysql_version', aliases='mysql -v', permission=SUPERUSER)
async def connect_mysql(session: CommandSession):
    await session.send("Database version : %s " % data)
    db.close()

