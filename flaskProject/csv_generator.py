import mysql.connector
import re
import google.generativeai as genai
from text_extractor import *
import mysql.connector
import google.generativeai as genai
from gemini_conversation import start_gemini_conversation

# Set up API key
API_KEY = "AIzaSyAvh9AbDKJ6E0DdOUll0f1p4qCSlerGvfs"
genai.configure(api_key=API_KEY)


def run_resume_parser_conversation(user_input, position):
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(user_input, stream=True)
    full_response = ""

    for result in response:
        for part in result.parts:
            full_response += part.text

    # Extract rating from the response
    rating = extract_rating(full_response)

    return rating



def extract_rating(response):
    return response


def rate_resume_with_position(candidate_info, position):
    # Generate rating for the given candidate info and position
    user_input = f"Generate a rating from 1 to 10 for the suitability of person for the role of {position}. The rating should reflect how well the person's skills, experience, and qualifications align with the requirements of the job. Please provide a single number as the output."
    rating = run_resume_parser_conversation(user_input, position)
    return rating


def rate_all_resumes_for_position(position):
    # Fetch candidates data from the database
    candidates_data = fetch_candidates_data()

    # Iterate over fetched candidate data and rate each resume
    for candidate_data in candidates_data:
        rating = rate_resume_with_position(candidate_data, position)
        # Update the rating in the database
        update_rating_in_database(candidate_data[0], rating)


def fetch_candidates_data():
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="vks-MacBook-Pro.local",
        user="root",
        password="dellomac",
        database="your_database"
    )
    cursor = conn.cursor()

    # Fetch candidate data from the database
    select_candidates_query = """
        SELECT name, achievements, skills, certifications, projects, summary
        FROM resume_data
    """
    cursor.execute(select_candidates_query)
    candidates_data = cursor.fetchall()

    # Close connection
    cursor.close()
    conn.close()

    return candidates_data


def update_rating_in_database(candidate_name, rating):
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="vks-MacBook-Pro.local",
        user="root",
        password="dellomac",
        database="your_database"
    )
    cursor = conn.cursor()

    # Update the rating in the database for the given candidate name
    update_rating_query = """
        UPDATE resume_data
        SET rating = %s
        WHERE name = %s
    """
    cursor.execute(update_rating_query, (rating, candidate_name))
    conn.commit()

    # Close connection
    cursor.close()
    conn.close()


def initialize_database():
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="vks-MacBook-Pro.local",
        user="root",
        password="dellomac"
    )
    cursor = conn.cursor()

    # Create database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS your_database")
    cursor.execute("USE your_database")

    # Create table if it doesn't exist
    create_table_query = """
        CREATE TABLE IF NOT EXISTS resume_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(255),
            degree VARCHAR(255),
            university VARCHAR(255),
            graduation_year VARCHAR(255),
            job_role VARCHAR(255),
            job_title VARCHAR(255),
            achievements TEXT,
            skills TEXT,
            certifications TEXT,
            projects TEXT,
            summary TEXT,
            rating VARCHAR(255) DEFAULT NULL
        )
    """
    cursor.execute(create_table_query)

    # Commit and close connection
    conn.commit()
    cursor.close()
    conn.close()


def parse_resume_from_pdf(custom_input):
    # Set up API key
    API_KEY = "AIzaSyAvh9AbDKJ6E0DdOUll0f1p4qCSlerGvfs"  # Replace with your API key
    genai.configure(api_key=API_KEY)

    def run_resume_parser_conversation(user_inputs):
        model = genai.GenerativeModel('gemini-pro')
        chat = model.start_chat(history=[])
        results = {}

        for user_input in user_inputs:
            response = chat.send_message(user_input, stream=True)
            full_response = ""
            for chunk in response:
                full_response += chunk.text

            # Format the response as comma-separated values
            formatted_response = ", ".join(full_response.split('\n'))
            results[user_input] = formatted_response[:240]

        return results

    user_inputs = [
        custom_input,
        "give me only the name from resume  ",
        "give me only the email from resume  ",
        "give me only the phone number from resume  ",
        "give me only the degree with major from resume  ",
        "give me only the university from resume  ",
        "give me only the graduation year from resume  ",
        "give me all the job roles from resume ",
        "give me all the job titles from resume  ",
        "give me all the achievements from resume ",
        "give me all the skills in keywords from resume  ",
        "give me all the certifications from resume  ",
        "give me all the projects from resume  ",
        "give me a 3 line summary of the candidate",
    ]

    results = run_resume_parser_conversation(user_inputs)
    return results


def clean_alphanumeric(text):
    return re.sub(r'\W+', ' ', text)


def save_to_database(results):
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="vks-MacBook-Pro.local",
        user="root",
        password="dellomac",
        database="your_database"
    )
    cursor = conn.cursor()

    # Insert data into database
    insert_query = """
        INSERT INTO resume_data 
        (name, email, phone, degree, university, graduation_year, job_role, job_title, 
        achievements, skills, certifications, projects, summary)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cleaned_data = [
        clean_alphanumeric(results["give me only the name from resume  "]),
        clean_alphanumeric(results["give me only the email from resume  "]),
        clean_alphanumeric(results["give me only the phone number from resume  "]),
        clean_alphanumeric(results["give me only the degree with major from resume  "]),
        clean_alphanumeric(results["give me only the university from resume  "]),
        clean_alphanumeric(results["give me only the graduation year from resume  "]),
        clean_alphanumeric(results["give me all the job roles from resume "]),
        clean_alphanumeric(results["give me all the job titles from resume  "]),
        clean_alphanumeric(results["give me all the achievements from resume "]),
        clean_alphanumeric(results["give me all the skills in keywords from resume  "]),
        clean_alphanumeric(results["give me all the certifications from resume  "]),
        clean_alphanumeric(results["give me all the projects from resume  "]),
        clean_alphanumeric(results["give me a 3 line summary of the candidate"])
    ]

    cursor.execute(insert_query, cleaned_data)
    conn.commit()

    # Close connection
    cursor.close()
    conn.close()




def get_top_rated_ids(limit=10):
    # Function to get top N highest rated IDs
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="vks-MacBook-Pro.local",
        user="root",
        password="dellomac",
        database="your_database"
    )
    cursor = conn.cursor()

    # Fetch top N highest rated IDs
    select_query = """
        SELECT id
        FROM resume_data
        ORDER BY rating DESC
        LIMIT %s
    """
    cursor.execute(select_query, (limit,))
    top_ids = [row[0] for row in cursor.fetchall()]

    # Close connection
    cursor.close()
    conn.close()

    return top_ids




def AI():
    # Get top 10 highest rated IDs
    top_rated_ids = get_top_rated_ids(limit=10)

    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="vks-MacBook-Pro.local",
        user="root",
        password="dellomac",
        database="your_database"
    )
    cursor = conn.cursor()

    # Fetch data for top 10 candidates from the database
    select_query = """
         SELECT name, achievements, skills, certifications, projects, summary
         FROM resume_data
         WHERE id IN (%s)
     """

    # Create a string of placeholders for the IDs
    placeholders = ', '.join(['%s'] * len(top_rated_ids))

    # Format the query with the placeholders
    select_query = select_query % placeholders

    # Execute the query with the list of IDs as parameters
    cursor.execute(select_query, top_rated_ids)
    candidates_data = cursor.fetchall()

    # Close connection
    cursor.close()
    conn.close()

    # Prepare inputs for Gen AI
    gen_input = []

    for candidate_data in candidates_data:
        name = candidate_data[0]
        achievements = candidate_data[1]
        skills = candidate_data[2]
        certifications = candidate_data[3]
        projects = candidate_data[4]
        summary = candidate_data[5]

        # Concatenate all information for each candidate
        candidate_info = f"{name} has achieved: {achievements}. Skills: {skills}. Certifications: {certifications}. Projects: {projects}. Summary: {summary}"

        # Truncate the information if it exceeds 1000 characters
        if len(candidate_info) > 1000:
            candidate_info = candidate_info[:1000]

        gen_input.append(candidate_info)

    # Concatenate all candidate information into a single string
    all_candidates_info = "\n".join(gen_input)

    # Prefix the string with the desired message
    output = "Give me a gist of strong points of the candidate in plain text and in very short\n" + all_candidates_info

    # Run the conversation with Gen AI
    start_gemini_conversation(output[:15000])











#get_strong_points_for_top_10()