from pydantic import BaseModel, Field

class SignupForm(BaseModel):
    username: str = Field(..., description="Username (at least 5 characters)")
    email: str = Field(..., description="Email address")
    age: int = Field(..., description="Age (must be a positive integer)")


# Example Usage
form_data = {
    "username": "john_doe",
    "email": "john@example.com",
    "age": 30
}


try:
    validated_form = SignupForm(**form_data)
    print("Form data is valid!")
    print(validated_form)
except ValueError as e:
    print("Form validation error:")
    print(e)
