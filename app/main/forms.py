from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from wtforms.validators import Required, Length, Email, EqualTo, ValidationError
from ..models import User

class BlogForm(FlaskForm):
    title = StringField('Title', validators =[Required()])
    content = TextAreaField('Content', validators = [Required()])
    submit = SubmitField('Post Blog')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us something about yourself',validators=[Required()])
    submit = SubmitField('Submit')

class CreateBlog(FlaskForm):
    title = StringField('Title',validators=[Required()])
    content = TextAreaField('Blog Content',validators=[Required()])
    submit = SubmitField('Post')