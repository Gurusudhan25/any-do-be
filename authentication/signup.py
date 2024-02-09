from flask import Blueprint, request
import pymongo

from schema.user import db

bp = Blueprint("signup", __name__)


@bp.route("/signin", methods=['POST'])
def signup():
    if request.method == "POST":
        user = request.form.to_dict()
        userCol = db['user']
        # pass encryption not done
        userCol.insert_one(user)
    return {
        "data": "user registered"
    }
