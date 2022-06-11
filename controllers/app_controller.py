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


# # NEW
# # GET '/tasks/new'
@app_blueprint.route("/new", methods=["GET"])
def new_spending():
    users = user_repository.select_all()
    return render_template("/new.html", all_users = users)

# # CREATE
# # POST '/tasks'
# @tasks_blueprint.route("/tasks", methods=["POST"])
# def create_task():
#     description = request.form["description"]
#     user_id = request.form["user_id"]
#     duration = request.form["duration"]
#     completed = request.form["completed"]
#     user = user_repository.select(user_id)
#     task = Task(description,user,duration,completed)
#     task_repository.save(task)
#     return redirect("/tasks")


# # SHOW
# # GET '/tasks/<id>'
# @tasks_blueprint.route("/tasks/<id>")
# def show_task(id):
#     found_task = task_repository.select(id)
#     return render_template("/tasks/show.html", task = found_task)

# # ___________________v
# # EDIT
# # GET '/tasks/<id>/edit'
# @tasks_blueprint.route("/tasks/<id>/edit")
# def edit_task(id):
#     task = task_repository.select(id)
#     users = user_repository.select_all()
#     return render_template("/tasks/edit.html", task=task, all_users=users)

# # UPDATE
# # PUT '/tasks/<id>'
# @tasks_blueprint.route("/tasks/<id>", methods=["POST"])
# def update_task(id):
#     description = request.form["description"]
#     user_id = request.form["user_id"]
#     duration = request.form["duration"]
#     completed = request.form["completed"]
#     user = user_repository.select(user_id)
#     task = Task(description,user,duration,completed, id)
#     task_repository.update(task)
#     return redirect("/tasks")

# # ____________________^

# # DELETE
# # DELETE '/tasks/<id>'

# @tasks_blueprint.route("/tasks/<id>/delete", methods=["POST"])
# def delete_task(id):
#     task_repository.delete(id)
#     return redirect("/tasks")