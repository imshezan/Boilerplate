from django.db import models
from django.urls import reverse
import uuid
import datetime
import os

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files import File


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
    




    

    # #for compress images
    # def save(self, *args, **kwargs):
    #    # call the compress function
    #     new_image = compress(self.photo)
    #     # set self.image to new_image
    #     self.photo = new_image
    #     # save
    #     super().save(*args, **kwargs)
    # def __str__(self):
    #     return self.title
    
    # def get_thumbnail(self):
    #     if self.thumbnail:
    #         return self.thumbnail.url
    #     else:
    #         if self.image:
    #             self.thumbnail = self.make_thumbnail(self.image)
    #             self.save()
    #             return self.thumbnail.url
            
    #         else:
    #             # Default Image
    #             return 'default.jpg'
    
    # # Generating Thumbnail - Thumbnail is created when get_thumbnail is called
    # def make_thumbnail(self, image, size=(300, 200)):
    #     img = Image.open(image)
    #     img.convert('RGB')
    #     img.thumbnail(size)

    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'JPEG', quality=85)

    #     thumbnail = File(thumb_io, name=image.name)

    #     return thumbnail