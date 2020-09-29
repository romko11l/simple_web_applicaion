from django.urls import path

from .views import give_my_table, give_my_table_by_login, give_my_table_by_id


urlpatterns = [
    path('', give_my_table),
    path('by-login/', give_my_table_by_login),
    path('by-id/', give_my_table_by_id)
]
