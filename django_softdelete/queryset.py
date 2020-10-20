from django.db.models import QuerySet
from django.utils import timezone
from django_softdelete import filters


class SoftDeleteQuerySet(QuerySet):

    def __init__(self, *args, **kwargs):
        super(SoftDeleteQuerySet, self).__init__(*args, **kwargs)

    def delete(self):
        return super(SoftDeleteQuerySet, self).update(
            is_deleted=True,
            deleted_at=timezone.now()
        )

    def hard_delete(self):
        """
        Remove queryset permanently
        """
        return super(SoftDeleteQuerySet, self).delete()

    def restore(self):
        """
        Undo queryset soft deletion
        """
        return super(SoftDeleteQuerySet, self).update(
            is_deleted=False,
            deleted_at=None
        )

    def alive(self):
        """
        Get all available records except soft deleted
        :return:
        """
        return self.filter(filters)
