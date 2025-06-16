import pandas as pd
from fpdf import FPDF
import os


def read_data(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.csv':
        data = pd.read_csv(file_path)
    elif ext == '.json':
        data = pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file type. Use only Marks.csv or Marks_JSON.json.")

    return data


def generate_report(data, output_file):
    if 'Name' not in data.columns or 'Marks' not in data.columns:
        raise ValueError("File must contain 'Name' and 'Marks' columns.")

    average_marks = data['Marks'].mean()
    highest_marks = data['Marks'].max()
    lowest_marks = data['Marks'].min()
    topper = data.loc[data['Marks'].idxmax()]['Name']

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Student Performance Report", ln=True, align='C')

    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    for index, row in data.iterrows():
        pdf.cell(200, 10, txt=f"{row['Name']} - {row['Marks']} Marks", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Summary Statistics", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Average Marks: {average_marks:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Highest Marks: {highest_marks}", ln=True)
    pdf.cell(200, 10, txt=f"Lowest Marks: {lowest_marks}", ln=True)
    pdf.cell(200, 10, txt=f"Topper: {topper}", ln=True)

    pdf.output(output_file)
    print(f"Report generated successfully as {output_file}")


if __name__ == "__main__":
    file_path = input("Enter the file path (Marks.csv or Marks_JSON.json): ")
    output_file = "Generated_Student_Report.pdf"

    try:
        data = read_data(file_path)
        generate_report(data, output_file)
    except Exception as e:
        print("Error:", e)

