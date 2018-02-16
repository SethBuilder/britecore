from flask import Flask, jsonify, request, render_template
from app import ceateTables, getTables
import logging
from sqlalchemy import MetaData
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

class CustomFlask(Flask):
	metadata = MetaData()
	jinja_options = Flask.jinja_options.copy()
	jinja_options.update(dict(
	block_start_string='(%',
	block_end_string='%)',
	variable_start_string='((',
	variable_end_string='))',
	comment_start_string='(#',
	comment_end_string='#)',
	))

app = CustomFlask(__name__)


@app.route('/', methods=['get'])
def index(name=None):
	return render_template('index.html', name=name)

@app.route('/risks', methods=['POST'])
def postInsurancePolicySpecs():
	logging.info('This goes to log file: '+str(request.json))
	return(ceateTables(request.json, app.metadata))

@app.route('/risks', methods=['GET'])
def getData():
	logging.info('This goes to log file: '+str(request.json))
	# data = getTables(app.metadata)
	# return render_template('form.html', risks=data)
	return(getTables(app.metadata))

@app.route('/form', methods=['GET'])
def getInsurancePolicyForm():
	logging.info('This goes to log file: '+str(request.json))
	# data = getTables(app.metadata)
	return render_template('form.html')
	# return(getTables(app.metadata))

if __name__ == '__main__:':
	app.run(debug=True)