from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
import graphene

from posts import models


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

#class AuthorType(DjangoObjectType):
  #  class Meta:
    #    model = models.Profile

class PostType(DjangoObjectType):
    class Meta:
        model = models.Post

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag




class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)


def resolve_all_posts(root, title):
        return (
            models.Post.objects.prefetch_related("title")
            .select_related("id")
            .all()
        )  


def resolve_posts_by_tag(root, info, title):
        return (
            models.Post.objects.prefetch_related("title")
            .select_related("id")
            .filter(tags__name__iexact=tag)
        )      



schema = graphene.Schema(query=Query)     