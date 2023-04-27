import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, request

app = Flask(__name__)

# Set up logging
handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


@app.route('/')
def index():
    app.logger.info('Index route accessed')
    app.logger.info(f'Remote IP address: {request.remote_addr}')
    app.logger.info(f'User agent: {request.headers.get("User-Agent")}')
    return 'Hello, world!'


@app.route('/about')
def about():
    app.logger.info('About route accessed')
    return 'About us'


if __name__ == '__main__':
    app.run(debug=True)
