from flask import Flask, render_template
from extensions import db
from routes.auth_routes import auth_bp

app = Flask(__name__)

app.secret_key = "erp_secret_key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///erp.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(auth_bp)

# ---------------- DASHBOARD ROUTES ---------------- #

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")


@app.route("/teacher/dashboard")
def teacher_dashboard():
    return render_template("teacher/dashboard.html")


@app.route("/student/dashboard")
def student_dashboard():
    return render_template("student/dashboard.html")


# ---------------- DATABASE CREATE ---------------- #

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
