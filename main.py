# Import 
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')

db = SQLAlchemy(app)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.Text, nullable=False)

@app.route('/feedback', methods=['POST'])
def feedback():
        email= request.form['email']
        comment = request.form['text']
        
        feedback_entry = Card(email=email, comment=comment)
        db.session.add(feedback_entry)
        db.session.commit()

        return redirect('/')


# Habilidades dinámicas
#python
@app.route('/', methods=['GET', 'POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')

    return render_template('index.html', 
                        button_python=button_python,
                        button_discord=button_discord,
                        button_html=button_html,
                        button_db=button_db)


if __name__ == "__main__":
    app.run(debug=True)
