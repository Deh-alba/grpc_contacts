import grpc
import sys
sys.path.insert(0, "./generated")

from generated import contacts_pb2, contacts_pb2_grpc
from randon_info import randon_info


def run():
    channel = grpc.insecure_channel('grpc_server:50051')
    stub = contacts_pb2_grpc.ContactServiceStub(channel)

    # Call the class to generate random name and phone numbers
    randon_in = randon_info()

    
    # Add Contacts
    print("Adding contacts...")
    for i in range(10):
        name = randon_in.get_random_name()
        phone_number_mobile = randon_in.get_randon_phone_number()
        phone_number_work = randon_in.get_randon_phone_number()
        
        contato = contacts_pb2.Contact(
            name=name,
            phones=[
                contacts_pb2.PhoneNumber(number=phone_number_mobile, type=contacts_pb2.MOBILE),
                contacts_pb2.PhoneNumber(number=phone_number_work, type=contacts_pb2.WORK),
            ],
            category=contacts_pb2.PERSONAL
        )

        resp = stub.AddContact(contato)
        print(resp.message)


    # List All contacts
    all_contacts = stub.ListContacts(contacts_pb2.Empty())
    
    print("\n All contacts:")
    for c in all_contacts.contacts:
        print(f"- {c.name} ({c.category})")


    # Consult the last contact by name
    result = stub.GetContact(contacts_pb2.ContactRequest(name=c.name))

    if result is None or not result.name:
        print("Contact not found.")
        return
    else:
        print(f"Name: {result.name}, Category: {result.category}")
        for phone in result.phones:
            print(f"Phone: {phone.number}, Type: {phone.type}")


if __name__ == '__main__':
    run()
