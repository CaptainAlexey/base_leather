from flask import Blueprint
from flask import render_template
from models import Item
from flask import request
from .forms import ItemForm
from app import db
from flask import redirect
from flask import url_for

posts=Blueprint('covers', __name__, template_folder='templates')


@posts.route('/')
def index():
    
    items = Item.query.all()
    q=request.args.get('q')
    if q:
        items=Item.query.filter(Item.title.contains(q) | Item.body.contains(q)).all()
        

    return render_template('posts/index.html', items=items)


@posts.route('/create', methods=['POST', 'GET'])
def create_item():
    form=ItemForm()
    if request.method=='POST':
        title=request.form['title']
        body=request.form['body']
        if title:
            try:
                item=Item(title=title, body=body)
                db.session.add(item)
                db.session.commit()
                return redirect(url_for('covers.index'))
            except:
                print('Что-то пошло не так.')
        else:
            print('Введите название')

    return render_template('posts/create.html', form=form)


@posts.route('/<slug>')
def item_detail(slug):
    item=Item.query.filter(Item.slug==slug).first()
    return render_template('posts/item_detail.html', item=item)


