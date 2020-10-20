from django.db import models
from django.utils import timezone

from django_softdelete.helpers import (
    handle_related_objects_soft_delete_cascade,
    handle_restore_soft_deleted_related_objects
)
from django_softdelete.mangers import SoftDeleteManager


class SoftDeleteModel(models.Model):
    """
     Soft delete mechanism base model
    """
    _soft_delete_cascade = False
    _restore_soft_deleted_related_objects = False

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = SoftDeleteManager()
    all_objects = SoftDeleteManager(with_trashed=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """
        Make an object as soft deleted
        """

        if self._soft_delete_cascade:
            handle_related_objects_soft_delete_cascade(self)

        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self):
        """
        Remove object permanently
        """
        super(SoftDeleteModel, self).delete()

    def restore(self):
        """
        Undo object soft deletion
        """
        if self._restore_soft_deleted_related_objects:
            handle_restore_soft_deleted_related_objects(self)

        assert self.is_deleted, (
                "%s object can't be restored because its not soft deleted." % self
        )

        self.is_deleted = False
        self.deleted_at = None
        self.save()
