from private import PLAID_CLIENT_ID, PLAID_SECRET, PLAID_ENV
from plaid.api import plaid_api
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.country_code import CountryCode
from plaid.model.products import Products
from plaid import Configuration, ApiClient


# Configure client
configuration = Configuration(
    host="https://sandbox.plaid.com",
    api_key={
        'clientId': PLAID_CLIENT_ID,
        'secret': PLAID_SECRET,
    }
)
api_client = ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

# Create the request
request = LinkTokenCreateRequest(
    user=LinkTokenCreateRequestUser(client_user_id='user-id-1234'),
    client_name='My Budget App',
    products=[Products("transactions"), Products("investments")],  # ✅ fixed here
    country_codes=[CountryCode("US")],
    language="en"
)

# Send request
response = client.link_token_create(request)
print("✅ Link token:", response["link_token"])
