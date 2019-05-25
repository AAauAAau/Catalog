from flask import render_template, url_for, flash, redirect, request
from Catalog import app, db
from Catalog.model import User, CategorieItem, Categorie


@app.route("/")
@app.route("/home")
def home():
    categories = Categorie.query.order_by(Categorie.name).all()
    categorieitems = CategorieItem.query.order_by(CategorieItem.created_at).all()
    return render_template('home.html',title='Latest Post', categories=categories, categorieitems=categorieitems)


@app.route("/categorieitem", methods=['GET', 'POST'])
def about():
    return render_template('home.html', title='About')

# @app.route("/login", methods=['GET', 'POST'])
# def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(email=form.email.data).first()
    #     if user and bcrypt.check_password_hash(user.password, form.password.data):
    #         login_user(user, remember=form.remember.data)
    #         next_page = request.args.get('next')
    #         return redirect(next_page) if next_page else redirect(url_for('home'))
    #     else:
    #         flash('Login Unsuccessful. Please check email and password', 'danger')
    # return render_template('login.html', title='Login', form=form)


# @app.route("/logout")
# def logout():
#     logout_user()
#     return redirect(url_for('home'))


# @app.route("/account")
# @login_required
# def account():
#     return render_template('account.html', title='Account')
