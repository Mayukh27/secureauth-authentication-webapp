from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector
import bcrypt

app = Flask(_name_)
app.secret_key = "pwc_launchpad_secret"

# ---------- DATABASE CONNECTION ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_mysql_password",
    database="secure_auth"
)

# ---------- ROUTES ----------

@app.route("/")
def home():
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"].encode()

        hashed = bcrypt.hashpw(password, bcrypt.gensalt())

        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO users(username,password) VALUES(%s,%s)",
                (username, hashed)
            )
            db.commit()
            return redirect("/login")
        except:
            return "Username already exists"

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"].encode()

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        user = cursor.fetchone()

        if not user:
            return "Invalid credentials"

        if user["failed_attempts"] >= 5:
            return "Account locked due to multiple failed attempts"

        if bcrypt.checkpw(password, user["password"].encode()):
            cursor.execute(
                "UPDATE users SET failed_attempts=0 WHERE username=%s",
                (username,)
            )
            db.commit()
            session["user"] = username
            return redirect("/dashboard")
        else:
            cursor.execute(
                "UPDATE users SET failed_attempts = failed_attempts + 1 WHERE username=%s",
                (username,)
            )
            db.commit()
            return "Wrong password"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html", user=session["user"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if _name_ == "_main_":
    app.run(debug=True)