from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer,Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#基础类
Base = declarative_base()

#此处没有使用pymysql的驱动
#请安装pip install mysql-connector-python
#engine中的 mysqlconnector 为 mysql官网驱动
engine = create_engine(
	'mysql+mysqlconnector://root:root@127.0.0.1:3306/test?charset=utf8',#连接本地
	echo = True
)

class Book(Base):
	__tablename__ = 'book'
	id = Column('id',Integer(),primary_key = True,autoincrement = True)
	title = Column('title',String(20))
	info = Column('info',String(30))
	star = Column('star',String(10))
	pl = Column('pl',String(10))
	introduce = Column('introduce',Text())


session = sessionmaker(engine)
sess=session()