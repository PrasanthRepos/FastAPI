from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from typing import Union
app=FastAPI()

shipments={
    458:{
        "weight":.8,
        "content":"cookware",
        "status":"placed"
    },
    459: {
    "weight": 1.2,
    "content": "cutlery",
    "status": "placed"
},
460: {
    "weight": 0.5,
    "content": "glassware",
    "status": "placed"
},
461: {
    "weight": 2.0,
    "content": "dinner set",
    "status": "placed"
},
462: {
    "weight": 1.5,
    "content": "bakeware",
    "status": "placed"
}

}


@app.get("/shipment/latest")
def Get_Latest_Shipment():
    latest_shipment_id=max(shipments.keys())

    return shipments[latest_shipment_id]
    

@app.get("/shipment/{id}")
def Get_Shipment(id:int)->dict[str,Union[int,str]]:
    if id not in shipments:
        return{
            "detail":"The given id data does not exist in the database"
        }
    return {
        shipments[id]
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
