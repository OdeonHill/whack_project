from website_code import create_app

app = create_app() # Create the Flask app instance

if __name__ == '__main__': # If this script is run directly, start the Flask app
    app.run(debug=True)
