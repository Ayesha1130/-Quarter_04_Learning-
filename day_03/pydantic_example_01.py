from pydantic import BaseModel, ValidationError

# ----------------------------------------
# Define a simple model using Pydantic
# ----------------------------------------
class User(BaseModel):
    id: int               # Required field: must be an integer
    name: str             # Required field: must be a string
    email: str            # Required field: must be a string (email format not validated here)
    age: int | None = None  # Optional field: int or None, default is None

# ----------------------------------------
# Valid user data (dictionary)
# ----------------------------------------
user_data = {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "age": 25
}

# Create a User instance using the valid data
user = User(**user_data)

# Print the user object (uses model's __str__)
print(user)
# Output: id=1 name='Alice' email='alice@example.com' age=25

# Print as a dictionary
print(user.model_dump())
# Output: {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'age': 25}

# ----------------------------------------
# Invalid user data (will raise ValidationError)
# ----------------------------------------
try:
    # 'id' is not an integer here, which violates the schema
    invalid_user = User(id="not-an-int", name="Bob", email="bob@example.com")
except ValidationError as e:
    print("Validation error:")
    print(e)
