from flask import Flask, jsonify

from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, Numeric
from sqlalchemy.dialects.mysql import ENUM
# from enum import Enum
# from sqlalchemy.types import Enum
from sqlalchemy import create_engine
import os
import ast

class CustomFlask(Flask):
	""" This class is so that I can work with Flask and Vue templates together"""
	
	jinja_options = Flask.jinja_options.copy()
	jinja_options.update(dict(
	block_start_string='(%',
	block_end_string='%)',
	variable_start_string='((',
	variable_end_string='))',
	comment_start_string='(#',
	comment_end_string='#)',
	))






# Create Flask app
app = CustomFlask(__name__)

def ceateTables(risks, metadata):
	"""Takes a list of objects representing risks and fields for each risk,
	Then it creates a representation for these tables and creates them afterwards | all the tables have a MetaData() object as foreign key,
	So that each set of tables are seperate and possibly assigned to a specific user"""

	# Connect to database
	# engine = create_engine("sqlite:///test.db", echo=True)
	engine = create_engine('mysql+mysqldb://root:123456@localhost/britecore')

	print("POSTED DATA: "+str(risks))

	# Loop through risks and makes a table representation/describtion for each risk
	for risk in risks:
		ceateTableRepresentation(risk, metadata)

	# Create tables
	metadata.create_all(engine)
	return "Hello"

def getTables(metadata):
	print("BEHOLD TABLE NAMES: "+str(metadata.sorted_tables))
	# [
	#{'table_name': 'Jim's car', 'fields': [{'field': 'Price', 'type': 'String'}]}
	#]
	tables = metadata.sorted_tables
	table_names = [table.name for table in tables]
	field_types = []
	for table in tables:
		field_names = [column.name for column in table.columns]
		field_types_initial = [column.type for column in table.columns]
		for field_type in field_types_initial:
			if isinstance(field_type, ENUM):
				field_type = ast.literal_eval(str(field_type)[4:].replace('(', '[').replace(')', ']'))
				
				field_types.append(field_type)
			else:
				field_types.append(field_type)
		
	# fields = [(field_name, data_type) for field_name, data_type in zip(field_names, field_types) ]
	print("XXX"+str(field_types))
	# fields = [{k:v for k,v in fields}]
	
	print(str(table_names))

	tables_and_their_fields = []

	return 'Hi'

def getFieldNamesFromDB(metadata):
	pass


def ceateTableRepresentation(risk, metadata):
	table_name = risk['risk_name'].replace(' ', '-').lower()+"-table"
	table_display_name = risk['risk_name'].capitalize()
	field_names = getFieldNames(risk['fields'])
	data_types = getDataTypes(risk['fields'])

	table = Table(table_name, metadata,
		Column('id', Integer, primary_key=True),
		*(Column(field_name, data_type)
			for field_name, data_type in zip(field_names, data_types)
			)
		)


def getFieldNames(fields):
	return [field['field'] for field in fields]

def getDataTypes(fields):
	data_types = []
	for field in fields:
		types_list = field['type']
		print("FIELD types: " + str(types_list))
		if isinstance(types_list, str):
			if types_list == 'text':
				data_types.append(String(50))
			elif types_list == 'number':
				data_types.append(Numeric())
			elif types_list == 'date':
				data_types.append(DateTime)
			else:
				data_types.append(ENUM(types_list[0]))

		else:
			data_types.append(ENUM(*(types_list)))
	return data_types

if __name__ == '__main__:':
	app.run(debug=True)