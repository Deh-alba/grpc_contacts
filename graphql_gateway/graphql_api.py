import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI

import client_grpc

@strawberry.type
class PhoneNumber:
    number: str
    type: int

@strawberry.input
class PhoneNumberInput:
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
        grpc_contacts = client_grpc.list_contacts()
        return [
            Contact(
                name=c.name,
                phones=[PhoneNumber(number=p.number, type=p.type) for p in c.phones],
                category=c.category
            )
            for c in grpc_contacts
        ]
    

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_contact(self, name: str, phones: list[PhoneNumberInput], category: int) -> str:
        # Montar lista de PhoneNumber protobuf a partir da lista de PhoneInput
        phone_proto_list = [
            client_grpc.contacts_pb2.PhoneNumber(number=p.number, type=p.type)
            for p in phones
        ]

        resp = client_grpc.add_contact_proto(name, phone_proto_list, category)
        return resp.message
    

    

schema = strawberry.Schema(query=Query, mutation=Mutation)

app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")
