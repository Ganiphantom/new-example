from flask import Blueprint, render_template, request, redirect, session
from models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        user = User.query.filter_by(
            email=email,
            password=password,
            role=role
        ).first()

        if user:

            session["user_id"] = user.id
            session["role"] = user.role

            # Role based redirect
            if role == "admin":
                return redirect("/admin/dashboard")

            elif role == "teacher":
                return redirect("/teacher/dashboard")

            elif role == "student":
                return redirect("/student/dashboard")

        else:
            return render_template(
                "auth/login.html",
                error="Invalid Login Credentials"
            )

    return render_template("auth/login.html")
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")