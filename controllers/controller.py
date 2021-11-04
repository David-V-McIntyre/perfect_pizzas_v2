from app import app
from models.orders import orders
from flask import render_template
from flask.templating import render_template

@app.route('/orders')
def index():
    return render_template('index.html', title='Perfect Pizzas', orders=orders)

@app.route('/orders/<index>')
def an_order(index):
    order_picked = orders[int(index)]
    
    return render_template('order.html', order=order_picked)

