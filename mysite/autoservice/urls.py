from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('uzsakymai/', views.UzsakymaiListView.as_view(), name="uzsakymai"),
    path('uzsakymai/<int:pk>', views.UzsakymaiDetailView.as_view(), name='uzsakymas'),
    path('automobiliai/', views.automobiliai, name="automobiliai"),
    path('automobiliai/<int:automobilis_id>', views.automobilis, name="automobilis"),
    path('search/', views.search, name = "search"),
]