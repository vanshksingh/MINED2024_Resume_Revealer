import warnings
from urllib3.exceptions import NotOpenSSLWarning
from csv_generator import *
from text_extractor import *
import io
import tkinter as tk
from tkinter import filedialog

def main():

    print("Welcome to the Resume Parser!")
    CheckAI()
    print("Please select the resumes you want to parse from the dialog box.")
    # Filter out NotOpenSSLWarning
    warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

    files = open_file_window()  # Open file window to select files
    if files:
        initialize_database()
        print("Database initialized.")

        extracted_texts = []
        for file_data in files:
            file_name, file_content = file_data
            print(f"Processing {file_name}...")
            text = extract_text(file_data)
            extracted_texts.append((file_name, text))
            print(f"Extracted text from {file_name}.")

        for file_name, text in extracted_texts:
            try:
                print(f"Extracted text from {file_name}: {text}")

                results = parse_resume_from_pdf(text[:2000])
                save_to_database(results)
                print(f"Data from {file_name} saved to database.")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
                continue  # Skip to the next file if an error occurs

        print("All files processed.")



        CheckAI()



    else:
        print("No files selected.")





def CheckAI():
    print("Starting AI mode...")
    ai_mode = input("Would you like to use AI mode? (yes/no): ").lower()

    if ai_mode == 'yes':
        print("AI mode activated!")
        AI()
        # Call your AI mode function or include the AI functionality here
    elif ai_mode == 'no':
        print("AI mode deactivated.")
        # Add alternative functionality if AI mode is deactivated
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        CheckAI()  # Restart the function if the input is invalid


if __name__ == "__main__":
    main()
