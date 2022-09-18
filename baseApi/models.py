from django.db import models

from django.urls import reverse 
from .managers import CategoryManager, SubCategoryManager
# def get_upload_path(instance, filename):
#     return os.path.join('account/avatars/', now().date().strftime("%Y/%m/%d"), filename)

# class User(AbstractUser):
#     avatar = models.ImageField(blank=True, upload_to=get_upload_path)


# making node class for category and subcategory // Abstract class type 

class Node(models.Model):
    name = models.CharField(max_length = 150)
    parent = models.ForeignKey(
        'self', 
        on_delete = models.CASCADE,
        related_name = 'children',
        null = True,
        blank = True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering =  ('name',)
        verbose_name_plural = "Nodes"  

# proxy model for category
class Category(Node):
    objects = CategoryManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Categories"


# proxy model for subcategory
class SubCategory(Node):
    objects = SubCategoryManager()

    class Meta:
        proxy = True
        verbose_name_plural = "Sub categories"




# class categoryOld(models.Model):
#     title = models.CharField(max_length=100)
#     detail = models.CharField(max_length=500)
    
#     def __str__(self): 
#         return self.title

#     def get_absolute_url(self): 
#         return reverse("category_detail", args=[str(self.id)])

#     class Meta:
#        # ordering = ('title')
#         verbose_name = "Category old"
#         verbose_name_plural = "Categories old"

class Tag(models.Model):
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)
    
    def __str__(self): 
        return self.title

    def get_absolute_url(self): 
        return reverse("tag_detail", args=[str(self.id)])

    class Meta:
       # ordering = ('title')
        verbose_name = "Tag"
        verbose_name_plural = "Tags"



class Post(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
 #   categoryOld = models.ForeignKey(categoryOld, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    detail = models.CharField(max_length=1000, default = "")
    tags = models.ManyToManyField(to='Tag', related_name='posts', blank=True)

   # author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')
    
    def __str__(self): 
        return self.title

    def get_absolute_url(self): 
        return reverse("post_detail", args=[str(self.id)])

    class Meta:
       # ordering = ('title')
        verbose_name = "Post"
        verbose_name_plural = "Posts"


    # https://learndjango.com/tutorials/django-best-practices-models