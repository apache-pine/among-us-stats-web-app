from django.urls import path
from . import views
from .views import insert_match, insert_match_results

urlpatterns = [
    path('main/', views.main),
    path('insert/', views.insert),
    path('query/', views.query),
    path('main/pmw/', views.main_pmw),
    path('main/pml/', views.main_pml),
    path('main/pmk/', views.main_pmk),
    path('main/pmd/', views.main_pmd),
    path('main/rmw/', views.main_rmw),
    path('main/rml/', views.main_rml),
    path('main/rmk/', views.main_rmk),
    path('main/rmd/', views.main_rmd),
    path('insert/match/', views.insert_match),
    path('insert/match_results/', views.insert_match_results),
    path('insert_match/', insert_match, name='insert_match'),
    path('insert_match_results/', insert_match_results,
         name='insert_match_results'),
]
