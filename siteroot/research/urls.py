from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login', log_in, name='login'),
    path('logout', log_out, name='logout'),
    path('researchers', get_all_researchers, name='get_researchers'),
    path('researchers/<int:researcher_id>/', get_researcher, name='researcher_by_id'),
    path('posts/<int:post_id>/', get_post, name='post_by_id'),
    path('post_creation', create_post, name='create_post'),
    path('post_creation', render_creation_page, name='render_creation_page')
]
