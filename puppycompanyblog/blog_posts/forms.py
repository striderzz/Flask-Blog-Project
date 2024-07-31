
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length

class BlogPostForm(FlaskForm):
  title = StringField('Title',validators=[DataRequired(),Length(max=50)])
  text = TextAreaField('Text',validators=[DataRequired()])
  submit = SubmitField("Post")