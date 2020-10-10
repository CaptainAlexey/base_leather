from app import app
import view
from covers.blueprint import posts
from app import db


app.register_blueprint(posts, url_prefix='/items')


if __name__=='__main__':
    app.run()