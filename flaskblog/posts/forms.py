from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CreatePostForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired()])
    content = TextAreaField(label="Content", validators=[DataRequired()])
    submit = SubmitField(label="Post")

class UpdatePostForm(FlaskForm):
    title = StringField(label="Title", validators=[DataRequired()])
    content = TextAreaField(label="Content", validators=[DataRequired()])
    submit = SubmitField(label="Update")