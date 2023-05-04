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

@app.route('/show/<int:user_id>')
def show_one(user_id):
    oneuser = User.get_one(user_id)
    return render_template("show_user.html", one_user = oneuser)

# update and render update html routes

@app.route('/update', methods = ["POST"])
def update():
    User.editUser(request.form)
    return redirect('/user/dashboard')

@app.route('/user/edit/<int:user_id>')
def edit(user_id):
    return render_template("editUser.html", one_user = User.get_one(user_id))


@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    User.deleteUser(user_id)
    return redirect('/user/dashboard')

if __name__ =="__main__":
    app.run(debug=True, port = 5001)