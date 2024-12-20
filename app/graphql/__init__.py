# app/graphql/__init__.py
from app.graphql.queries import Query
from app.graphql.mutations import Mutation
from app.graphql.schemas import (
    UserModel,
    RoleModel,
    UserProfileModel,
    PostModel,
    CommentModel,
    MediaModel,
)
import graphene

# Define the main GraphQL schema
schema = graphene.Schema(query=Query, mutation=Mutation)
# Export the models for use in the schema and GraphQL schema
__all__ = [
    "schema",
    "UserModel",
    "RoleModel",
    "UserProfileModel",
    "PostModel",
    "CommentModel",
    "MediaModel",
]
