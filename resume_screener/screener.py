import os
import re
import docx
import PyPDF2
import pandas as pd
import webbrowser

# === Step 1: Read Job Requirements ===
def load_job_keywords(filepath='job_description.txt'):
    with open(filepath, 'r', encoding='utf-8') as file:
        keywords = [line.strip().lower() for line in file if line.strip()]
    return keywords

# === Step 2: Extract Text from DOCX ===
def extract_text_docx(path):
    doc = docx.Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

# === Step 3: Extract Text from PDF ===
def extract_text_pdf(path):
    with open(path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        return "\n".join(page.extract_text() or '' for page in reader.pages)

# === Step 4: Match Resume Text Against Keywords ===
def match_resume(text, keywords):
    matched = [kw for kw in keywords if re.search(r'\b' + re.escape(kw) + r'\b', text.lower())]
    return matched, len(matched)

# === Step 5: Process All Resumes ===
def process_resumes(folder='resumes', keywords=[]):
    results = []
    for filename in os.listdir(folder):
        if filename.endswith('.pdf') or filename.endswith('.docx'):
            path = os.path.join(folder, filename)
            text = extract_text_pdf(path) if filename.endswith('.pdf') else extract_text_docx(path)
            matched_keywords, score = match_resume(text, keywords)
            results.append({
                'Filename': filename,
                'Matched Keywords': ", ".join(matched_keywords),
                'Score': score
            })
    return results

# === Step 6: Export to Excel and Apply Filtering ===
def export_to_excel(results, output='shortlisted_candidates.xlsx', min_score=1):
    df = pd.DataFrame(results)
    df = df[df['Score'] >= min_score]
    df = df.sort_values(by='Score', ascending=False)

    try:
        df.to_excel(output, index=False)
        print(f"\n✅ {len(df)} candidates shortlisted and saved to {output}")
        abs_path = os.path.abspath(output)
        webbrowser.open(f'file://{abs_path}')
    except PermissionError:
        print("❌ Cannot write to Excel file. Please close 'shortlisted_candidates.xlsx' and try again.")

# === Optional: Send Email Notification (Optional - Configure SMTP) ===
def send_email_notification():
    # Placeholder function — configure SMTP if needed
    print("📧 Email feature is not active. Add SMTP config to enable.")

# === Main Function ===
def main():
    if not os.path.exists("resumes"):
        print("❌ 'resumes' folder not found. Please create one with some resume files.")
        return

    keywords = load_job_keywords()
    results = process_resumes(keywords=keywords)
    export_to_excel(results, min_score=1)

    # Uncomment below line to activate email (SMTP setup needed)
    # send_email_notification()

if __name__ == '__main__':
    main()
