"""
The Flask app module
"""

import os
import connexion

from flask import render_template


def create_app(testing=False):
    """
    Application factory, used to create application
    """
    basedir = os.path.abspath(os.path.dirname(__file__))
    connex_app = connexion.App(__name__, specification_dir=basedir)
    configure_apispec(connex_app)

    # Get the underlying Flask app instance
    app = connex_app.app
    # app.config.from_object('api.config')

    if testing:
        app.config['TESTING'] = True

    @app.route('/')
    def index():
        """
        Handles the index
        """
        return render_template('index.html')

    return app


def configure_apispec(app):
    """
    Configure the REST API definition for swagger yaml file
    """
    app.add_api("swagger.yml")


def main():
    """
    Main entry point
    """
    app = create_app()
    app.run(debug=True)


if __name__ == '__main__':
    main()
