from blog.models import *

import graphene
from graphene_django import DjangoObjectType


def update_create_instance(instance, args, exception=['id']):
    if instance:
        [setattr(instance, key, value) for key, value in args.items() if key not in exception]
    if 'book' not in exception:
        instance.save()
    return instance

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "description")

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    def resolve_all_books(self, info):
        return Book.objects.all()

    book = graphene.Field(BookType, id=graphene.Int())
    def resolve_book(self, info, id):
        return Book.objects.get(pk=id)

class CreateBook(graphene.Mutation):
    book = graphene.Field(BookType)

    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        description = graphene.String()

    def mutate(self, info, title, author, description=None):
        book = Book(title=title, author=author, description=description)
        book.save()
        return CreateBook(book=book)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

# Query operation example:

# Query operation for all books:
# query {
#     allBooks {
#       id
#       title
#       author
#       description
#     }
#   }

# Query operation for a single book:
# query {
#     book(id: 1) {
#       id
#       title
#       author
#       description
#     }
#   }


#Mutation operation example:
# mutation {
#   createBook(
#     title: "Book Title 4"
#     author: "Author Name 4"
#     description: "Book Description 4"
#   ) {
#     book {
#       id
#       title
#       author
#       description
#     }
#   }
# }