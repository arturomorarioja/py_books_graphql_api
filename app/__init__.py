from flask import Flask
from .routes.books import books_bp

def create_app() -> Flask:
    app = Flask(__name__)

    # Health check or root
    @app.get('/health')
    def health():
        return {'status': 'ok'}

    # Register GraphQL endpoint
    app.register_blueprint(books_bp)

    return app