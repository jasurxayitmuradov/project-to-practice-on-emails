from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/contactme')
def contactme():
    return render_template('contactme.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['POST'])
def contact():
    message = request.form.get('message')
    print(message)
    return f"Your message was received: {message}"

if __name__ == '__main__':
    app.run(debug=True)