#The /search route: This route just displays a message about searching. You can use this to demonstrate URL parameters and query strings in your Selenium tutorial.

#The /search/results/<query> route: This route takes a query parameter from the URL and displays the search results. This can be used to illustrate how to handle dynamic data in web pages.

#The /form route: This route renders an HTML form and handles both GET and POST requests. It's used to show how to interact with forms on web pages. 
#To make this work, you'll need to create an HTML template for the form (e.g., form.html) and store it in a folder named templates in the same directory as your Flask application.
from flask import Flask, render_template, request

app = Flask(__name__)

# Define routes for different pages

@app.route('/')
def index():
    return 'Welcome to the Selenium Tutorial!'

@app.route('/search')
def search():
    return 'This is the search page. Enter a query in the URL.'

@app.route('/search/results/<query>')
def search_results(query):
    # This route takes a query parameter from the URL and displays it.
    return f'Search results for: {query}'

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Handle form submission and display the submitted data
        data = request.form
        return f'You submitted the form with data: {data}'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
