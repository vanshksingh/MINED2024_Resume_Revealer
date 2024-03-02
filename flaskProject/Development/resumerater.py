import mysql.connector
import google.generativeai as genai

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

'''
if __name__ == "__main__":
    position_to_rate_for = "Software Engineer"  # Specify the position you want to rate for
    rate_all_resumes_for_position(position_to_rate_for)
'''