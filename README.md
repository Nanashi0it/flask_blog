# Flask Blog Website
This is a Flask Blog Website.

Reference: [Flask Tutorials - Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)

## Features

### MAIN
- Home page.
- About page.
### USER
- User page.
- User register, login, logout.
- User reset password.
- Update username, email, and profile image.
- View all user posts.
### POST
- Create a new post.
- Update post.
- Delete post.

## Requirements

- bcrypt: 4.0.1
- blinker: 1.6.3
- click: 8.1.7
- colorama: 0.4.6
- dnspython: 2.4.2
- email-validator: 2.0.0.post2
- Flask: 2.3.3
- Flask-Bcrypt: 1.0.1
- Flask-Login: 0.6.2
- Flask-Mail: 0.9.1
- Flask-SQLAlchemy: 3.1.1
- Flask-WTF: 1.2.1
- greenlet: 3.0.0
- gunicorn: 21.2.0
- idna: 3.4
- itsdangerous: 2.1.2
- Jinja2: 3.1.2
- MarkupSafe: 2.1.3
- packaging: 23.2
- Pillow: 10.1.0
- SQLAlchemy: 2.0.22
- typing_extensions: 4.8.0
- Werkzeug: 2.3.7
- WTForms: 3.1.0

## Installation and Run

Download source code from Github: `https://github.com/Nanashi0it/flaskblog.git`

**NOTE BEFORE RUNNING PROJECT:**
- Before running the application you need to create some environment variables:
    + `SQLALCHEMY_DATABASE_URI` for `SQLALCHEMY_DATABASE_URI`: Name of the database (Eg: site.db).
    + `SECRET_KEY` for `SECRET_KEY`: secret key hashes the password to save in the database.
    + `EMAIL_USER` for `MAIL_USERNAME`: Email address that is used to send password reset email.
    + `EMAIL_PASSWORD` for `MAIL_PASSWORD`: Password of the email you used above. This password should be [App Password](https://support.google.com/mail/answer/185833?hl=vi) if you user Gmail.
- If you use the application's virtual environment (env), you do not need to install additional packages in the requirements.txt file, but you need to activate it before running the application. More detail in [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)

Go to directory: `cd flaskBlog`

Run in command line: `python app.py` or `py app.py`
