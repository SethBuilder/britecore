from flask import jsonify
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime, Numeric
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy import create_engine
import os
import ast
from sqlalchemy import MetaData

metadata = MetaData()

def ceateTables(risks):
	"""Takes a list of objects representing risks and their fields.
	Then it creates a representation for these tables and creates them afterwards.
	All the tables have a MetaData() object as foreign key,
	So that each set of tables are seperate and possibly assigned to a specific user"""

	# Connect to database
	# engine = create_engine("sqlite:///test.db", echo=True)
	engine = create_engine('mysql+mysqldb://root:123456@localhost/britecore')


	# Loop through risks and makes a table representation/describtion for each risk
	for risk in risks:
		ceateTableRepresentation(risk, metadata)

	# All table descriptions have 'metadata' as their foreign key. So, we simply create them all.
	metadata.create_all(engine)
	return "Success!"

def getTables():
	'''
		Takes metadata object and returns all tables' names, fields, data-types associated with the it.
	'''

	# Pulls all tables' data in alphabetic order
	tables = metadata.sorted_tables

	# We'll return this array
	all_tables_info=[]

	# Loop through all tables
	for table in tables:

		# To hold each table's risk fields
		table_fields=[]

		# Loop though columns (risk fields)
		for column in table.columns:
			
			# Get the data type of the risk field
			data_type = column.type
			if isinstance(data_type, ENUM):
				data_type=ast.literal_eval(str(data_type)[4:].replace('(', '[').replace(')', ']'))
			else:
				data_type = str(data_type)

			# Ignore the id column
			if column.name == 'id':
				pass
			else:
				# Push a 'dict' for each risk field
				table_fields.append({'column_name': column.name, 'data_type': data_type})

		# Push a 'dict' record for each table
		all_tables_info.append({'table_name':table.name, 'fields':table_fields})

	# Return 'Response' object with all the risks' data (from the DB) to the API
	return jsonify(all_tables_info)


def ceateTableRepresentation(risk, metadata):
	''' Takes a risk and returns a table describtion with metadata as foreign field'''
	table_name = risk['risk_name'].replace(' ', '-').lower()+"-table" # This is not used. 
	table_display_name = risk['risk_name'].title()# to be displayed to user in the next page of UX
	field_names = getFieldNames(risk['fields'])# Fetches all fields associated with the risk
	data_types = getDataTypes(risk['fields'])# Fetches all data-types associated with each field

	# Creates Table object. No need to return as metadata has saved the object.
	table = Table(table_display_name, metadata,
		Column('id', Integer, primary_key=True),
		*(Column(field_name, data_type)
			for field_name, data_type in zip(field_names, data_types)
			)
		)

def getFieldNames(fields):
	return [field['field'].title() for field in fields]


# 'text' => String(50)
# 'number' => Numeric()
# 'date' => DateTime
# 'other' => ENUM
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

# if __name__ == '__main__:':
# 	app.run(debug=True)