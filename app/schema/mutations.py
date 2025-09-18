from graphene import Mutation, Field, String, Boolean
from .types import Book
from ..data.store import books_data

class AddBook(Mutation):
    class Arguments:
        title = String(required=True)
        author = String(required=True)

    success = Boolean()
    book = Field(Book)

    def mutate(root, info, title, author):
        new_entry = {'title': title, 'author': author}
        books_data.append(new_entry)
        return AddBook(success=True, book=Book(title=title, author=author))