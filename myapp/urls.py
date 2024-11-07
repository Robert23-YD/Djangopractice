from django.urls import path
from myapp import views


urlpatterns=[
    path('',views.home,name='my_home'),
    path('About/',views.about,name='my_about'),
    path('Contact/',views.contact,name='my_contact'),
    path('services/',views.services,name='my_services'),
    path('blog/',views.blog,name='my_blog'),
    path('help/',views.help,name='my_help'),

]
