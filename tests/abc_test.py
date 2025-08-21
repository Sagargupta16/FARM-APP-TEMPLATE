import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "message": "FARM App Template is running"}

def test_root_endpoint():
    """Test the root endpoint when client_build doesn't exist"""
    response = client.get("/")
    assert response.status_code == 200

def test_create_user():
    """Test creating a new user"""
    user_data = {
        "name": "Test User",
        "email": "test@example.com"
    }
    response = client.post("/api/v1/users", json=user_data)
    # Note: This test will fail without a running MongoDB instance
    # In a real scenario, you'd mock the database or use a test database

def test_get_users():
    """Test getting all users"""
    response = client.get("/api/v1/users")
    # Note: This test will fail without a running MongoDB instance
    # In a real scenario, you'd mock the database or use a test database

# Delete this file if you don't want to use it. Use *_test.py pattern to create new test files.

def test_abc():
    assert 1+1 == 2