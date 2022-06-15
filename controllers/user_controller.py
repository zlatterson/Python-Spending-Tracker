from datetime import datetime
from flask import Flask, render_template,request,redirect
from models.user import User
from models.transaction import *
from flask import Blueprint

import repositories.user_repository as user_repository
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository

users_blueprint = Blueprint("user", __name__)

@users_blueprint.route("/users/<id>")
def show_users(id):
    found_user = user_repository.select(id)
    user = User.format_money(found_user)

    transacitons = transaction_repository.select_all()
    user_transacts = Transaction.sort_by_user(transacitons,user.id)
    date_sorted = Transaction.sort_by_time(user_transacts)

    current_date = str(datetime.date(datetime.now()))
    cur_year = current_date[0:4]
    cur_month = current_date[5:7]
    cur_day = current_date[8:10]
    month_sorted = Transaction.sort_by_month(date_sorted,cur_year,cur_month)
    month_fmt = datetime(day=int(cur_day), month=int(cur_month), year=int(cur_year)).strftime('%A %d %B %Y')
    monthly_expendature = Transaction.find_monthly_expendature(month_sorted)
    green_if_monthly = Transaction.green_text(monthly_expendature, user.daily_allowance)
    red_if_monthly = Transaction.red_text(monthly_expendature, user.daily_allowance)

    tags = tag_repository.select_all()
    tag_total = Transaction.find_tag_total(tags)
    update_transactions = Transaction.change_transaction_object_tag_into_percentage(date_sorted,tag_total)
    transactions_with_today_bool = Transaction.check_if_date_condition(update_transactions,current_date)
    tranasctions_with_money_formatted = Transaction.format_money(transactions_with_today_bool)
    transaction_dates = Transaction.transaction_dates(update_transactions)

    user = User.format_monthly_allowance(user)
    return render_template("/users/show.html", 
    user=user, 
    user_transacts=tranasctions_with_money_formatted, 
    green_if_monthly=green_if_monthly,
    red_if_monthly=red_if_monthly,
    month_fmt = month_fmt,
    transaction_dates=transaction_dates)

@users_blueprint.route("/users/<id>/<year>/<month>")
def show_users_month(id,year,month):
    found_user = user_repository.select(id)
    user = User.format_money(found_user)

    transacitons = transaction_repository.select_all()
    user_transacts = Transaction.sort_by_user(transacitons,user.id)
    date_sorted = Transaction.sort_by_time(user_transacts)
    month_sorted = Transaction.sort_by_month(date_sorted,year,month)
    month_fmt = month + "/" + year
    monthly_expendature = Transaction.find_monthly_expendature(month_sorted)
    green_if_monthly = Transaction.green_text(monthly_expendature, user.daily_allowance)
    red_if_monthly = Transaction.red_text(monthly_expendature, user.daily_allowance)

    tags = tag_repository.select_all()
    tag_total = Transaction.find_tag_total(tags)

    update_transactions = Transaction.change_transaction_object_tag_into_percentage(month_sorted,tag_total)
    current_date = str(datetime.date(datetime.now()))
    transactions_with_today_bool = Transaction.check_if_date_condition(update_transactions,current_date)
    tranasctions_with_money_formatted = Transaction.format_money(transactions_with_today_bool)
    transaction_dates = Transaction.transaction_dates(update_transactions)

    user = User.format_monthly_allowance(user)
    return render_template("/users/show.html", 
    user=user, 
    user_transacts=tranasctions_with_money_formatted,
    green_if_monthly=green_if_monthly,
    red_if_monthly=red_if_monthly,
    month_fmt=month_fmt,
    transaction_dates=transaction_dates)
 

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