from flask import *
from database import db_session
from flask_login import LoginManager

import os

absp = os.path.abspath  # shorter abspath

DIR = os.getcwd()


def create_app():
    app = Flask(__name__)

    # setup with the configuration provided
    app.config.from_object('config.DevelopmentConfig')
    db_session.global_init(absp("database/data.sqlite/"))  # init database

    #############
    # init apps #
    #############

    # authentication
    from apps.auth.views import auth
    app.register_blueprint(auth)

    # main pages
    from apps.main.views import main
    app.register_blueprint(main)

    # messages
    from apps.message.views import message__
    app.register_blueprint(message__)

    ##################
    # authentication #
    ##################

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    ############
    # database #
    ############

    from database.models import User

    @login_manager.user_loader
    def load_user(user_id):
        s = db_session.create_session()
        user = s.query(User).filter(User.user_id == user_id).first()
        s.close()
        return user

    #################
    # event handler #
    #################

    from engine.event_handler import global_init as event_global_init
    event_global_init()

    # not a good idea to define a function inside another function
    @app.route('/favicon.ico')
    def favicon():
        return redirect(url_for('static', filename='favicon.ico'))

    return app


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    create_app().run(host='0.0.0.0', port=port)
