from django.urls import path
from . import views

app_name = "game"

urlpatterns = [
    path("", views.start_view, name="start"),
    path("panel/<int:panel_number>/", views.panel_detail, name="panel_detail"),
]