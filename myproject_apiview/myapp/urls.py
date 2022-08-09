from django.urls import path
from .views import AddRetrieve,UpdateDelete

urlpatterns = [
    path('addretrive/',AddRetrieve),
    path('updatedelete/<int:id>',UpdateDelete)
]