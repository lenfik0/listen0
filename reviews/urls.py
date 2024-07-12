from django.urls import path
from reviews.views import reviews


urlpatterns = [
    path('', reviews, name= 'review'),
    
     

]