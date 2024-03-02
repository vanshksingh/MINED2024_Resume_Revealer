from flask import Blueprint, render_template, request, redirect, session
from database import get_db
from text_extractor import process_files
import os
from flask import request, jsonify
# Import your functions
from csv_generator import initialize_database, parse_resume_from_pdf, save_to_database

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')

@routes.route('/login', methods=['POST'])
def login():
    db = get_db()
    cursor = db.cursor()
    username = request.form['username']
    password = request.form['password']

    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    if user:
        session['username'] = username
        return redirect('/dashboard')
    else:
        return render_template('index.html', error="Invalid username or password.")

@routes.route('/signup', methods=['GET', 'POST'])
def signup():
    db = get_db()
    cursor = db.cursor()
    if request.method == 'GET':
        return render_template('signup.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        db.commit()

        session['username'] = username
        return redirect('/dashboard')

@routes.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect('/')

# Add more routes as needed
# Route for HR resume sorter page
@routes.route('/hr_resume_sorter')
def hr_resume_sorter():
    return render_template('hr_resume_sorter.html')

# Route for resume suggestor page
@routes.route('/resume_suggestor')
def resume_suggestor():
    return render_template('resume_suggestor.html')

@routes.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


@routes.route('/upload')
def upload_file():
    return render_template('upload.html')




@routes.route('/uploader', methods=['POST'])
def uploader():
    text_input = request.form.get('text_input')
    print("Text Input:", text_input)

    if 'files[]' not in request.files:
        return 'No file part'

    files = request.files.getlist('files[]')

    # Extract file data and filenames
    file_data = [(file.filename, file.read()) for file in files]

    extracted_texts = process_files(file_data)

    # Here you can return or process the extracted texts as needed
    # For now, let's just return them as a JSON response
    return jsonify(extracted_texts)






# Route to display the list of top 10 resumes
@routes.route('/top_resumes')
def top_resumes():
    # Retrieve top 10 resumes from the database (you need to implement this)
    resumes = []  # Replace with SQL query to retrieve top 10 resumes
    return render_template('top_resumes.html', resumes=resumes)

# Route to display detailed information about a selected resume
@routes.route('/resume/<int:resume_id>')
def resume_details(resume_id):
    # Retrieve detailed information about the selected resume from the database (you need to implement this)
    resume_info = {}  # Replace with SQL query to retrieve resume details
    return render_template('resume_details.html', resume_info=resume_info)

# Route to send email to candidate
@routes.route('/send_email/<int:resume_id>')
def send_email(resume_id):
    # Code to send email to the candidate (you need to implement this)
    return "Email sent successfully"


@routes.route('/resume_details', methods=['POST'])
def show_resume_details():
    if request.method == 'POST':
        custom_input = request.form['resume_data']
        initialize_database()
        results = parse_resume_from_pdf(custom_input)
        save_to_database(results)
        return render_template('resume_details.html', resume_info=results)
    else:
        return render_template('resume_details.html')
