import grpc

import sys
sys.path.insert(0, "./generated")

from generated import contacts_pb2, contacts_pb2_grpc

channel = grpc.insecure_channel("grpc_server:50051")
stub = contacts_pb2_grpc.ContactServiceStub(channel)

def add_contact(name, number, type, category):
    contact = contacts_pb2.Contact(
        name=name,
        phones=[contacts_pb2.PhoneNumber(number=number, type=type)],
        category=category
    )
    response = stub.AddContact(contact)
    return response.message


def get_contact(name):
    request = contacts_pb2.ContactRequest(name=name)
    try:
        response = stub.GetContact(request)
        return response
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.NOT_FOUND:
            return None
        else:
            raise e
        
def list_contacts():
    response = stub.ListContacts(contacts_pb2.Empty())
    return response.contacts