from flask import Flask, render_template, request, redirect

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login ():
    username = request.form['username']
    password = request.form['password']

    if username == 'king@' and password == '321':
        return redirect('/servicos')
    
    else:
        print('Usuário não encontrado')
        return "Usuário ou senha incorretas", 401