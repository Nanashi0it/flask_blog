from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

db = SQLAlchemy()

# Bcrypt => Hash password to save in db
bcrypt = Bcrypt()

# LoginManager => Manage login process
login_manager = LoginManager()

# Tell Extension login_required where login route locate
login_manager.login_view = "users.login"

# Alert if try to the access (need login) page without login
login_manager.login_message_category = "danger"

mail = Mail()

# Create different instances of app with different configurations
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app