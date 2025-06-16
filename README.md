# AUTOMATED-REPORT-GENERATION

COMPANY : CODTECH IT SOLUTIONS
NAME : SUNKARI VINAY KUMAR
INTERN ID : CT04DN68
DOMAIN : PYTHON PROGRAMMING
MENTOR : NEELA SANTOSH

#  Automated Report Generation using Python

# Project Overview

This project is a simple yet powerful Python script that reads student marks data from either a **CSV** or **JSON** file, analyzes it, and generates a formatted **PDF report** containing individual marks and summary statistics like average, highest, and lowest marks.


# Features

-  Supports **CSV** and **JSON** files as input
-  Calculates:
  - Average Marks
  - Highest Marks
  - Lowest Marks
  - Topper Name
-  Generates a clean and readable **PDF Report** using `fpdf`
- Output PDF saved in the **project directory**



# Project Structure

/Project_Folder/
├── Marks.csv
├── Marks_JSON.json
├── report_generator_marks.py
├── requirements.txt
├── Generated_Student_Report.pdf # Generated after script execution
└── README.md


# Installation

**Required Python Libraries:**

- `pandas`
- `fpdf`

# Install via pip:

pip install -r requirements.txt
requirements.txt

nginx
Copy
Edit
fpdf
pandas


How to Use :

Place your data file (Marks.csv or Marks_JSON.json) inside the project folder.

Run the Python script:
python report_generator_marks.py
Enter your file name when prompted:

css
Copy
Edit
Marks.csv
or

pgsql
Copy
Edit
Marks_JSON.json
Your Generated_Student_Report.pdf will appear in the project folder.

📑 Sample Input Files
Marks.csv
Marks_JSON.json

csv :
Name,Marks
Nani,85
Vinay,90
Sai,78
Ravi,88
Raju,95
Marks_JSON.json

json :

[
  {"Name": "Nani", "Marks": 85},
  {"Name": "Vinay", "Marks": 90},
  {"Name": "Sai", "Marks": 78},
  {"Name": "Ravi", "Marks": 88},
  {"Name": "Raju", "Marks": 95}
]
📤 Output
The script generates a PDF file named:

Generated_Student_Report.pdf
in the same directory as your script.

Completion :
This project is part of the CODTECH Internship submission for the Automated Report Generation task.
