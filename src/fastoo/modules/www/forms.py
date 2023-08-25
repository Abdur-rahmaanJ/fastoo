from starlette_wtf import StarletteForm
from wtforms import StringField
from wtforms.validators	import DataRequired


class MyForm(StarletteForm):
    name = StringField('name', validators=[DataRequired()])
