from django.urls import path, include

app_name = 'blog'

urlpatterns = [
    path('v1/', include('app.blog.v1.urls'))
]
