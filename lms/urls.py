from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonCreateView, LessonListView, LessonDetailView, LessonUpdateView, \
    LessonDeleteView


app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
urlpatterns = [
    path("lessons/create/", LessonCreateView.as_view(), name="create_lesson"),
    path("lessons/", LessonListView.as_view(), name="lessons"),
    path("lessons/<int:pk>/", LessonDetailView.as_view(), name="lesson"),
    path("lessons/<int:pk>/update/", LessonUpdateView.as_view(), name="update_lesson"),
    path("lessons/<int:pk>/delete/", LessonDeleteView.as_view(), name="delete_lesson"),

] + router.urls
