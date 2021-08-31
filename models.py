# https://github.com/graphql-python/graphene-mongo

from mongoengine import Document
from mongoengine.fields import StringField

class User(Document):
    meta = {'collection': 'user'}
    first_name = StringField(required=True)
    last_name = StringField(required=True)

import graphene

from graphene_mongo import MongoengineObjectType

from .models import User as UserModel

class User(MongoengineObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = graphene.List(User)
    
    def resolve_users(self, info):
    	return list(UserModel.objects.all())

schema = graphene.Schema(query=Query)

query = '''
    query {
        users {
            firstName,
            lastName
        }
    }
'''
result = schema.execute(query)
