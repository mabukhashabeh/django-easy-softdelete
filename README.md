Django Easy Soft Delete
=======================


Goals
------------

The Default behavior for Django model instances delete action is
permanently delete a resource, means to remove the resource from the database completely with no option for recovery.

Some users want a “recycling bin” or “archival” feature which allows segregating active objects from non-active ones, and soft-deletion is one way of accomplishing this. The capability to delete and restore data needs to be available. That's what django-easy-softdelete package offer.

Description
------------

Using Django Easy Soft Delete package when model instances are soft deleted(default behavior), they are not actually removed from your database. Instead, a is_deleted flag and deleted_at attributes are set on the model and inserted into the database.
If a model has a non-null is_deleted and deleted_at values, the model instance has been soft deleted


This package gives Django model instances the ability to be soft-deleted(masked or hidden), and it gives the ability to restore any soft-deleted object,
And obviously it gives the ability to be normally deleted (hard delete)

You have to take into consideration the following:
- When the object hard deleted, that would delete all related objects.
- You can't use it as is for many-to-many relation, obviously.
- You could use soft-delete-cascade, restore and restore-related-objects correctly using model instance.


Example
-------

.. code-block:: python

    # imports
    from django_softdelete.models import SoftDeleteModel
    from django.utils import timezone

    # models
    class Author(SoftDeleteModel):
        _soft_delete_cascade = True
        _restore_soft_deleted_related_objects = True

        name = models.CharField(max_length=50)

    class Profile(SoftDeleteModel):
        author = models.OneToOneField(Author, on_delete=models.CASCADE)
        publish_books = PositiveIntegerField(default=0)

    class Book(SoftDeleteModel):
        author = models.ForeignKey(Author, on_delete=models.CASCADE)
        publish_date = models.DateField()


    # Example of use
    >>> author = Author(name='mohammad')
    >>> author.save()

    >>> book = Book(author=author, publish_date=timezone.now())
    >>> book.save()

    >>> profile = Profile(author=author, publish_books=+1)
    >>> profile.save()
    
    # If you would single-level soft deletion you could inherit SoftDeleteModel without override _soft_delete_cascade.
    
    # as we set _soft_delete_cascade=True then any objects related to author beside the author object will be soft-deleted.
    >>> author.delete()
    
    # once you have run delete() method is_deleted flag will set True and deleted_at will set the current datetime
    
    # all objects will be hidden
    >>> Author.objects.count() //0
    >>> Profile.objects.count() //0
    >>> Book.objects.count() //0
    
    # If you would get soft-deleted objects, you could use all_objects manager
    >>> Author.all_objects.count() //1
    >>> Profile.all_objects.count() //1
    >>> Book.all_objects.count() //1
    
    # You could inquire about non soft-deleted objects
    >>> Author.objects.all().alive()
  
    
    # Author object will be soft-deleted only
    >>> Author.objects.filter(id=author.id).delete()
    
    # List of author objects will be soft-deleted
    >> Author = objects.filter(id__in=[id's]).delete()
    
     # as we set _restore_soft_deleted_related_objects=True then any objects related 
     to author beside the author object will be restored.
     >>> author = Author.all_objects.get(id=1)
     >>> author.restore()
    
    # once you have run restore() method is_deleted flag will set False and deleted_at will set null
   

    # This will be hard deleted from the database.
    >>> author.hard_delete()




Installation
------------

Installing from pypi (using pip). ::

    pip install django-easy-softdelete


Installing from github. ::

    pip install -e https://github.com/mabukhashabeh/djagno-softdelete.git#egg=django-softdelete


The application doesn't have any special requirement or configurations.



Licensing
---------

Please see the LICENSE file.

Contacts
--------

Email: abukhashabehmohammad@gmail.com

GitHub: https://github.com/mabukhashabeh/

