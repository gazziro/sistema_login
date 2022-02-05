from cgitb import html
from bottle import route, run, request, template, TEMPLATE_PATH, static_file, get, error
import os
 
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


@route('/Login')  #@get('/login')
def Login():
    return template('Login')

def check_login(username, password):
    d = {'gabriel':'python', 'giovani':'java', 'alberto':'javascript'}
    if username in d.keys() and d[username] == password:
        return True
    return False

@route("/Login", method="POST")
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return template('verificacao_login', sucesso=check_login(username, password), nome = username)

@error(404)
def error404(error):
    return template('pagina404')

if __name__ =='__main__':
    run(host='localhost', port=8080, debug=False)