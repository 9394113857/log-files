from flask import Flask, request
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')


@app.before_request
def log_request():
    logging.info(f'Request {request.method} {request.url}')


# Define routes
@app.route('/')
def index():
    logging.info('--------------------')
    logging.info('Index route accessed')
    logging.info(f'Request Method Used: {request.method} and URL Used: {request.url}')
    logging.info(f'Remote IP address: {request.remote_addr}')
    logging.info(f'User agent: {request.headers.get("User-Agent")}')
    return 'Hello, world!'


@app.route('/about')
def about():
    logging.info('--------------------')
    logging.info('About route accessed')
    logging.info(f'Request Method Used: {request.method} and URL Used: {request.url}')
    logging.info(f'Remote IP address: {request.remote_addr}')
    logging.info(f'User agent: {request.headers.get("User-Agent")}')
    return 'About us'


if __name__ == '__main__':
    app.run(debug=True)
