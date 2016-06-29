# connect ticketsystem

import mysql.connector
from sqlalchemy import Column, Integer, String,  create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TS(Base):
	__tablename__ = 'TicketStatus'
	TicketStatus_ID = Column(Integer, primary_key=True)
	name = Column(String(25))
	isSoftDeleted = Column(Integer)
	createTimeStamp = Column(String(26))
	lastUpdateTimeStamp = Column(String(26))

engine = create_engine('mysql+mysqlconnector://USR:PWD@9.9.153:3306/dstticket')
DBSession = sessionmaker(bind=engine)

session = DBSession()

ts= session.query(TS).filter(TS.TicketStatus_ID==1).one()

print('type:', type(ts))
print(ts)
print('name:', ts.name)

session.close();



'''
conn = mysql.connector.connect(host = '9.9.153', user= '', password = '', database= 'dstticket')

cursor = conn.cursor()
mysql = 'select * from TicketStatus '
cursor.execute(mysql)
print(cursor.rowcount)

values = cursor.fetchall()
print(values)
cursor.close()

conn.close() 
'''

