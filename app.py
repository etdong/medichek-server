"""
Flask server for medichek-server
"""
from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)

# Enable CORS for all origins (development mode)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['DEBUG'] = True


@app.route('/api/health/', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "ok",
        "service": "medichek-server"
    })


@app.route('/api/analysis/submit/', methods=['POST'])
def receive_data():
    """Receive JSON data from client."""
    try:
        data = request.get_json()
        
        if data is None:
            return jsonify({
                "status": "error",
                "message": "No JSON data received"
            }), 400
        
        # Process the received data here
        # For now, just echo it back with a success message
        return jsonify({
            "status": "success",
            "message": "Data received successfully",
            "received_data": data
        }), 200
        
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        "status": "error",
        "message": "Endpoint not found"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500


if __name__ == '__main__':
    # Run the Flask development server
    app.run(
        host='127.0.0.1',
        port=8000,
        debug=True
    )
