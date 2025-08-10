#  API (Application Programming Interface)

API stands for **Application Programming Interface**.  
It bridges communication between the **user interface** and the **server**.

---

## Types of APIs

### Based on Accessibility:
- Open API  
- Internal API  
- Partner API  
- Composite API  

### Based on Communication Style:
- REST API  
- SOAP API  
- GraphQL API  
- gRPC API  
- WebSocket API  

---

## Components of an HTTP Request

- **Method** → Defines the operation (GET, POST, PUT, DELETE, PATCH)  
- **Endpoint** → URL pointing to a resource on the server  
- **Body** → Data sent to the server (for POST/PUT/PATCH)  
- **Headers** → Metadata (key-value pairs) describing the request  

---

#  REST API

REST API is a widely used communication style.  
### **Constraints:**
- Client-Server Architecture  
- Resource-Based  
- Stateless  
- Cacheable  
- Uniform Interface  
- HATEOAS (Hypermedia as the Engine of Application State)  
- Layered System  

---

#  FastAPI

FastAPI is a **web framework** designed to build REST-styled applications.

**Key Features:**
- Uses **Pydantic** for data validation  
- Auto-generates API documentation  
- Supports asynchronous programming  

---

## Pydantic & BaseModel

`BaseModel` (from `pydantic`) is used for:
- Automatic Data Validation  
- Type Enforcement  
- Structured Schemas  
- Serialization & OpenAPI Integration  

### Example:
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    id: int
```
---

## Serialization

### Why is Serialization Needed?
- **Communication between systems** – Converts Python objects into a format that can be transmitted.  
- **JSON is universal** – Most APIs exchange data in JSON.  
- **FastAPI responses must be JSON** – Ensures compatibility with clients.  
- **Supports storage/caching** – Serialized data can be stored or cached efficiently.  

---

# Pytest

**Pytest** is a **testing framework** for Python, used for writing simple, scalable, and readable tests.

### Why Use Pytest?
- **Prevent regressions** – Detects bugs early.  
- **Speed up debugging** – Clear error output.  
- **Enable refactoring** – Safe code improvements.  
- **CI/CD Integration** – Automates testing in pipelines.  
- **Validate correctness** – Ensures application works as intended.  

# Function Decorators

**A Decorator Function** is used to wrap the extra functionality around the existing function without modifying its code

It takes another function as the input parameter into the Decorator Function, and returns the modified function


**The Communication always happens between the API and server, the server then communicates with the database
thisremoves the dependency of the tight coupling between the UI and Database**

# Uvicorn

**Uvicorn is an ASGI(Asynchronous Server Gateway Interface)
Uvicorn is an asynchronous server which does not wait for the response and sends the requests while not waiting for the response to return**

**Uvicorn** can run all the following ASGI web applications:
- FastAPI
- Starlette
- Django
- Quart
- Sanic
- Responder

# Path Parameters
**Path Parameters** are used in the API endpoint, these are passed dynamically into the endpoint, upon the user value,
the corresponding information is fetched on to the UI
Below are different path parameters
- Single Value path parameters
- Multiple Value path parameters
- Typed path parameters
- Path parameters with validation constraints
- Path parameter that capture the entire remaining path

**The difference between the path parameters and query parameters is, query parameters are used after the question
indicator to fetch the relavant information onto th UI**

For the path or query parameters to work we need to clearly define whether the route is path parameter route or quer route, the fastapi matches route exactly so, this is important when defining the query and path parameters



