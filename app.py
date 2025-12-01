"""
Simple Flask API for infrastructure testing.
"""
import os
import logging
from flask import Flask, jsonify, request
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['HOST'] = os.getenv('HOST', '0.0.0.0')
app.config['PORT'] = int(os.getenv('PORT', 5001))
app.config['DEBUG'] = os.getenv('DEBUG', 'False').lower() == 'true'


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@app.route('/api/requests', methods=['GET', 'POST'])
def requests():
    """Handle requests endpoint."""
    if request.method == 'GET':
        return jsonify({
            'method': 'GET',
            'message': 'Request received',
            'timestamp': datetime.utcnow().isoformat(),
            'headers': dict(request.headers)
        }), 200
    
    elif request.method == 'POST':
        try:
            data = request.get_json() if request.is_json else request.form.to_dict()
            return jsonify({
                'method': 'POST',
                'message': 'Request received',
                'timestamp': datetime.utcnow().isoformat(),
                'data': data,
                'headers': dict(request.headers)
            }), 201
        except Exception as e:
            logger.error(f"Error processing POST request: {str(e)}")
            return jsonify({
                'error': 'Failed to process request',
                'message': str(e)
            }), 400


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'error': 'Not found',
        'message': 'The requested resource was not found'
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({
        'error': 'Internal server error',
        'message': 'An unexpected error occurred'
    }), 500


if __name__ == '__main__':
    logger.info(f"Starting Flask app on {app.config['HOST']}:{app.config['PORT']}")
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )

