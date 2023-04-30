from flask import Flask, redirect, render_template, request
from users import User
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add_entry', methods = ["POST"])
def add_entry():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }

    User.save(data)

    return redirect('/')


@app.route('/user/dashboard')
def users_dashboard():
    users_data = User.get_all()

    return render_template("users_dashboard.html", myusers = users_data)



if __name__ =="__main__":
    app.run(debug=True, port = 5001)