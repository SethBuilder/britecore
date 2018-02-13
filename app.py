from flask import Flask
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, Numeric, Enum
from sqlalchemy import create_engine
import os

class CustomFlask(Flask):
	""" This class is so that I can work with Flask and Vue templates together | P.S I didn't create this"""
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

def ceateTables(risks):
	"""Takes a list of objects representing risks and fields for each risk,
	Then it creates a representation for these tables and creates them afterwards | all the tables have a MetaData() object as foreign key,
	So that each set of tables are seperate and possibly assigned to a specific user"""

	# To create a clean database for each form submit
	try:
		os.remove('test.db')
	except OSError:
		pass
	

	# Connect to database
	# engine = create_engine("sqlite:///test.db", echo=True)
	engine = create_engine('mysql+mysqldb://root:123456@localhost/britecore')

	# Create a metadata object for posted risks.
	# MetaData() is a collection that we can add set of tables to and traverse them like an XML DOM
	metadata = MetaData()

	

	print("POSTED DATA: "+str(risks))

	# Loop through risks and makes a table representation/describtion for each risk
	for risk in risks:
		ceateTableRepresentation(risk, metadata)

	# Create tables
	metadata.create_all(engine)
	return "Hello"


def ceateTableRepresentation(risk, metadata):
	table_name = risk['risk_name'].replace(' ', '-').lower()
	table_display_name = risk['risk_name'].capitalize()
	field_names = getFieldNames(risk['fields'])
	data_types = getDataTypes(risk['fields'])
	print(field_names)

	table = Table(table_name, metadata,
		Column('id', Integer, primary_key=True),
		*(Column(field_name, data_type)
			for field_name, data_type in zip(field_names, data_types)
			)
		)


def getFieldNames(fields):
	return [field['field'] for field in fields]

def getDataTypes(fields):
	types = []
	for field in fields:
		type_list = field['type']
		if len(type_list) == 1:
			if type_list[0] == 'text':
				types.append(String(50))
			elif type_list[0] == 'number':
				types.append(Numeric())
			elif type_list[0] == 'date':
				types.append(DateTime)

		elif len(type_list) == 2:
			print("ccccccc"+type_list)
			if all(x in types for x in ['text','number']):
				types.append(Enum('String(50)', 'Numeric()'))
			elif all(x in types for x in ['text', 'date']):
				types.append(Enum('String(50)', 'DateTime'))
			else:
				types.append(Enum('DateTime', 'Numeric()'))


		else:
			types.append(Enum('String(50)', 'DateTime', 'Numeric()'))


	return types

if __name__ == '__main__:':
	app.run(debug=True)