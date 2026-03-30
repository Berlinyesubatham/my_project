from flask import Flask, request, render_template, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

def get_db():
    return sqlite3.connect("database.db")

@app.route("/")
def home():
    return "Flask server running"

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    mobile = request.form.get("mobile")
    address = request.form.get("address")
    source = request.form.get("source")

    db = get_db()
    cur = db.cursor()
    cur.execute(
        "INSERT INTO enquiries VALUES (NULL,?,?,?,?,?)",
        (name, email, mobile, address, source)
    )
    db.commit()
    db.close()
    return "Saved successfully"

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT * FROM admin WHERE username=? AND password=?", (u,p))
        user = cur.fetchone()

        if user:
            session["admin"] = u
            return redirect("/dashboard")
        else:
            return "Wrong login"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "admin" not in session:
        return redirect("/login")

    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM enquiries")
    data = cur.fetchall()
    db.close()

    return render_template("dashboard.html", data=data)

# 🔥 DELETE ROUTE
@app.route("/delete/<int:id>")
def delete(id):
    if "admin" not in session:
        return redirect("/login")

    db = get_db()
    cur = db.cursor()
    cur.execute("DELETE FROM enquiries WHERE id=?", (id,))
    db.commit()
    db.close()

    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

app.run(debug=True)




