from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text = """
#Project Name : Smart Student tracker
A simple student tracking system built using Python and Flask. It allows users to add, view, and manage student information such as name, age, grade, and contact details. The application provides a user-friendly interface for easy navigation and efficient data management. It also includes features like search functionality and data validation to ensure accurate and organized student records.

#Features  

- Add Student: Users can add new student records by filling out a form with the student's details.
- View Students: Users can view a list of all students in the system, along with their information.
- Search Functionality: Users can search for specific students based on their name or other attributes.
- Data Validation: The application includes validation checks to ensure that the entered data is accurate and complete.

#Tech stack:
- Python: The programming language used for the backend development of the application.
- Flask: A lightweight web framework used to build the web application and handle routing.
- HTML/CSS: Used for creating the frontend interface of the application.

#Getting Started
To get started with the Smart Student Tracker project, follow these steps:
1. Clone the repository: `git clone
https://github.com/your-username/smart-student-tracker.git`
2. Navigate to the project directory: `cd smart-student-tracker`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the application: `python app.py`
5. Open your web browser and go to `http://localhost:5000` to access the application.

"""

#Initializing the RecursiveCharacterTextSplitter with a chunk size of 100 characters and an overlap of 20 characters

text_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size=100,
    chunk_overlap=0)

#Splitting the text into chunks
chunks = text_splitter.split_text(text)
#Printing the resulting chunks
print(chunks)
