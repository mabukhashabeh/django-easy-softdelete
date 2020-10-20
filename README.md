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
If a model has a non-null is_deleted and deleted_at values, the model instance has been soft deleted.


This package gives Django model instances the ability to be soft-deleted(masked or hidden), and it gives the ability to restore any soft-deleted objects,
...obviously it gives the ability to be normally deleted (hard delete)

You have to take into consideration the following:
- When the object hard deleted, that would delete all related objects.
- You can't use it as is for many-to-many relation, obviously.
- You could use soft-delete-cascade, restore and restore-related-objects correctly using model instance.


The only thing that you have to do to utilize the package functionalities is inheriting from django_softdelete.models.SoftDeleteModel

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
    
    >>> Author.objects.all().values()
    <SoftDeleteQuerySet [{'id': 1, 'is_deleted': False, 'deleted_at': None, 'name': 'mohammad'}]>

    
    # as we set _soft_delete_cascade=True then any objects related 
    to author beside the author object will be soft-deleted.
    >>> author.delete()
    
    # All objects will be soft-deleted
    >>> Author.objects.count() 
    0
    >>> Profile.objects.count()
    0
    >>> Book.objects.count()
    0
    
    # If you would get soft-deleted objects, you could use all_objects manager
    >>> Author.all_objects.count() 
    1
    >>> Profile.all_objects.count() 
    1
    >>> Book.all_objects.count() 
    1
    
    # Author object will be soft-deleted only
    >>> Author.objects.filter(id=author.id).delete()
        
    # List of author objects will be soft-deleted
    >>> Author.objects.filter(id__in=[1,]).delete()
    >>> Author.all_objects.all().values()
    <SoftDeleteQuerySet [{'id': 1, 'is_deleted': True, 'deleted_at': datetime.datetime(2020, 5, 20, 10, 51, 52, 50725, tzinfo=<UTC>), 'name': 'mohammad'}]>
    
    # You could inquire about non soft-deleted objects
    >>> Author.objects.all().alive().count()
    0
  
     # as we set _restore_soft_deleted_related_objects=True then any objects related 
     to author beside the author object will be restored.
     >>> author = Author.all_objects.get(id=1)
     >>> author.restore()
    
    >>> authors = Author.objects.all()
    >>> authors.values()
    <SoftDeleteQuerySet [{'id': 1, 'is_deleted': False, 'deleted_at': None, 'name': 'mohammad'}]>
    >>> authors
    <SoftDeleteQuerySet [<Author: Author object (1)>]>
    >>> author = authors.first()
    >>> author
    <Author: Author object (1)>
    >> author.book_set.first()
    <Book: Book object (1)>
    >> author.profile
    <Profile: Profile object (1)>   
 
    # This will be hard deleted from the database.
    >>> author.hard_delete()
    >>> Author.objects.all()
    <SoftDeleteQuerySet []>



Installation
------------

Installing from pypi (using pip). ::

    pip install django-easy-softdelete


The application doesn't have any special requirement or configurations.



Licensing
---------

Please see the LICENSE file.

Contacts
--------

Email: abukhashabehmohammad@gmail.com

GitHub: https://github.com/mabukhashabeh/

