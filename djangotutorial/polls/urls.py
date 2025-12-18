from django.urls import path

from . import views

#app names are to used to tell django this url is called 
# from the details view in the polls app html template
#we will have many apps in the future
app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/      ## the 'name' value as called by the {% url %} template tag
    path("<int:question_id>/", views.detail, name="detail"),
    # If you want to change the URL of the polls detail view to something else, 
    # you can change the name attribute of the path() call. like polls/specifics/12/
    #path("specifics/<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]