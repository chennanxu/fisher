from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange


class searchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=50)])
    page = IntegerField(validators=[NumberRange(min=1, max=50)], default=1)