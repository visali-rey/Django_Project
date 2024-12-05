from django.urls import path
from .views import AccountView, DestinationView, IncomingDataView

urlpatterns = [
    path('accounts/', AccountView.as_view()),
    path('destinations/', DestinationView.as_view()),
    path('incoming_data/', IncomingDataView.as_view()),
]
