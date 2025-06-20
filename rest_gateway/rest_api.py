from fastapi import FastAPI
from pydantic import BaseModel
from typing import List


import client_grpc as client_grpc

app = FastAPI()

class PhoneNumberIn(BaseModel):
    number: str
    type: int  # 0=MOBILE, 1=HOME, 2=WORK

class ContactIn(BaseModel):
    name: str
    phones: List[PhoneNumberIn]
    category: int  # 0=FAMILY, 1=PERSONAL, 2=BUSINESS

@app.post("/contacts/")
def create_contact(contact: ContactIn):
    """
    Create a new contact with multiple phone numbers.
    """
    phone_proto_list = [
        client_grpc.contacts_pb2.PhoneNumber(number=p.number, type=p.type)
        for p in contact.phones
    ]

    msg = client_grpc.add_contact_proto(contact.name, phone_proto_list, contact.category)
    return {"message": msg.message}

@app.get("/contacts/{name}")
def read_contact(name: str):
    """
    Retrieve a contact by name.
    This endpoint allows you to get the details of a contact by providing their name.
    If the contact does not exist, it returns a message indicating that the contact was not found.
    """
    
    contact = client_grpc.get_contact(name)
    if contact is None:
        return {"message": "Contact not found"}
    return {
        "name": contact.name,
        "phones": [{"number": phone.number, "type": phone.type} for phone in contact.phones],
        "category": contact.category
    }

@app.get("/contacts/")
def list_all_contacts():
    """
    List all contacts.
    This endpoint retrieves all contacts stored in the system.
    It returns a list of contacts with their names, phone numbers, and categories.
    """
    
    contacts = client_grpc.list_contacts()
    return [
        {
            "name": contact.name,
            "phones": [{"number": phone.number, "type": phone.type} for phone in contact.phones],
            "category": contact.category
        } for contact in contacts
    ]