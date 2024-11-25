from rest_framework.routers import DefaultRouter

from author.views import AuthorViewSet

router = DefaultRouter()
router.register("authors", AuthorViewSet, basename="manage")

urlpatterns = router.urls

app_name = "author"
