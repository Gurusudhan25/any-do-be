from flask import Blueprint, request
import pymongo

from schema.user import db

bp = Blueprint("signin", __name__)


@bp.route("/signin", methods=['POST'])
def signin():
    if request.method == "POST":
        userMail = request.form['email']
        password = request.form['password']
        isUserFound = db['user'].find(
            {"email": userMail, "password": password})
    return "user: isUserFound"
