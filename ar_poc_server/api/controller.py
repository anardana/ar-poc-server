'''Controllers used by AR PoC Server'''
from flask import Flask, request
from ar_poc_server.api import routes


APP = Flask(__name__)


@APP.route("/")
def hello():
    '''Hello Controller'''
    return "Hello World"


@APP.route(routes.AR_OBJECT_DETECTION_V1, methods=['POST'])
def ar_object_detection():
    '''This controller accepts POST request with type multipart/form-data.
    Image file comes as form input field named "file"'''
    files = request.files['file']
    APP.logger.error(files.read())
    return "OK"

if __name__ == "__main__":
    APP.run()
