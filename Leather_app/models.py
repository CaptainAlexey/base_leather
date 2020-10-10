from app import db
import re


def slugify(s):
    pattern=r'[^\w+]'
    return re.sub(pattern,'-',s)



class Item(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(140), nullable=False)
    body=db.Column(db.Text, nullable=False)
    slug=db.Column(db.String(140), unique=True)

    def __init__(self, *args, **kwargs):
        super(Item, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug=slugify(self.title)

    def __repr__(self):
        return f'Item id: {self.id}, title: {self.title}'