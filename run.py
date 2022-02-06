from app import app
import os, bottle
from bottle import TEMPLATE_PATH

if __name__ == '__main__':
    TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "app/views")))
    if os.environ.get('APP_LOCATION') == 'heroku':
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        app.run(host='localhost', port=8080, debug=False, reloader=True)