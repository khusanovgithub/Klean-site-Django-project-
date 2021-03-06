from django.urls import path
from .views import blog, blog_detail, index, about, service, project, contact, category

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('project/', project, name='project'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('blog_detail/<int:id>/', blog_detail, name='blog_detail'),
    path('category/<int:id>/', category, name='category'),
    path('project/', project, name='project')
]
