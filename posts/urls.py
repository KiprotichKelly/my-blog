from django.urls import path

from . import views
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    path('',views.index, name='index'),
    path('post/<str:pk>',views.post, name='post'),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True)))
]
