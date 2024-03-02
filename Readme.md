

# Resume Parser and Conversational AI

<img width="1680" alt="Screenshot 2024-03-02 at 10 42 51 AM" src="https://github.com/vanshksingh/MINED2024_Resume_Revealer/assets/114809624/b8d6848b-16bd-4ee7-bdcb-cf2de1edf73e">


## Overview

The Resume Parser and Conversational AI project is a comprehensive solution designed to streamline the process of resume analysis and provide interactive communication capabilities. Leveraging cutting-edge technologies, this project offers a powerful suite of features for extracting text from resumes, storing and analyzing data in a MySQL database, and engaging in natural language conversations using the Google Gemini model.

## Key Features

- **Resume Parsing**: Extracts text from resumes in various formats, including PDF, DOCX, DOC, TXT, and images.
- **Conversational AI**: Utilizes the Google Gemini model to engage in interactive conversations with users.
- **Database Integration**: Stores extracted resume data in a MySQL database for easy access and analysis.
- **User-Friendly Interface**: Provides a GUI window for selecting multiple files and initiating processing tasks.
- **AI Mode**: Offers an AI mode for advanced processing and analysis of resume data.

## Requirements

- Python 3.x
- Python packages: `mysql-connector-python`, `google.generativeai`, `pytesseract`, `docx`, `pdf2image`, `Pillow`, `textract`, `tkinter`
- MySQL database

## Installation

1. **Clone the Repository**:

   ```
   git clone https://github.com/yourusername/resume-parser.git
   cd resume-parser
   ```

2. **Install Dependencies**:

   ```
   pip install -r requirements.txt
   ```

3. **Set Up MySQL Database**:

   - Install MySQL and create a new database for the project.
   - Update the MySQL connection details in `main.py` with your database credentials.

## Usage

1. **Run the Main Script**:

   ```
   python run.py
   ```

2. **Follow On-Screen Prompts**:

   - Select resumes for processing.
   - Interact with the conversational AI.

3. **Activate AI Mode (Optional)**:

   - Utilize the AI mode for advanced analysis of resume data.

## Documentation

- **`extract_text(file_data)`**: Extracts text from various file formats.
- **`open_file_window()`**: Opens a GUI window for selecting files.
- **`process_files(files)`**: Processes selected files and extracts text.
- **`start_gemini_conversation(initial_input)`**: Initiates a conversational AI session.
- **`Development Folder`**: It contains files and features under development.

  
<img width="1680" alt="Screenshot 2024-03-02 at 10 43 42 AM" src="https://github.com/vanshksingh/MINED2024_Resume_Revealer/assets/114809624/f85bc731-3202-4402-8428-d0604d53d136">
<img width="1680" alt="Screenshot 2024-03-02 at 10 44 45 AM" src="https://github.com/vanshksingh/MINED2024_Resume_Revealer/assets/114809624/3c83516e-06a1-45a8-b7cd-390c87033643">


## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Thanks to [Google](https://google.com) for providing the Gemini model.
- Special thanks to the open-source community for their valuable contributions.

## Contact

For questions or inquiries, please contact [yourname](mailto:vsvsasas@gmail.com).

---
