'''Server entry point for WSGI application (gunicorn)'''
from ar_poc_server.api.controller import APP as application


if __name__ == "__main__":
    application.run()
