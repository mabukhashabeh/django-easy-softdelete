from django.db.models import Q

filters = Q(is_deleted=False, deleted_at__isnull=True)
