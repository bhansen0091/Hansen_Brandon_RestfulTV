from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new_show),
    path('shows/create', views.create_show),
    path('shows/<int:id>', views.show_view),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/update', views.update_show),
    path('shows/<int:show_id>/<int:net_id>/remove_network', views.show_remove_network),
    path('networks', views.view_networks),
    path('networks/create', views.create_network),
    path("shows/<int:id>/delete", views.delete_show),
    path("networks/<int:net_id>/delete", views.delete_network)
]