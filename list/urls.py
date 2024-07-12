from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from list.views import ProductDetailView

urlpatterns = [
    path("<pk>",ProductDetailView.as_view(),name="product_detail"),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)