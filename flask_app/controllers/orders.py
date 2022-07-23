from flask_app import app
from flask import render_template,redirect, request,session,flash
from flask_app.models.order import Order

@app.route('/')
def orders():
    return render_template('orders.html',orders=Order.get_all())

@app.route('/order_new/')
def order_new():
    return render_template('order_new.html')

@app.route('/order_save/')
def order_save():
    return redirect('/')

@app.route('/order_edit/<int:order_id>/')
def order_edit(order_id):
    return render_template('order_edit.html')

@app.route('/order_update/<int:order_id>/')
def order_update(order_id):
    return redirect('/')

