import grpc
from concurrent import futures
import sys
sys.path.insert(0, "./generated")

from generated import contacts_pb2, contacts_pb2_grpc




# Banco de dados em memória
contacts_db = {}

class ContactServiceServicer(contacts_pb2_grpc.ContactServiceServicer):
    def AddContact(self, request, context):
        contacts_db[request.name] = request
        return contacts_pb2.AddContactResponse(message=f"Contact '{request.name}' add with sucess.")

    def GetContact(self, request, context):
        contact = contacts_db.get(request.name)
        if not contact:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Contact not found.")
            return contacts_pb2.Contact()
        return contact

    def ListContacts(self, request, context):
        return contacts_pb2.ContactList(contacts=list(contacts_db.values()))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    contacts_pb2_grpc.add_ContactServiceServicer_to_server(ContactServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server gRPC running in port 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
