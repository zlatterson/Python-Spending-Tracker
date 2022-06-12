from flask import Flask, render_template,request,redirect
from models.tag import Tag
from flask import Blueprint

import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tag", __name__)

@tags_blueprint.route("/tags")
def tag():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags=tags)


# NEW
@tags_blueprint.route("/tags/new")
def new_tag():
    tags = tag_repository.select_all()
    return render_template("tags/new.html", tags=tags)

# # CREATE
@tags_blueprint.route("/tags",methods=["POST"])
def create_tag():
    name = request.form["tag_name"]
    tag = Tag(name,0)
    tag_repository.save(tag)
    return redirect("/tags")

# # SHOW
# @users_blueprint.route("/users/<id>")
# def show_users(id):
#     user = user_repository.select(id)
#     print(user)
#     return render_template("users/show.html", user=user)

# # EDIT
# @users_blueprint.route("/users/<id>/edit")
# def edit_user(id):
#     user = user_repository.select(id)
#     return render_template("users/edit.html", user=user)

# # UPDATE
# @users_blueprint.route("/users/<id>",methods=["POST"])
# def update_user(id):
#     name = request.form["name"]
#     balance = request.form["balance"]
#     budget = request.form["budget"]
#     account = User(name,balance,budget,id)
#     user_repository.update(account)
#     return redirect("/users")

# # DELETE
# @users_blueprint.route("/users/<id>/delete",methods=["POST"])
# def delete_user(id):
#     user_repository.delete(id)
#     return redirect("/users")