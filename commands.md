fastapi uvicorn sqlalchemy graphene graphene-sqlalchemy alembic psycopg2 black python-dotenv

alembic init alembic

docker-compose run app alembic revision --autogenerate -m "New Migration" 
docker-compose run app alembic upgrade head

mutation CreateNewPost{ createNewPost(title:"new title1", content:"new content") { ok } }

query{ allPosts{ title } }

query{ postById(postId:2){ id title content } }






Amazing tutorial.
If you're coming here in 2023, here's a couple of things you need to know.
1. graphql is no longer accessible through starlette, use from starlette_graphene3 import GraphQLApp
2. app.add_route is nolonger valid, use app.mount
3. to get the GUI, you'll need make_graphiql_handler() from starlette_graphene3.

Your imports should be: 
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

your route method should be:
app.mount("/graphql",GraphQLApp(schema=graphene.Schema(query=Query, mutation=PostMutations),on_get=make_graphiql_handler()))

Another note from my headbanging - you would also need the 3.x version of graphene-sqlalchemy by running pip install --pre "graphene-sqlalchemy" as the standard install gets version < 3.