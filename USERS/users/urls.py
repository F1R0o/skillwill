from django.urls import path
from .views import all_users, create_user, user_by_id,update_user,delete_by_id
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", all_users, name="ALLUSERS"),
    path("update/",all_users,name="ALLUPDATE"),
    path("delete/",all_users,name="ALLDELETE"),
    path("create/", create_user, name="CREATEUSER"),
    path("delete/<int:id>",delete_by_id,name="DELETEUSER"),
    path("update/<int:id>/", update_user, name="UPDATEID"),
    path("<int:id>/", user_by_id, name="USERBYID"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)