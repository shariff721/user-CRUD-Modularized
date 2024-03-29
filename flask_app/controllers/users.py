from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User



@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add_entry', methods = ["POST"])
def add_entry():
    if not User.validate_user(request.form):
            return redirect('/')
    else:
            result = User.save(request.form)
            return redirect(f'/show/{result}')


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
    if not User.validate_user(request.form):
            return redirect(request.referrer)
    else:
            User.editUser(request.form)
            return redirect('/user/dashboard')

@app.route('/user/edit/<int:user_id>')
def edit(user_id):
    return render_template("editUser.html", one_user = User.get_one(user_id))


@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    User.deleteUser(user_id)
    return redirect('/user/dashboard')