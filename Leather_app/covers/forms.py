from wtforms import Form, StringField, TextAreaField


class ItemForm(Form):
    title=StringField('Title')
    body=TextAreaField('Body')