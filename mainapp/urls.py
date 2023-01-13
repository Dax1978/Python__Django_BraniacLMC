from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    # path("", views.hello_world),
    # path("", views.HelloWorldView.as_view()),
    # path("<str:word>/", views.check_kwargs),
    path("", views.MainPageView.as_view(), name="main_page"),
    path("news/", views.NewsPageView.as_view(), name="news"),
    # path("news/<int:page>/", views.NewsWithPaginatorView.as_view(), name="news_paginator"),
    path("news/<int:pk>/", views.NewsPageDetailView.as_view(), name="news_detail"),
    # path("courses/", views.CoursesPageView.as_view(), name="courses"),
    path("courses/", views.CoursesListView.as_view(), name="courses"),
    path("courses/<int:pk>/", views.CoursesDetailView.as_view(), name="courses_detail"),
    path("contacts/", views.ContactsPageView.as_view(), name="contacts"),
    path("doc_site/", views.DocSitePageView.as_view(), name="doc_site"),
    # path("login/", views.LoginPageView.as_view(), name="login"),
]
