"""
The Flask app module
"""

from flask import Flask, render_template


def create_app(testing=False):
    """
    Application factory, used to create application
    """
    app = Flask(__name__)

    if testing:
        app.config['TESTING'] = True

    @app.route('/')
    def index():
        """
        Handles the index
        """
        return render_template('index.html')

    return app


if __name__ == '__main__':
    """
    Main entry point
    """
    app = create_app()
    app.run(debug=True)
