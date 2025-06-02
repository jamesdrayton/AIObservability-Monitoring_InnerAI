from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from .testing import testing
from .dependencies import get_query_token, get_token_header

app = FastAPI()    

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"Hello": "World"}
    
#app.include_router(testing.router, prefix="/testing", dependencies=[Depends(get_token_header)])

app.include_router(testing.router, prefix="/testing")