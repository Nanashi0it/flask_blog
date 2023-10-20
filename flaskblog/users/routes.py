import os
from PIL import Image
from flask import Blueprint, render_template, url_for, flash, redirect, request, abort
from flaskblog import db, bcrypt
from flaskblog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, RequestResetPasswordForm, ChangePasswordForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flaskblog.users.utils import save_image, send_reset_email

users = Blueprint("users", __name__)

@users.route("/register", methods=["GET", "POST"]) 
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username= form.username.data, email= form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("You account has been created! You are now able to log in.", "success")

        return redirect(url_for("users.login"))
    
    return render_template("register.html", title="Register", form=form)

@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            # args => return none if the key doesn't exist
            # without args => throw an error if the key doesn't exist
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("main.home"))
        else:
            flash(f"Login Unsuccessful. Please check email and password!", "danger")

    return render_template("login.html", title="Login", form=form)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))

@users.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.image.data:
            image_file = save_image(form.image.data)
            current_image_file = current_user.image
            # Remove old image
            if current_image_file != "default.jpg":
                image_path = os.path.join(users.root_path, "static/profile_pics", current_image_file)
                os.remove(image_path)
            current_user.image = image_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account have been updated!", "success")

        return redirect(url_for("users.account"))
    
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image = url_for('static', filename=f"profile_pics/{current_user.image}")

    return render_template("account.html", title="Account", 
                           image=image, form=form)

@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(per_page=5, page=page)
    
    return render_template("user_posts.html", posts=posts, user=user)

@users.route("/reset_password", methods=["GET", "POST"])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    
    form = RequestResetPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash("An email has been sent with instructions to reset your password.", "info")

        return redirect(url_for("users.login"))
    
    return render_template("reset_password_request.html", title="Reset Password", form=form)

@users.route("/reset_password/<token>", methods=["GET", "POST"])
def change_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    
    user = User.verify_reset_token(token)
    
    if user is None:
        flash("That is an invalid or expired token", "warning")
        return redirect(url_for("users.reset_password_request"))
    
    form = ChangePasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user.password = hashed_password
        db.session.commit()
        flash("You password has been changed! You are now able to log in.", "success")

        return redirect(url_for("users.login"))

    return render_template("change_password.html", title="Change Password", form=form)