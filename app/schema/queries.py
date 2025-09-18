from graphene import ObjectType, List, Field, String
from .types import Book
from ..data.store import books_data

class Query(ObjectType):
    
    # Returns a single book by title
    book = Field(Book, title=String(required=True))
    
    # Returns all books
    books = List(Book)

    def resolve_book(root, info, title):
        for b in books_data:
            if b['title'] == title:
                return Book(title=b['title'], author=b['author'])
        return None

    def resolve_books(root, info):
        return [Book(title=b['title'], author=b['author']) for b in books_data]