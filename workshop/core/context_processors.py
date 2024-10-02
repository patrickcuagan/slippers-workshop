from django.conf import settings

from workshop.core.models import Tracking


def global_vars(request):
    tracking = Tracking.for_request(request)
    return {
        "GOOGLE_TAG_MANAGER_ID": getattr(tracking, "google_tag_manager_id", None),
        "SEO_NOINDEX": settings.SEO_NOINDEX,
        "LANGUAGE_CODE": settings.LANGUAGE_CODE,
    }
