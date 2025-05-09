from pydantic import BaseModel, EmailStr

# ----------------------------------------
# Define a nested model for Address
# ----------------------------------------
class Address(BaseModel):
    street: str           # Street name
    city: str             # City name
    zip_code: str         # ZIP/postal code

# ----------------------------------------
# Define a User model with nested addresses
# ----------------------------------------
class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr       # Automatically validates email format
    addresses: list[Address]  # List of Address models

# ----------------------------------------
# Valid data with nested structure
# ----------------------------------------
user_data = {
    "id": 2,
    "name": "Ayesha",
    "email": "Ayesha@example.com",
    "addresses": [
        {
            "street": "123 Main St",
            "city": "Karachi",
            "zip_code": "10001"
        },
        {
            "street": "456 Oak Ave",
            "city": "Los Angeles",
            "zip_code": "90001"
        },
    ],
}

# Validate and create the model instance using .model_validate() (Pydantic v2)
user = UserWithAddress.model_validate(user_data)

# Print the model as a dictionary
print(user.model_dump())
# Output:
# {
#     'id': 2,
#     'name': 'Ayesha',
#     'email': 'Ayesha@example.com',
#     'addresses': [
#         {'street': '123 Main St', 'city': 'Karachi, 'zip_code': '10001'},
#         {'street': '456 Oak Ave', 'city': 'Los Angeles', 'zip_code': '90001'}
#     ]
# }
