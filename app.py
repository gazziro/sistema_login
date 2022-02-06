from cgitb import html
from bottle import route, run, request, template, TEMPLATE_PATH, static_file, get, error
import os
from model import insert_user

TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "views")))


#static routes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root='static/fonts')

@route('/cadastro')
def cadastro():
    return template('cadastro')

@route('/cadastro', method="POST")
def acao_cadastro():
    username = request.forms.get('username')
    password = request.forms.get('password')
    insert_user(username, password)
    return template('verificacao_cadastro', nome=username)

@route('/')  #@get('/')
def Login():
    return template('Login')

def check_login(username, password):
    d = {'gabriel':'python', 'giovani':'java', 'alberto':'javascript'}
    if username in d.keys() and d[username] == password:
        return True
    return False


@route("/", method="POST")
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return template('verificacao_login', sucesso=check_login(username, password), nome = username)

@error(404)
def error404(error):
    return template('pagina404')

if __name__ =='__main__':
    if os.environ.get("APP_LOCATION") == "heroku":
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:    
        run(host='localhost', port=8080, debug=False)