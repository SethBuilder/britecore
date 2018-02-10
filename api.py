from flask import Flask, jsonify, request, render_template
from app import app
app = Flask(__name__,static_url_path='')
import logging
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

@app.route('/', methods=['get'])
def index(name=None):
	return render_template('index.html', name=name)

@app.route('/risks', methods=['POST'])
def addRisks():
	app.addRisks(request.data)
	logging.info('So should this: '.x)

if __name__ == '__main__:':
	app.run(debug=True)