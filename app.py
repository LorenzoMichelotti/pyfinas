"""
PyFinas - Flask API Application
A simple Flask-based REST API
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Configuration
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def home():
    """Home endpoint - API information"""
    return jsonify({
        'name': 'PyFinas API',
        'version': '1.0.0',
        'description': 'A Flask-based REST API',
        'endpoints': {
            '/': 'API information',
            '/health': 'Health check',
            '/api/status': 'API status',
            '/api/time': 'Current server time',
            '/api/echo': 'Echo service (POST)'
        }
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    })


@app.route('/api/status')
def status():
    """API status endpoint"""
    return jsonify({
        'status': 'running',
        'uptime': 'operational',
        'timestamp': datetime.utcnow().isoformat()
    })


@app.route('/api/time')
def get_time():
    """Get current server time"""
    return jsonify({
        'utc_time': datetime.utcnow().isoformat(),
        'timestamp': datetime.utcnow().timestamp()
    })


@app.route('/api/echo', methods=['POST'])
def echo():
    """Echo service - returns the posted data"""
    data = request.get_json()
    return jsonify({
        'received': data,
        'timestamp': datetime.utcnow().isoformat()
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Not found',
        'message': 'The requested resource was not found',
        'status': 404
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'message': 'An internal server error occurred',
        'status': 500
    }), 500


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
