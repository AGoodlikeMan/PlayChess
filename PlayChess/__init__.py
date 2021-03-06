"""

Makes the web application modular!

"""

from flask import Flask
from flask_socketio import SocketIO

from .config import configurations

app = Flask(__name__)

# Add configurations

app.secret_key = configurations['_SECRET_KEY']
app.config['JSON_SORT_KEYS'] = configurations['JSON_AUTO_SORT']
app.config['TEST_USERNAME'] = configurations['TEST_USERNAME']
app.config['TEST_PASSWORD'] = configurations['TEST_PASSWORD']

## Socket IO connection for chat and playing chess games.
socketio = SocketIO(app)

from PlayChess.site.routes import mod
from PlayChess.admin.routes import mod
from PlayChess.blog.routes import mod
from PlayChess.chat.routes import mod
from PlayChess.game.routes import mod
from PlayChess.api.routes import mod

# makes an instance of admin class that can be used to add new admins!

from PlayChess.admin.admins import create_admin

# Register the blueprints!

app.register_blueprint(site.routes.mod)
app.register_blueprint(admin.routes.mod, url_prefix='/admin')
app.register_blueprint(blog.routes.mod, url_prefix='/blog')
app.register_blueprint(chat.routes.mod, url_prefix='/chat')
app.register_blueprint(game.routes.mod, url_prefix='/game')
app.register_blueprint(api.routes.mod, url_prefix='/api')

# Makes chess board easily accessible thorugh terminal

from PlayChess.utils.chessboard import Chessboard

# Make database accessible for unit testing

from PlayChess.database import db