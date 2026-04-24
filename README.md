# Flask API - Infrastructure Test

A simple Flask API for infrastructure testing with health check and request handling endpoints.

## Endpoints

### `GET /health`

Health check endpoint that returns the API status.

**Response:**

```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00.000000"
}
```

### `GET /api/requests`

Handle GET requests and return request information.

**Response:**

```json
{
  "method": "GET",
  "message": "Request received",
  "timestamp": "2024-01-01T12:00:00.000000",
  "headers": {...}
}
```

### `POST /api/requests`

Handle POST requests and return request data.

**Request Body:** JSON or form data

**Response:**

```json
{
  "method": "POST",
  "message": "Request received",
  "timestamp": "2024-01-01T12:00:00.000000",
  "data": {...},
  "headers": {...}
}
```

## Installation

1. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Locally

### Development Mode

```bash
python app.py
```

The API will be available at `http://localhost:5002`

### Production Mode (using Gunicorn)

```bash
gunicorn -w 4 -b 0.0.0.0:5002 app:app
```

## Environment Variables

- `HOST`: Server host (default: `0.0.0.0`)
- `PORT`: Server port (default: `5002`)
- `DEBUG`: Enable debug mode (default: `False`)

## Production Deployment

For production deployment, use Gunicorn as the WSGI server:

```bash
gunicorn -w 4 -b 0.0.0.0:${PORT:-5002} app:app
```

The number of workers (`-w 4`) can be adjusted based on your server's CPU cores (typically 2-4x CPU cores).

## Testing

Test the endpoints using curl:

```bash
# Health check
curl http://localhost:5002/health

# GET request
curl http://localhost:5002/api/requests

# POST request
curl -X POST http://localhost:5002/api/requests \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```
