# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views.generic import View

from django.shortcuts import get_object_or_404

from django.views.generic import TemplateView
# from datetime import datetime

from mainapp import models as mainapp_models

# Create your views here.

# def hello_world(request):
#     return HttpResponse("Hello world!")
# class HelloWorldView(View):
#     def get(self, *args):
#         return HttpResponse("Hello world!")

# def check_kwargs(request, **kwargs):
#     return HttpResponse(f"kwargs:<br>{kwargs}")


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        # context["news_title"] = "Громкий новостной заголовок"
        # context["news_preview"] = "Предварительное описание, которое заинтересует каждого"
        # context["range"] = range(5)
        # context["datetime_obj"] = datetime.now()
        context["news_qs"] = mainapp_models.News.objects.all()[:5]
        return context

# class NewsWithPaginatorView(NewsPageView):
#     def get_context_data(self, page, **kwargs):
#         context = super().get_context_data(page=page, **kwargs)
#         context["page_num"] = page
#         return context

class NewsPageDetailView(TemplateView):
    template_name = "mainapp/news_detail.html"
    
    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        context["news_object"] = get_object_or_404(mainapp_models.News, pk=pk)
        return context

# class CoursesPageView(TemplateView):
#     template_name = "mainapp/courses_list.html"
class CoursesListView(TemplateView):
    template_name = "mainapp/courses_list.html"

    def get_context_data(self, **kwargs):
        context = super(CoursesListView, self).get_context_data(**kwargs)
        context["objects"] = mainapp_models.Courses.objects.all()[:7]
        return context


class CoursesDetailView(TemplateView):
    template_name = "mainapp/courses_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(CoursesDetailView, self).get_context_data(**kwargs)
        context["course_object"] = get_object_or_404(mainapp_models.Courses, pk=pk)
        context["lessons"] = mainapp_models.Lesson.objects.filter(course=context["course_object"])
        context["teachers"] = mainapp_models.CourseTeachers.objects.filter(course=context["course_object"])
        return context


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


# class LoginPageView(TemplateView):
#     template_name = "mainapp/login.html"
