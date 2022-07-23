from flask_app import app
from flask import render_template,redirect, request,session,flash
from flask_app.models.order import Order

@app.route('/')
def orders():
    session.clear()
    return render_template('orders.html',orders=Order.get_all())

@app.route('/order_new/')
def order_new():
    return render_template('order_new.html')

@app.route('/order_save/',methods=['POST'])
def order_save():
    if not Order.validate(request.form):
        session['customer_name'] = request.form['customer_name']
        session['cookie_type'] = request.form['cookie_type']
        session['number_of_boxes'] = request.form['number_of_boxes']
        return redirect('/order_new/')
    Order.save(request.form)
    session.clear()
    return redirect('/')

@app.route('/order_edit/<int:order_id>/')
def order_edit(order_id):
    return render_template('order_edit.html',order=Order.get_one({'order_id':order_id}))

@app.route('/order_update/',methods=['POST'])
def order_update():
    if not Order.validate(request.form):
        order_id=request.form['order_id']
        return redirect(f'/order_edit/{order_id}/')
    Order.update(request.form)
    return redirect('/')

