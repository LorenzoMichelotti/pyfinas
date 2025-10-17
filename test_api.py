"""
Simple tests for the PyFinas Flask API
Run with: python test_api.py (requires the Flask server to be running)
"""

import requests
import json


def test_home_endpoint():
    """Test the home endpoint"""
    response = requests.get('http://localhost:5000/')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'PyFinas API'
    assert 'endpoints' in data
    print("✓ Home endpoint test passed")


def test_health_endpoint():
    """Test the health endpoint"""
    response = requests.get('http://localhost:5000/health')
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'healthy'
    assert 'timestamp' in data
    print("✓ Health endpoint test passed")


def test_status_endpoint():
    """Test the status endpoint"""
    response = requests.get('http://localhost:5000/api/status')
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'running'
    assert 'timestamp' in data
    print("✓ Status endpoint test passed")


def test_time_endpoint():
    """Test the time endpoint"""
    response = requests.get('http://localhost:5000/api/time')
    assert response.status_code == 200
    data = response.json()
    assert 'utc_time' in data
    assert 'timestamp' in data
    print("✓ Time endpoint test passed")


def test_echo_endpoint_valid():
    """Test the echo endpoint with valid JSON"""
    test_data = {'message': 'Hello, World!', 'test': True}
    response = requests.post(
        'http://localhost:5000/api/echo',
        json=test_data
    )
    assert response.status_code == 200
    data = response.json()
    assert data['received'] == test_data
    assert 'timestamp' in data
    print("✓ Echo endpoint (valid) test passed")


def test_echo_endpoint_invalid():
    """Test the echo endpoint with invalid JSON"""
    response = requests.post(
        'http://localhost:5000/api/echo',
        data='not json',
        headers={'Content-Type': 'application/json'}
    )
    assert response.status_code == 400
    data = response.json()
    assert data['error'] == 'Bad request'
    print("✓ Echo endpoint (invalid JSON) test passed")


def test_404_error():
    """Test 404 error handling"""
    response = requests.get('http://localhost:5000/nonexistent')
    assert response.status_code == 404
    data = response.json()
    assert data['error'] == 'Not found'
    print("✓ 404 error handling test passed")


if __name__ == '__main__':
    print("Running PyFinas API tests...")
    print("Note: Make sure the Flask server is running on http://localhost:5000")
    print()
    
    try:
        test_home_endpoint()
        test_health_endpoint()
        test_status_endpoint()
        test_time_endpoint()
        test_echo_endpoint_valid()
        test_echo_endpoint_invalid()
        test_404_error()
        
        print()
        print("All tests passed! ✓")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to Flask server at http://localhost:5000")
        print("Please start the server with: python app.py")
    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
