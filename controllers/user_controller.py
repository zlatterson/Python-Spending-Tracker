from datetime import datetime
from flask import Flask, render_template,request,redirect
from models.user import User
from models.transaction import *
from flask import Blueprint

import repositories.user_repository as user_repository
import repositories.transaction_repository as transaction_repository

users_blueprint = Blueprint("user", __name__)

# @users_blueprint.route("/users")
# def user():
#     users = user_repository.select_all() 
#     return render_template("/index.html", users=users)

# SHOW
@users_blueprint.route("/users/<id>")
def show_users(id):
    user = user_repository.select(id)
    transacitons = transaction_repository.select_all()
    print(transacitons)
    user_transacts = Transaction.sort_by_user(transacitons,user.id)
    print("New:")
    print(user_transacts)
    # sort by transacitons:working
    dt_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_sorted = Transaction.sort_by_time(user_transacts,dt_string)
    print("date sorted:")
    print(date_sorted)
    return render_template("/users/show.html", user=user, user_transacts=date_sorted)

 

# NEW
@users_blueprint.route("/users/new")
def new_user():
    users = user_repository.select_all()
    return render_template("users/new.html", users=users)

# CREATE
@users_blueprint.route("/users",methods=["POST"])
def create_user():
    name = request.form["name"]
    balance = request.form["balance"]
    budget = request.form["budget"]
    account = User(name,balance,budget)
    user_repository.save(account)
    return redirect("/users")

# EDIT
@users_blueprint.route("/users/<id>/edit")
def edit_user(id):
    user = user_repository.select(id)
    return render_template("/users/edit.html", user=user)

# UPDATE
@users_blueprint.route("/users/<id>",methods=["POST"])
def update_user(id):
    name = request.form["name"]
    balance = request.form["balance"]
    budget = request.form["budget"]
    account = User(name,balance,budget,id)
    user_repository.update(account)
    return redirect("/users/"+id)

# DELETE
@users_blueprint.route("/users/<id>/delete",methods=["POST"])
def delete_user(id):
    user_repository.delete(id)
    return redirect("/")