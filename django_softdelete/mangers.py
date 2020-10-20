from django.db import models
from django_softdelete import filters
from django_softdelete.queryset import SoftDeleteQuerySet


class SoftDeleteManager(models.Manager):
    def __init__(self, with_trashed=False, *args, **kwargs):
        self.with_trashed = with_trashed
        super(SoftDeleteManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        queryset = SoftDeleteQuerySet(self.model)
        if not self.with_trashed:
            queryset = queryset.filter(filters)

        return queryset

    def hard_delete(self):
        return self.get_queryset().hard_delete()
