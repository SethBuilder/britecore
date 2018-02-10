from flask import Flask
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, Numeric, Enum
from sqlalchemy import create_engine

app = Flask(__name__)

def addRisks(posted_data):
	return "POSTED DATA: ".posted_data

# MetaData() is a collection that we can add tables to and traverse them like XML DOM
# metadata = MetaData()

# test_table = Table('test', metadata,
# 	Column('id', Integer, primary_key=True),
# 	Column('name', String(50))
# 	)

# engine = create_engine("sqlite:///test.db", echo=True)

# metadata.create_all(engine)

# if __name__ == '__main__:':
# 	app.run(debug=True)