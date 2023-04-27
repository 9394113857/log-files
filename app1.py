from flask import Flask, request
import logging
from logging.handlers import TimedRotatingFileHandler
import os

app = Flask(__name__)

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.mkdir('logs')

# Configure logging
handler = TimedRotatingFileHandler(filename='logs/app.log', when='midnight', backupCount=7)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))
logging.getLogger().addHandler(handler)


# Custom middleware to log requests
@app.before_request
def log_request():
    logging.info(f'Request {request.method} {request.url}')


# Define routes
@app.route('/')
def index():
    return 'Hello, world!'


@app.route('/about')
def about():
    return 'About us'


if __name__ == '__main__':
    app.run(debug=True)

# In this modified example, we create a directory called logs if it doesn't already exist.
# We then create a TimedRotatingFileHandler object that writes log messages to a file named app.log
# in the logs directory.
#
# The when parameter is set to 'midnight', which means a new log file will be created at midnight each day.
# The backupCount parameter is set to 7, which means that up to 7 old log files will be kept before they are deleted.
#
# We also set the log level to INFO and specify a logging format.
# Finally, we define the same custom middleware function as before to log requests.
#
# When you run this Flask app, it will create a new log file for each day in the logs directory
# with a filename like app.log.YYYY-MM-DD.
# For example, on March 12th, 2023, the log file would be named app.log.2023-03-12.
# This allows you to keep track of each day's log messages separately,
# which can be useful for long-term monitoring and analysis.
