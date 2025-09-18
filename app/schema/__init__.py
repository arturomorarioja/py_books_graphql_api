from graphene import Schema
from .queries import Query
from .mutations import AddBook
from graphene import ObjectType

class Mutation(ObjectType):
    add_book = AddBook.Field()

schema = Schema(query=Query, mutation=Mutation)