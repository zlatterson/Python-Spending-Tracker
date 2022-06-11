from flask import Flask, render_template,request,redirect
from models.merchant import Merchant
from flask import Blueprint

import repositories.merchant_repository as merchant_repository

merchants_blueprint = Blueprint("merchant", __name__)

@merchants_blueprint.route("/merchants")
def merchant():
    merchants = merchant_repository.select_all()
    print(merchants)
    return render_template("/merchants/index.html", merchants = merchants)