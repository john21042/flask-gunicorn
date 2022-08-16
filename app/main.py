
from flask import Flask
from datetime import datetime
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
 
@app.route('/')
@app.route('/index')
def index():
    app.logger.info('/ called')
    date_str =  datetime.now().strftime('%Y-%m-%d %I:%M:%S %p %Z')
    # return 'Hello world! ' + datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p %Z')
    return 'Hello world! ' + date_str