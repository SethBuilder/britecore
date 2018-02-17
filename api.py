from flask import jsonify, request, render_template
from app import ceateTables, getTables
import logging
from custom_flask import CustomFlask

logging.basicConfig(filename='flask_logs.log', filemode='w', level=logging.DEBUG)

app = CustomFlask(__name__)

# Index page route
@app.route('/', methods=['get'])
def index(name=None):
	return render_template('index.html', name=name)


# Post risks specs route
@app.route('/risks', methods=['POST'])
def postInsurancePolicySpecs():
	logging.info('This goes to log file: '+str(request.json)) # Log incoming request
	return(ceateTables(request.json))


# Get risks' tables details from DB
@app.route('/risks', methods=['GET'])
def getData():
	tablesData = getTables()
	logging.info('This goes to log file: '+str(tablesData)) # Log data coming from DB
	return(tablesData)

# Get form page (second page in UX)
@app.route('/form', methods=['GET'])
def getInsurancePolicyForm():
	return render_template('form.html')

# if __name__ == '__main__:':
# 	app.run(debug=True)