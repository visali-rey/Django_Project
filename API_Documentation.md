"""Create an account using this API"""

Endpoint: /server/accounts/
Description: Handles CRUD operations for accounts.

Method: POST
Request_Body = {
    "email": "user@example.com",
    "name": "Test Account",
    "website": "http://example.com"
}
Headers = "Content-Type: application/json"

Sample_Response = {
    "email": "user@example.com",
    "account_id": "14625f1d-b57d-462f-801c-112029a88595",
    "name": "Test Account",
    "app_secret_token": "58b250b7fbac414f9a091073011c54af",
    "website": "http://example.com"
}


"""Retrieve All Accounts"""

Method: GET
sample_response = [
    {
        "email": "user@example.com",
        "account_id": "14625f1d-b57d-462f-801c-112029a88596",
        "name": "Test Account_01",
        "app_secret_token": "auto-generated-token",
        "website": "http://example.com"
    },
{
        "email": "example@example.com",
        "account_id": "14625f1d-b57d-462f-801c-112029a88595",
        "name": "Test Account",
        "app_secret_token": "58b250b7fbac414f9a091073011c54af",
        "website": "http://example.com"
    }
]


"""Retrieve a Single Account"""
Method: GET
URL: /server/accounts/<id>/

"""Update an Account"""
Method: PUT
URL = "/server/accounts/<id>/"

"""Delete an Account"""
Method: DELETE
URL = "/server/accounts/<id>/"


"""Destination API"""
Endpoint: /server/destinations/
Description: Handles CRUD operations for destinations belonging to accounts.

"""Create a Destination"""

Method: POST
Request Body:
{
    "account": 1,
    "url": "http://webhook.site/your-webhook",
    "http_method": "POST",
    "headers": {
        "APP_ID": "1234APPID1234",
        "APP_SECRET": "secret-key",
        "ACTION": "user.update",
        "Content-Type": "application/json"
    }
}

Response:
{
    "id": 1,
    "account": 1,
    "url": "http://webhook.site/your-webhook",
    "http_method": "POST",
    "headers": {
        "APP_ID": "1234APPID1234",
        "APP_SECRET": "secret-key",
        "ACTION": "user.update",
        "Content-Type": "application/json"
    }
}

Retrieve Destinations for an Account
Method: GET
URL: /server/accounts/<account_id>/destinations/
response = [
  {
    "id": 1,
    "account_id": 1,
    "url": "https://webhook.example.com",
    "http_method": "POST",
    "headers": {
      "APP_ID": "1234APPID1234",
      "APP_SECRET": "some-secret-token",
      "ACTION": "user.update",
      "Content-Type": "application/json"
    }
  }
]

Update a Destination
Method: PUT
URL: /server/destinations/<id>/
Request_Body:
{
  "url": "https://new-webhook.example.com",
  "http_method": "PUT",
  "headers": {
    "APP_ID": "updated-id",
    "APP_SECRET": "updated-secret-token",
    "ACTION": "user.modify",
    "Content-Type": "application/json"
  }
}

Response: 
{
  "id": 1,
  "account_id": 1,
  "url": "https://new-webhook.example.com",
  "http_method": "PUT",
  "headers": {
    "APP_ID": "updated-id",
    "APP_SECRET": "updated-secret-token",
    "ACTION": "user.modify",
    "Content-Type": "application/json"
  }
}

Delete a Destination
Method: DELETE
URL: /server/destinations/<id>/
Response:
{
  "message": "Destination deleted successfully"
}


"""Incoming Data API"""

Endpoint: /server/incoming_data/
Description: Receives data from external sources and pushes it to the destinations associated with the identified account.

Post Incoming Data
Method: POST
Headers: Content-Type: application/json
         CL-X-TOKEN: <app_secret_token>

Request Body:
{
  "user_id": 12345,
  "status": "active"
}

response: {
  "message": "Data successfully pushed to all destinations"
}

Error Responses:
Token is missing: 
{
  "message": "Un Authenticate"
}

HTTP method is GET and the data is not JSON:
{
  "message": "Invalid Data"
}









