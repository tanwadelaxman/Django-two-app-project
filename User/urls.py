from django.urls import path

from . import views

urlpatterns = [
    path("", views.index,name="UserHome"),
    path("post/<int:id>", views.post, name ="Post")
]