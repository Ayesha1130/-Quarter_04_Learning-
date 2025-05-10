from pydantic import BaseModel, EmailStr, field_validator, ValidationError
from typing import List

# Define the Address class as a Pydantic model
class Address(BaseModel):
    street: str  # Street address as a string
    city: str    # City as a string
    zip_code: str  # Zip code as a string

# Define the UserWithAddress class that includes user details and a list of addresses
class UserWithAddress(BaseModel):
    id: int  # User ID as an integer
    name: str  # User name as a string
    email: EmailStr  # User email must be a valid email string
    addresses: List[Address]  # List of Address objects for the user's addresses
    
    # Validator for the 'name' field to ensure it is at least 2 characters long
    @field_validator("name")
    def name_must_be_at_least_two_chars(cls, v):
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")  # Raise error if name is too short
        return v

# Test with invalid data where the name is too short (only one character)
try:
    invalid_user = UserWithAddress(
        id=3,
        name="A",  # Name is too short (less than 2 characters)
        email="charlie@example.com",  # Valid email
        addresses=[  # One address for the user
            {
                "street": "789 Pine Rd",  # Address street
                "city": "Chicago",  # Address city
                "zip_code": "60601"  # Address zip code
            }
        ], 
    )
except ValidationError as e:
    print(e)  # Catch validation error and print it if occurs
