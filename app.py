from flask import Flask, request

# Local modules
from authentication import signin, signup

app = Flask(__name__)

if __name__ == "__main__":
    app.debug = True
    app.register_blueprint(signup.bp)
    app.register_blueprint(signin.bp)
    app.run()
