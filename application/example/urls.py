# example/urls.py
from django.urls import path, include
from example.views import (
    Index,
    Calendar,
    ProjectListView,
    Profile,
    CustomLoginView,
    SignupView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectDeleteView,
    ProjectUpdateView,
    create_tasklist,
    create_task,
    update_task_status,
    delete_task_list,
    update_task_list,
    delete_task,
    update_task,
    update_profile,
    tutorial,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", Index.as_view(), name="Index"),
    path("Calendar", Calendar.as_view(), name="Calendar"),
    path("Profile", Profile.as_view(), name="Profile"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("Project", ProjectListView.as_view(), name="Project"),
    path("Projects/<uuid:pk>/", ProjectDetailView.as_view(), name="project-detail"),
    path("Projects/create/", ProjectCreateView.as_view(), name="project-create"),
    path(
        "Projects/<uuid:pk>/update/", ProjectUpdateView.as_view(), name="project-update"
    ),
    path(
        "Projects/<uuid:pk>/delete/", ProjectDeleteView.as_view(), name="project-delete"
    ),
    path("create-tasklist/", create_tasklist, name="create-tasklist"),
    path("create-task/", create_task, name="create-task"),
    path("update_task_status/", update_task_status, name="update_task_status"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("delete_task_list/", delete_task_list, name="delete_task_list"),
    path("update_task_list/", update_task_list, name="update_task_list"),
    path("delete_task/", delete_task, name="delete_task"),
    path("update_task/", update_task, name="update_task"),
    path("update_profile/", update_profile, name="update_profile"),
    path('tutorial/', tutorial, name='tutorial'),
]
