# import graphene
# from graphene_django import DjangoObjectType

# from .models import categoryOld as CategoryModel, Post as PostModel , Tag as TagModel

# # Create Type 
# class CategoryType(DjangoObjectType):
#     class Meta:
#         model = CategoryModel
#         fields = ("id", "name")

# class TagType(DjangoObjectType):
#     class Meta:
#         model = TagModel
#         fields = ("id", "name")

# class PostType(DjangoObjectType):
#     class Meta:
#         model = PostModel
#         fields = ("id", "title", "detail", "category","tags")


# class Query(graphene.ObjectType):

#     hello = graphene.String(default_value="Hi NerdBit!")

#     posts = graphene.List(PostType)
#     post = graphene.Field(PostType, id = graphene.Int())
#     categories = graphene.List(CategoryType)
#     category = graphene.Field(CategoryType, id = graphene.Int())
    
#     tags = graphene.List(TagType)
#     tag = graphene.Field(TagType, id = graphene.Int())


#     category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))
#     tag_by_name = graphene.Field(TagType, name=graphene.String(required=True))

#     def resolve_post(self, info, **kwargs):
#         id = kwargs.get('id')
#         if id is not None: 
#             return PostModel.objects.get(pk = id)
#         return None

#     def resolve_category(self, info, **kwargs):
#         id = kwargs.get('id')
#         if id is not None: 
#             return CategoryModel.objects.get(pk = id)
#         return None

#     def resolve_all_posts(self, info, **kwargs):
#         try:
#             return PostModel.objects.all()        
#         except PostModel.DoesNotExist:
#             return None

#     def resolve_all_categories(self, info, **kwargs):
#         try:
#             return CategoryModel.objects.all()        
#         except CategoryModel.DoesNotExist:
#             return None

# # Input Object Type

# class CategoryInput(graphene.InputObjectType):
#     id = graphene.ID()
#     detail = graphene.String()

# class TagInput(graphene.InputObjectType):
#     id = graphene.ID()
#     detail = graphene.String()

# class PostInput(graphene.InputObjectType):
#     id = graphene.ID()
#     title = graphene.String()
#     detail = graphene.String()
#     category = graphene.List(CategoryInput)
#     tag = graphene.List(TagInput)

# # Mutations 

# class CreatePost(graphene.Mutation):
#     class Arguments: 
#         input = PostInput(required = True)
#     ok  = graphene.Boolean()
#     post = graphene.Field(PostType)

#     @staticmethod
#     def mutate(root, info, input=None):
#         ok = True
#         post_instance = PostModel(title = input.title)
#         post_instance.save()
#         return CreatePost(ok = ok, post = post_instance)

# class UpdatePost(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required = True)
#         input = PostInput(required = True)
#     ok  = graphene.Boolean()
#     post = graphene.Field(PostType)

#     @staticmethod
#     def mutate(root, info, id,  input=None):
#         ok = False
#         post_instance = PostModel.objects.get(pk=id)
#         if post_instance:
#             ok = True
#             post_instance.title = input.title
#             post_instance.save()
#             return UpdatePost(ok = ok, post = post_instance)
#         return UpdatePost(ok = ok, post = None)

# class DeletePost(graphene.Mutation):
#     class Arguments:
#         id = graphene.Int(required = True)
#     ok  = graphene.Boolean()

#     @staticmethod
#     def mutate(root, info, id,  input=None):
#         ok = False
#         post_instance = PostModel.objects.get(pk=id)
#         if post_instance:
#             ok = True
#             post_instance.delete()
#             return DeletePost(ok = ok)

# class Mutation(graphene.ObjectType):
#     createPost = CreatePost.Field()
#     updatePost = UpdatePost.Field()
#     deletePost = DeletePost.Field()

# schema = graphene.Schema(query=Query, mutation = Mutation)



# # https://www.youtube.com/watch?v=GnaCVdGFTDI&ab_channel=PythonIndia