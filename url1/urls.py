from django.urls import path , re_path 
from . import views

urlpatterns =[
    path("home/",views.home ,name='home'),  # Normal views
    path("",views.blog, name='blog'),
    path("blog/<int:blog_id>/",views.blog_detail,name='blog_detail'),
    re_path(r'^regular/$',views.aboutus),# regularexpression
    path('aboutus/<int:aboutusid>',views.aboutdetails), # dynamicview
    re_path(r"^add/(?P<a>[0-9]{1})/(?P<b>[0-9]{1})/$", views.add), 


    
]