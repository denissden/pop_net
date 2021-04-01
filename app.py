from flask import *
from database import db_session

import os

absp = os.path.abspath  # shorter abspath

DIR = os.getcwd()


def create_app():
    app = Flask(__name__)

    # setup with the configuration provided
    app.config.from_object('config.DevelopmentConfig')
    from apps.pop_net.views import pop_net

    db_session.global_init(absp("database/data.sqlite/"))  # init database

    app.register_blueprint(pop_net)

    # not a good idea to define a function inside another function
    @app.route('/favicon.ico')
    def favicon():
        return redirect(url_for('static', filename='favicon.ico'))

    return app


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    create_app().run(host='0.0.0.0', port=port)
