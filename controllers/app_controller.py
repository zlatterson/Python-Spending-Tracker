from flask import Flask, render_template, request, redirect
from models.user import User
from flask import Blueprint

import repositories.user_repository as user_repository


app_blueprint = Blueprint("app", __name__)

# RESTful CRUD Routes

# INDEX
# GET '/tasks'
@app_blueprint.route("/")
def app():
    users = user_repository.select_all() 
    return render_template("/index.html", users=users)


# SHOW
@app_blueprint.route("/<id>")
def show_users(id):
    user = user_repository.select(id)
    print(user)
    return render_template("/show.html", user=user)



# NEW
@app_blueprint.route("/new")
def new_user():
    users = user_repository.select_all()
    return render_template("/new.html", users=users)

# CREATE
@app_blueprint.route("/",methods=["POST"])
def create_user():
    name = request.form["name"]
    balance = request.form["balance"]
    budget = request.form["budget"]
    account = User(name,balance,budget)
    user_repository.save(account)
    return redirect("/users")


# EDIT
# @app_blueprint.route("/<id>/edit")
# def edit_user(id):
#     user = user_repository.select(id)
#     return render_template("/edit.html", user=user)

# # UPDATE
# @app_blueprint.route("/<id>",methods=["POST"])
# def update_user(id):
#     name = request.form["name"]
#     balance = request.form["balance"]
#     budget = request.form["budget"]
#     account = User(name,balance,budget,id)
#     user_repository.update(account)
#     return redirect("/")

# DELETE
@app_blueprint.route("/users/<id>/delete",methods=["POST"])
def delete_user(id):
    user_repository.delete(id)
    return redirect("/users")