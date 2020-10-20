from django_softdelete.utils import related_objects


def handle_related_objects_soft_delete_cascade(obj):
    """
    Helper function to perform soft deletion for all related objects
    """
    _objects = related_objects(obj)

    for _object in _objects:
        _object.delete()


def handle_restore_soft_deleted_related_objects(obj):
    """
    Helper function restore soft deleted related objects
    """
    _objects = related_objects(obj)

    for _object in _objects:
        _object.restore()