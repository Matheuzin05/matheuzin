from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/nuuv')
def nuuv():
    return render_template('nuuv.html')

@app.route('/servico')
def servico():
    return render_template('servico.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Lógica para processar o cadastro
        pass
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)