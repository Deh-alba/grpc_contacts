# 📞 gRPC Contacts API

This project demonstrates a simple **gRPC-based Contacts management system** using Python. It is containerized with **Docker Compose**, splitting the application into two services:

- `grpc-server`: Exposes gRPC methods to manage contacts (add, retrieve, list).
- `grpc-client`: Connects to the server and calls the gRPC methods.

---

## 📆 Features

- Uses `proto3` to define service and messages.
- Supports contact creation, retrieval, and listing.
- Uses `enum` to manage phone types and categories.
- Separated into two Docker containers (client + server).
- Communication over gRPC via Docker internal network.

---

## 🗂️ Project Structure

```
grpc-app/
├── client/              # gRPC client (Python)
│   └── client.py
├── server/              # gRPC server (Python)
│   └── server.py
├── proto/               # .proto definitions
│   └── contacts.proto
├── generated/           # Auto-generated gRPC Python files
│   ├── contacts_pb2.py
│   └── contacts_pb2_grpc.py
├── Dockerfile.server    # Server container
├── Dockerfile.client    # Client container
└── docker-compose.yml   # Docker Compose config
```

---

## 🚀 Getting Started

### ✅ Prerequisites

- Docker
- Docker Compose

---

### 🛠️ Build & Run

Clone the repo and run:

```bash
docker compose up --build
```

- The server will start and listen on `50051`
- The client will connect and invoke gRPC methods

---

### 🧪 Example gRPC Methods

- `AddContact`: Adds a contact with name, phone(s), and category.
- `GetContact`: Retrieves a contact by name.
- `ListContacts`: Lists all registered contacts.

---

## 📡 gRPC Interface Overview

Defined in `proto/contacts.proto`:

```protobuf
service ContactService {
  rpc AddContact (Contact) returns (AddContactResponse);
  rpc GetContact (ContactRequest) returns (Contact);
  rpc ListContacts (Empty) returns (ContactList);
}
```

---

## 🛠️ Tech Stack

- Python 3.10
- gRPC / Protobuf
- Docker & Docker Compose

---

## 📝 Notes

- The `.proto` file is compiled inside both containers during image build.
- Files in `generated/` are copied automatically to avoid runtime issues.
- Make sure `generated/__init__.py` exists so Python treats it as a package.

---

## 🤝 Contributing

Feel free to fork and improve this project. Add REST gateway, persistent storage, or even a front-end!

---

## 📄 License

MIT – do whatever you want, just don't forget to credit.

