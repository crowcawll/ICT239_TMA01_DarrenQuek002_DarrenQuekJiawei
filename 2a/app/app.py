from flask import Flask, render_template, blueprints
app = Flask(__name__)

# Register Blueprint so we can factor routes
from controllers.bookTitleController import bookTitle

# register blueprint from respective module
app.register_blueprint(bookTitle)

@app.route('/base')
def show_base():
    return render_template('base.html')