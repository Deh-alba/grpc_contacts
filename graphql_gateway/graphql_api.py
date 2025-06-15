import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI

import client_grpc

@strawberry.type
class PhoneNumber:
    number: str
    type: int

@strawberry.type
class Contact:
    name: str
    phones: list[PhoneNumber]
    category: int

@strawberry.type
class Query:
    @strawberry.field
    def get_contact(self, name: str) -> Contact:
        c = client_grpc.get_contact(name)
        return Contact(name=c.name, phones=c.phones, category=c.category)

    @strawberry.field
    def list_contacts(self) -> list[Contact]:
        resp = client_grpc.list_contacts()
        return [Contact(name=c.name, phones=c.phones, category=c.category) for c in resp.contacts]

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_contact(self, name: str, number: str, type: int, category: int) -> str:
        resp = client_grpc.add_contact(name, number, type, category)
        return resp.message

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")
