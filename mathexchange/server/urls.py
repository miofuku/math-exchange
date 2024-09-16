
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
import debug_toolbar
from django.conf.urls.static import static
from mathexchange.forum.urls import forum_patterns
from mathexchange.accounts.views import image_upload_view
import mathexchange.accounts.urls as accounts_urls
from mathexchange.planet.urls import planet_patterns


urlpatterns = [

    # Include forum urls
    path(r'forum/', include(forum_patterns)),

    # Include planets urls
    path(r'planet/', include(planet_patterns)),

    # Include the accounts urls
    path(r'accounts/', include(accounts_urls)),

]

if settings.PAGEDOWN_IMAGE_UPLOAD_ENABLED:

    urlpatterns += [
        # Pagedown image upload url.
        path('pagedown/image-upload/', image_upload_view, name="pagedown-image-upload")
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
