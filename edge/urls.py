"""edge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from edge import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',view.home),
    path('about/',view.about),
    path('blog/',view.blog),
    path('post/',view.posta),
    path('post1/',view.postb),
    path('post2/',view.postc),
    path('post3/',view.postd),
    path('course/',view.course),
    path('courseinner/',view.courseinner),
    path('courseinner1/',view.courseinner1),
    path('courseinner2/',view.courseinner2),
    path('courseinner3/',view.courseinner3),
    path('courseinner4/',view.courseinner4),
    path('courseinner5/',view.courseinner5),
    path('courseinner6/',view.courseinner6),
    path('courseinner7/',view.courseinner7),
    path('courseinner8/',view.courseinner8),
    path('courseinner9/',view.courseinner9),
    path('contact/',view.contact),
    path('enroll/',view.enroll),
    path('view/',view.view),
    path("delete/<int:s_id>",view.delete),
    path("update/<int:s_id>",view.update),
]
