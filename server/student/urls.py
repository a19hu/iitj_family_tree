from django.urls import path
from .views import ResolveAllTreeNodes

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('nodes/', ResolveAllTreeNodes.as_view(), name='nodes'),
]