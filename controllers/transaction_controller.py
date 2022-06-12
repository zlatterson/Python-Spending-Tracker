from flask import Flask, render_template,request,redirect
from models.transaction import Transaction
from models.user import User
from flask import Blueprint

import repositories.transaction_repository as transaciton_repository
import repositories.user_repository as user_repository

transactions_blueprint = Blueprint("transaction", __name__)

@transactions_blueprint.route("/transactions/<id>/new")
def transaction(id):
    user = user_repository.select(id)
    return render_template("transactions/new.html", user=user)
