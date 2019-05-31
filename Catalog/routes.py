from flask import render_template, url_for, flash, redirect, request, jsonify, abort, g, make_response
from Catalog import app, db
from Catalog.models import User, CategorieItem, Categorie
from Catalog.forms import ItemForm
from google.oauth2 import id_token
from google.auth.transport import requests as googleRequests
from flask_login import login_user, current_user, logout_user, login_required
import httplib2
import requests
import json

CLIENT_ID = json.loads(open('Catalog/client_secrets.json', 'r').read())['web']['client_id']
categories = Categorie.query.order_by(Categorie.name).all()

@app.route("/")
@app.route("/home")
def home():
    categorieitems = CategorieItem.query.order_by(CategorieItem.created_at.desc()).all()
    return render_template('home.html', title='Latest Post', categories=categories, categorieitems=categorieitems)

@app.route("/myItems")
@login_required
def myItems():
    categorieitems = CategorieItem.query.filter_by(user_id=current_user.id).order_by(CategorieItem.created_at.desc()).all()
    return render_template('home.html', title='My Items', categories=categories, categorieitems=categorieitems)

@app.route("/item/<int:item_id>/delete", methods=['POST'])
@login_required
def delete_item(item_id):
    item = CategorieItem.query.get_or_404(item_id)
    if item.author != current_user:
        abort(403)
    db.session.delete(item)
    db.session.commit()
    flash('Your iIem has been deleted!', 'success')
    return redirect(url_for('home'))

@app.route('/api/resource')
@login_required
def get_resource():
    return jsonify({ 'data': 'Hello, %s!' % g.user.name })

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/item/new", methods=['GET', 'POST'])
@login_required
def newItem():
    form = ItemForm()
    if form.validate_on_submit():
        item = CategorieItem(name=form.name.data, description=form.description.data, author=current_user, price=str(form.price.data), categorie=Categorie.query.get_or_404(form.categorie.data))
        db.session.add(item)
        db.session.commit()
        flash('Your Item has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('new_item.html', title='New Item',
                           form=form, legend='New Item')
@app.route("/item/<int:item_id>")
@login_required
def item(item_id):
    item = CategorieItem.query.get_or_404(item_id)
    return render_template('item.html', title=item.name, item=item)


@app.route("/item/<int:item_id>/update", methods=['GET', 'POST'])
@login_required
def update_item(item_id):
    item = CategorieItem.query.get_or_404(item_id)
    if item.author != current_user:
        abort(403)
    form = ItemForm()
    if form.validate_on_submit():
        item.name = form.name.data
        item.description = form.description.data
        db.session.commit()
        flash('Your Item has been updated!', 'success')
        return redirect(url_for('item', item_id=item.id))
    elif request.method == 'GET':
        form.name.data = item.name
        form.description.data = item.description
    return render_template('new_item.html', title='Update Item',
                           form=form, legend='Update Item')
@app.route('/api/users/<int:id>')
@login_required
def get_user(id):
    user = User.query.filter_by(id=id).one()
    if not user:
        abort(400)
    return jsonify({'username': user.name})

@app.route('/signin/<provider>', methods = ['POST'])
def signin(provider):
    if provider == 'google':
        # (Receive token by HTTPS POST)
        token =request.form.get('idtoken')
        try:
            # Specify the CLIENT_ID of the app that accesses the backend:
            idinfo = id_token.verify_oauth2_token(token, googleRequests.Request(), CLIENT_ID)

            # Or, if multiple clients access the backend server:
            # idinfo = id_token.verify_oauth2_token(token, requests.Request())
            # if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
            #     raise ValueError('Could not verify audience.')
        
            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')

            # If auth request is from a G Suite domain:
            # if idinfo['hd'] != GSUITE_DOMAIN_NAME:
            #     raise ValueError('Wrong hosted domain.')

            # ID token is valid. Get the user's Google Account ID from the decoded token.
            userid = idinfo['sub']
            email = idinfo['email']
            picture = idinfo['picture']
            name = idinfo['name']
                  #see if user exists, if it doesn't make a new one
            user = User.query.filter_by(email=email).first()
            if not user:
                user = User(name = name, picture = picture, email = email)
                db.session.add(user)
                db.session.commit()
                flash('Your account has been created! You are now able to log in', 'success')    

            login_user(user, True)
            next_page = request.args.get('next')
           # flash('Login Successfull. Please check email and password', 'info')  
            # return redirect(next_page) if next_page else redirect(url_for('home'))    
            return name
        except ValueError:
            # Invalid token
            pass

