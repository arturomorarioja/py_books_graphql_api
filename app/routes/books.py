from flask import Blueprint, request, jsonify, Response
from graphql import graphql_sync
from ..schema import schema

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['POST'])
def graphql_server():
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 415

    payload = request.get_json(silent=True) or {}
    query = payload.get('query')
    variables = payload.get('variables')
    operation_name = payload.get('operationName')

    if not query:
        return jsonify({'error': 'Missing "query" in request body'}), 400

    result = graphql_sync(
        schema.graphql_schema,
        source=query,
        variable_values=variables,
        operation_name=operation_name,
        context_value={'request': request},
    )

    response = {}
    if result.errors:
        response['errors'] = [err.formatted for err in result.errors]
    if result.data is not None:
        response['data'] = result.data

    return jsonify(response), 200