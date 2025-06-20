# 📞 gRPC Contacts API

## 📇 Overview

This project demonstrates a **gRPC-based Contacts Management System** built with Python and containerized using **Docker Compose**. It showcases how to expose a gRPC backend through multiple client-accessible interfaces—**gRPC**, **REST**, and **GraphQL**—via gateway services.

---

## 🧱 Architecture

The application is structured into four main services:

### 1. `grpc-server`

A Python-based gRPC server exposing core contact management methods:

* Add a contact
* Retrieve a contact
* List all contacts

### 2. `grpc-client`

A basic client that connects directly to the gRPC server to demonstrate method calls.

### 3. `rest_gateway`

A RESTful API that translates HTTP requests into gRPC calls.

> 💡 **Why?** gRPC is not natively supported in web browsers. REST acts as a bridge to enable browser and HTTP tool integration.

### 4. `graphQL_gateway`

A GraphQL API that converts GraphQL queries and mutations into gRPC calls.

> 💡 **Why?** GraphQL provides flexibility for frontend apps, allowing fine-grained control over requested data.

---

## 📆 Features

* Uses `proto3` to define the gRPC service and message schemas.
* Supports contact creation, retrieval, and listing.
* Uses `enum` types for phone categories and contact classifications.
* **GraphQL Gateway**

  * Flexible, field-specific queries and mutations.
  * Exposes enums as native GraphQL enums.
  * Ideal for rich frontend applications.
* **REST Gateway**

  * HTTP API for easy testing (e.g., `curl`, Postman).
  * Facilitates integration with services preferring REST.
* Fully containerized via Docker Compose.
* Internal service communication over Docker's network.

---

## 🗂️ Project Structure

```
grpc-app/
├── client/                  # gRPC client
│   ├── client.py            # Script to test gRPC methods
│   ├── client_grpc.py       # gRPC connection logic
│   └── random_info.py       # Random data generator for testing
├── server/                  # gRPC server
│   └── server.py
├── proto/                   # Protobuf definitions
│   └── contacts.proto
├── generated/               # Auto-generated gRPC Python files
│   ├── contacts_pb2.py
│   └── contacts_pb2_grpc.py
├── graphql_gateway/         # GraphQL Gateway
│   └── graphql_api.py
├── rest_gateway/            # REST Gateway
│   └── rest_api.py
├── Dockerfile.server        # gRPC server Dockerfile
├── Dockerfile.client        # Client Dockerfile
├── Dockerfile.rest          # REST gateway Dockerfile
├── Dockerfile.graphql       # GraphQL gateway Dockerfile
└── docker-compose.yml       # Multi-service orchestration
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

### 🛠️ Build & Run

Clone the repository and run the containers:

```bash
docker compose up --build
```

Services will be available on:

* gRPC Server: internal on port `50051`
* REST Gateway: `http://localhost:8000`
* GraphQL Gateway: `http://localhost:9000/graphql`

---

## 🧰 API Usage

### ✅ gRPC Methods

* `AddContact`: Adds a contact with name, phone(s), and category.
* `GetContact`: Retrieves a contact by name.
* `ListContacts`: Lists all registered contacts.

### 🌐 REST Endpoints

* `POST /contacts`: Add a contact.
* `GET /contacts/{name}`: Get contact by name.
* `GET /contacts`: List all contacts.

### 🔎 GraphQL Schema

```graphql
mutation {
  addContact(
    name: "Alice",
    phones: [{ number: "123456", type: MOBILE }],
    category: FAMILY
  )
}

query {
  getContact(name: "Alice") {
    name
    phones {
      number
      type
    }
    category
  }
}
```

---

## 📡 gRPC Interface (Proto)

Defined in `proto/contacts.proto`:

```proto
service ContactService {
  rpc AddContact (Contact) returns (AddContactResponse);
  rpc GetContact (ContactRequest) returns (Contact);
  rpc ListContacts (Empty) returns (ContactList);
}
```

---

## 🛠️ Tech Stack

* Python 3.10
* gRPC + Protobuf (proto3)
* FastAPI (REST)
* Strawberry GraphQL
* Docker & Docker Compose

---

## 📝 Notes

* `.proto` files are compiled at build time into Python gRPC stubs.
* Make sure `generated/__init__.py` exists so the folder is treated as a package.
* Enums are shared across gateways to maintain consistency.

---

## 🤝 Contributing

Fork the repo, add improvements (e.g., persistent storage, frontend UI), and feel free to open a PR!

---

## 📄 License

**MIT License** – Free to use, modify, and distribute with attribution.

---

### 📃 Documentation Credits

This documentation was created through collaboration between a human and an LLM 👩‍💻✨.
