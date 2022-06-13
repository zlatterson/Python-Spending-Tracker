from datetime import datetime
from flask import Flask, render_template,request,redirect
from models.merchant import Merchant
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
@items_blueprint.route("/users/<id>/items/new")
def transaction(id):
    user = user_repository.select(id)
    merchants = merchant_repository.select_all()
    items = item_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("/users/items/new.html", user=user, merchants=merchants, items=items, tags=tags)

# CREATE
@items_blueprint.route("/users/<id>/items",methods=["POST"])
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
    dt_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transaction = Transaction(merchant_object,user_object,item,cost, dt_string)
    transaciton_repository.save(transaction)
    # reduce user money
    updated_user_cash = int(user_object.money) - int(cost)
    updated_user = User(user_object.name,updated_user_cash,user_object.daily_allowance,id)
    user_repository.update(updated_user)

    updated_merchant_cash = int(merchant_object.money_received) + int(cost)
    updated_merchant = Merchant(merchant_object.name,updated_merchant_cash,merchant_object.id)
    merchant_repository.update(updated_merchant)
    # reduce user money:working

    # update tag
    updated_tag_used = int(tag_object.times_used) + 1
    updated_tag = Tag(tag_object.name,updated_tag_used,tag_object.id)
    tag_repository.update(updated_tag)


    return redirect("/users/"+id)

@items_blueprint.route("/users/items")
def show_merchant():
    items = item_repository.select_all()
    return render_template("/users/items/show.html", items=items)