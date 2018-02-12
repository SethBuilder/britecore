from flask import Flask, jsonify, request, render_template
from app import ceateTables
import logging
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

class CustomFlask(Flask):
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
	return(ceateTables(request.json))

if __name__ == '__main__:':
	app.run(debug=True)