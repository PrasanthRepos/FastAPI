from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from typing import Union
app=FastAPI()


@app.get("/shipment/{id}")
def Get_Shipment(id:int)->dict[str,Union[int,str]]:
    return {
        "id":id,
        "Status":"delivered",
        "ShipmentId":458
    }

@app.get("/")
def get_root_message():
    return{
        "Hello, Welcome to the Base Url"
    }

@app.get("/scalar",include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
