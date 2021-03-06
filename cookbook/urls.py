"""cookbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from graphene_django.views import GraphQLView

# from cookbook.schema import schema
from ingredients.views import PrivateGraphQLView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', PrivateGraphQLView.as_view(graphiql=True)),

    # Enable graphiQL in graphql endpoint, see more https://github.com/graphql/graphiql
    # url(r'^graphql', GraphQLView.as_view(graphiql=True)),
    # If we did not specify the target schema in the Django settings file as explained above, we can do so here using:
    # url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
]
