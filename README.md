# PyFinas

A simple Flask-based REST API.

## Features

- RESTful API endpoints
- Health check endpoint
- CORS support
- Error handling
- Environment-based configuration

## Installation

1. Clone the repository:
```bash
git clone https://github.com/LorenzoMichelotti/pyfinas.git
cd pyfinas
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

Copy `.env.example` to `.env` and adjust the settings:
```bash
cp .env.example .env
```

Environment variables:
- `PORT`: Server port (default: 5000)
- `DEBUG`: Debug mode (default: False)

## Running the API

Start the Flask development server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### GET `/`
Returns API information and available endpoints.

**Response:**
```json
{
  "name": "PyFinas API",
  "version": "1.0.0",
  "description": "A Flask-based REST API",
  "endpoints": { ... }
}
```

### GET `/health`
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-10-17T22:19:10.123456"
}
```

### GET `/api/status`
API status endpoint.

**Response:**
```json
{
  "status": "running",
  "uptime": "operational",
  "timestamp": "2025-10-17T22:19:10.123456"
}
```

### GET `/api/time`
Get current server time.

**Response:**
```json
{
  "utc_time": "2025-10-17T22:19:10.123456",
  "timestamp": 1697577550.123456
}
```

### POST `/api/echo`
Echo service - returns the posted data.

**Request:**
```json
{
  "message": "Hello, World!"
}
```

**Response:**
```json
{
  "received": {
    "message": "Hello, World!"
  },
  "timestamp": "2025-10-17T22:19:10.123456"
}
```

## Development

### Running in Debug Mode

Set the `DEBUG` environment variable:
```bash
DEBUG=true python app.py
```

Or use Flask's built-in development server:
```bash
flask --app app run --debug
```

## Testing

You can test the API using curl:

```bash
# Test home endpoint
curl http://localhost:5000/

# Test health endpoint
curl http://localhost:5000/health

# Test echo endpoint
curl -X POST http://localhost:5000/api/echo \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, World!"}'
```

## License

MIT License