from flask import Flask, render_template,request,redirect
from models.merchant import Merchant
from models.user import User
from flask import Blueprint

import repositories.merchant_repository as merchant_repository
import repositories.user_repository as user_repository

merchants_blueprint = Blueprint("merchant", __name__)

@merchants_blueprint.route("/users/<id>/merchants/")
def merchant(id):
    user = user_repository.select(id)
    merchants = merchant_repository.select_all()
    merchants_with_percent = Merchant.received_as_percentage(merchants)
    merchants_by_most_money = Merchant.order_merchants_by_spent(merchants_with_percent)
    merchant_money_formatted = Merchant.format_money(merchants_by_most_money)
    return render_template("/users/merchants/index.html", 
    merchants=merchant_money_formatted, 
    user=user)

# NEW
@merchants_blueprint.route("/users/<id>/merchants/new")
def new_merchant(id):
    user = user_repository.select(id)
    merchants = merchant_repository.select_all()
    return render_template("/users/merchants/new.html", merchants=merchants, user=user) 

# CREATE
@merchants_blueprint.route("/users/<id>/merchants/",methods=["POST"])
def create_merchant(id):
    name = request.form["merchant_name"]
    received = 0
    merchant = Merchant(name,received)
    print(merchant)
    merchant_repository.save(merchant)
    return redirect("/users/"+id+"/items/new")

# # SHOW
@merchants_blueprint.route("/users/merchants")
def show_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("/users/merchants/show.html", merchant=merchant)

# # EDIT
@merchants_blueprint.route("/users/<id>/merchants/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("/users/merchants/edit.html", merchant=merchant)

# # UPDATE
@merchants_blueprint.route("/users/merchants/<id>",methods=["POST"])
def update_user(id):
    name = request.form["merchant_name"]
    received = request.form["received"]
    merchant = Merchant(name,received,id)
    merchant_repository.update(merchant)
    return redirect("/merchants")

# # DELETE
@merchants_blueprint.route("/merchants/<id>/delete",methods=["POST"])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect("/merchants")