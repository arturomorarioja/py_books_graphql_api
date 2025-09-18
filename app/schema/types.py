from graphene import ObjectType, String

class Book(ObjectType):
    title = String()
    author = String()