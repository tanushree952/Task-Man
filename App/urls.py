#from django.contrib import admin
from django.urls import path
from App.views import home , login , signup , add_todo , signout , delete_todo, change_todo,activity_log
from App import views

urlpatterns = [
   path('' , home , name='home' ), 
   path('login/' ,login  , name='login'), 
   path('signup/' , signup ), 
   path('add-todo/' , add_todo ), 
   path('delete-todo/<int:id>' , delete_todo ), 
   path('change-status/<int:id>/<str:status>' , change_todo ), 
   path('logout/' , signout ), 
   path('activity/',activity_log),
]