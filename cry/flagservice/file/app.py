from cipher import AESCBC
from flask import Flask, redirect, render_template, request
from secret import flag

app = Flask(__name__)
cipher = AESCBC()


@app.route("/")
def index():
    try:
        token = request.cookies.get("token")
        session = cipher.decrypt(token)
        return render_template("index.html", session=session, flag=flag)
    except Exception:
        pass
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    session = {"admin": False, "username": username}
    token = cipher.encrypt(session)

    response = redirect("/")
    response.set_cookie("token", token)
    return response


@app.route("/logout", methods=["POST"])
def logout():
    response = redirect("/")
    response.set_cookie("token", expires=0)
    return response


if __name__ == "__main__":
    app.run()
