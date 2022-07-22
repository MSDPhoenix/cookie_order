from flask_app import app
from flask import render_template,redirect, request,session,flash
from flask_app.models.order import Order

@app.route('/')
def index():
    return render_template('orders.html',orders=Order.get_all())