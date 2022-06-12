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


items_blueprint = Blueprint("item", __name__)

# GET
@items_blueprint.route("/<id>/items/new")
def transaction(id):
    user = user_repository.select(id)
    merchants = merchant_repository.select_all()
    items = item_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("/items/new.html", user=user, merchants=merchants, items=items, tags=tags)

# CREATE
@items_blueprint.route("/<id>/items",methods=["POST"])
def create_user(id):
    name = request.form["item"]
    cost = request.form["cost"]
    tag = request.form["tag"]
    merchant = request.form["merchant"]
    tag_object = tag_repository.select(tag)
    merchant_object = merchant_repository.select(merchant)
    item = Item(name,cost,tag_object,merchant_object)
    item_repository.save(item)
    # item saved: working
    user_object = user_repository.select(id)
    transaction = Transaction(merchant_object,user_object,item,cost, "11/11")
    transaciton_repository.save(transaction)
    # reduce user money

    return redirect("/items")

@items_blueprint.route("/items")
def show_merchant():
    items = item_repository.select_all()
    return render_template("/items/show.html", items=items)