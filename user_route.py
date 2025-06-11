from flask import Flask, blueprints, render_template, request, redirect

user_tp = blueprints('main', __name__)

@user_tp.route('/login')
def login():
    return render_template('login.html')

@user_tp.route('/registro')
def registro():
    return render_template('registro.html')