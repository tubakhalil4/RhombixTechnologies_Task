# Automated Resume Screener

This Python project scans resumes (PDF/DOCX) in a folder and filters candidates based on job keywords. It generates an Excel report for HR teams to shortlist candidates efficiently.

## Features

- Extracts text from PDF and DOCX resumes
- Filters based on keywords in `job_description.txt`
- Outputs shortlisted candidates to an Excel file
- Automatically opens the Excel report

## Setup and Usage

1. Install dependencies:


2. Add resumes inside the `resumes/` folder.

3. Update `job_description.txt` with keywords.

4. Run the script:


5. Check the generated `shortlisted_candidates.xlsx` report.

## Folder Structure


resume_screener/
├── resumes/
├── job_description.txt
├── screener.py
├── README.md
└── shortlisted_candidates.xlsx (auto-generated)


## Notes

- Resumes must have selectable text (no scanned images).
- Adjust keyword match threshold in `screener.py` as needed.

