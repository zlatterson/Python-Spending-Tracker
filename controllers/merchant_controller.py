from flask import Flask, render_template,request,redirect
from models.merchant import Merchant
from flask import Blueprint

import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchant", __name__)

@merchants_blueprint.route("/merchants/<id>")
def merchant(id):
    merchants = merchant_repository.select_all()
    print(merchants)
    return render_template("/merchants/index.html", merchants=merchants)

# NEW
@merchants_blueprint.route("/merchants/<id>/new")
def new_merchant(id):
    merchants = merchant_repository.select_all()
    return render_template("merchants/new.html", merchants=merchants)

# CREATE
@merchants_blueprint.route("/merchants/<id>",methods=["POST"])
def create_merchant(id):
    name = request.form["merchant_name"]
    received = 0
    merchant = Merchant(name,received)
    print(merchant)
    merchant_repository.save(merchant)
    return redirect("/users/")

# # SHOW
@merchants_blueprint.route("/merchants")
def show_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/show.html", merchant=merchant)

# # EDIT
@merchants_blueprint.route("/merchants/<id>/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/edit.html", merchant=merchant)

# # UPDATE
@merchants_blueprint.route("/merchants/<id>",methods=["POST"])
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