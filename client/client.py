import grpc
import sys
sys.path.insert(0, "./generated")

from generated import contacts_pb2, contacts_pb2_grpc

def run():
    channel = grpc.insecure_channel('grpc_server:50051')
    stub = contacts_pb2_grpc.ContactServiceStub(channel)

    contato = contacts_pb2.Contact(
        name="Alice",
        phones=[
            contacts_pb2.PhoneNumber(number="11999999999", type=contacts_pb2.MOBILE),
            contacts_pb2.PhoneNumber(number="1133334444", type=contacts_pb2.WORK),
        ],
        category=contacts_pb2.PERSONAL
    )

    # Adiciona contato
    resp = stub.AddContact(contato)
    print(resp.message)

    # Consulta
    result = stub.GetContact(contacts_pb2.ContactRequest(name="Alice"))
    print(f"Nome: {result.name}, Categoria: {result.category}")
    for phone in result.phones:
        print(f"Telefone: {phone.number}, Tipo: {phone.type}")

    # Lista todos
    all_contacts = stub.ListContacts(contacts_pb2.Empty())
    
    print("\nTodos os contatos:")
    for c in all_contacts.contacts:
        print(f"- {c.name} ({c.category})")

if __name__ == '__main__':
    run()
