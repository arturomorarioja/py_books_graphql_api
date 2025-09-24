from flask import Flask
from .routes.graphql import graphql_bp

def create_app() -> Flask:
    app = Flask(__name__)

    # Health check or root
    @app.get('/health')
    def health():
        return {'status': 'ok'}

    # Register GraphQL endpoint
    app.register_blueprint(graphql_bp)

    return app