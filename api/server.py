from flask import Flask, request, jsonify

# Create a Flask application
app = Flask(__name__)

# Route to handle POST requests
@app.route('/submit', methods=['POST'])
def handle_post():
    # Check if the request has JSON data
    if request.is_json:
        # Get the JSON data from the request
        data = request.get_json()

        # Process the data (for example, extracting a specific value)
        name = data.get('name')
        age = data.get('age')

        # Do something with the data (here, just print it)
        print(f"Received: Name = {name}, Age = {age}")

        # Send a response back to the client
        return jsonify({"message": "Data received successfully", "data": data}), 200
    else:
        return jsonify({"error": "Request must be JSON"}), 400

@app.route('/hello', methods=['GET'])
def handle_get():
        return jsonify( "HELLO WORLD!"), 200



# Start the Flask web server
if __name__ == '__main__':
    app.run(debug=True)
