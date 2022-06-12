from flask import Flask, render_template,request,redirect
from models.transaction import Transaction
from models.user import User
from models.tag import Tag
from models.item import Item
from flask import Blueprint

import repositories.transaction_repository as transaciton_repository
import repositories.user_repository as user_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.item_repository as item_repository

transactions_blueprint = Blueprint("transaction", __name__)

# GET
@transactions_blueprint.route("/<id>/transactions/new")
def transaction(id):
    user = user_repository.select(id)
    merchants = merchant_repository.select_all()
    items = item_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", user=user, merchants=merchants, items=items)

# CREATE
@transactions_blueprint.route("/transactions",methods=["POST"])
def create_user():
    name = request.form["name"]
    balance = request.form["balance"]
    budget = request.form["budget"]
    transaction = Transaction(name,balance,budget)
    user_repository.save(account)
    return redirect("/users")