from flask import Flask, blueprints, render_template, request, redirect

main_tp = blueprints('main', __name__)

@main_tp.route('/')
def index():
    return render_template('index.html')

@main_tp.route('/login')
def login():
    return render_template('login.html')

@main_tp.route('/')
def teste():
    return render_template('teste.html')

