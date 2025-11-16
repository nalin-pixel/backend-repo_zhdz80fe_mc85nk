"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Example schemas (retain for reference)

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# SaaS lead capture schema for the storybook app
class Lead(BaseModel):
    """
    Leads collection schema
    Collection name: "lead"
    Stores marketing signups and inquiries from the website
    """
    parent_name: str = Field(..., description="Parent full name")
    email: EmailStr = Field(..., description="Contact email")
    child_name: Optional[str] = Field(None, description="Child's first name")
    child_age: Optional[int] = Field(None, ge=0, le=18, description="Child's age")
    interest: Optional[str] = Field(
        None,
        description="Primary interest (e.g., Waitlist, Demo, Early Access, Educator)"
    )
    message: Optional[str] = Field(None, description="Optional message")
    source: Optional[str] = Field("website", description="Acquisition source tag")
