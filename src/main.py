"""
This is a simple FastAPI application that exposes one endpoint: /hello

When someone visits /hello (in a browser or API client), it returns:
{
    "message": "Hello World!"
}

FastAPI is a framework for building APIs quickly & efficiently.
"""

# --- Import FastAPI class from fastapi package ---
from fastapi import FastAPI

# --- Create the FastAPI application ---
# This object will hold all endpoints and settings.
app = FastAPI(
    title="Example FastAPI App",
    description="A simple Hello World API for demonstration.",
    version="1.0.0",
)

# -----------------------------------------------------
# CREATE AN ENDPOINT
# -----------------------------------------------------
# An endpoint is a function that responds to a specific URL.
#
# The @app.get("/hello") decorator means:
# "When someone sends a GET request to /hello, call the function below."
#
# Example:
#   http://127.0.0.1:8000/hello
# -----------------------------------------------------

@app.get("/hello")
def hello_world():
    """
    This function runs when a user accesses /hello.
    It returns a JSON response containing a message.

    FastAPI automatically converts the returned dictionary into JSON.
    """
    return {"message": "Hello World! the endpoint was deployed successfully"}


# -----------------------------------------------------
# OPTIONAL: Root endpoint (main page)
# -----------------------------------------------------
@app.get("/")
def root():
    """
    A basic root endpoint, so visiting http://127.0.0.1:8000
    also returns something friendly.
    """
    return {"info": "Welcome! Try /hello for the Hello World endpoint.THIS IS A TEST ONLINE adwdawdaawdawd"}
