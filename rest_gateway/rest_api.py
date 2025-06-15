from fastapi import FastAPI
from pydantic import BaseModel

import client_grpc as client_grpc

app = FastAPI()

class ContactIn(BaseModel):
    name: str
    number: str
    type: int  # 0=MOBILE, 1=HOME, 2=WORK
    category: int  # 0=FAMILY, 1=PERSONAL, 2=BUSINESS


@app.post("/contacts/")
def create_contact(contact: ContactIn):
    """
    Create a new contact.
    This endpoint allows you to add a new contact with a name, phone number, type, and category.
    The phone type can be MOBILE (0), HOME (1), or WORK (2).
    The category can be FAMILY (0), PERSONAL (1), or BUSINESS (2).
    """
    msg = client_grpc.add_contact(contact.name, contact.number, contact.type, contact.category)
    return {"message": msg}

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