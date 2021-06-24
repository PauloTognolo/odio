from flask import Flask, render_template, Blueprint, url_for, flash, redirect
from flask_login.utils import login_required
from flask_chance import app, db, bcrypt
from flask_chance.forms import RegistrationForm, LoginForm, BuyForm
from flask_chance.models import User, Order
from flask_login import login_user, current_user, logout_user


web = Blueprint('web', __name__, url_prefix='',
                template_folder='templates', static_folder='static')


@web.route("/index.html")
@web.route("/home")
def home():
    return render_template('index.html')


@web.route("/about.html")
def about():
    return render_template('about.html')


@web.route('/reservation.html')
def reservation():
    return render_template('reservation.html')


@web.route('/login_client', methods=['GET', 'POST'])
def client():
    if current_user.is_authenticated:
        return redirect(url_for('web.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            #next_page = request.args.get('next')
            # return redirect(next_page) if next_page else redirect(url_for('home'))
            return redirect(url_for('web.order'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@web.route('/order', methods=['GET', 'POST'])
@login_required
def order():
    form = BuyForm()
    if form.validate_on_submit():
        order = Order(date_posted=form.qdata.data, price=form.price.data,
                      quant_cafe=form.quant_cafe.data, client=current_user, type_cafe=form.id_cafe.data)
        db.session.add(order)
        db.session.commit()
        flash('Your order has been sent!', 'sucess')
        return redirect(url_for('web.home'))
    return render_template('order.html', title='Order', form=form)


@web.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('web.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data,
                    cpf=form.cpf.data, phone=form.phone.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'sucess')
        return redirect(url_for('web.client'))
    return render_template('registration.html', title='Register', form=form)


@web.route("/profile")
def profile():
    orders = Order.query.filter_by(client=current_user) 
    return render_template('profile.html', orders=orders)


@web.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('web.home'))


@web.route("/menu.html")
@web.route("/menu")
def menu():
    return render_template('menu.html')


@web.route("/contact.html")
def contact():
    return render_template('contact.html')


app.register_blueprint(web)
