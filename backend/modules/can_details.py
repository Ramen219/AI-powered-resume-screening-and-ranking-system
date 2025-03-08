import re

def extract_candidate_details(text):
    """
    Extracts the candidate's name and contact details (phone & email) from resume text.
    """
    name = "Unknown"

    # Dynamically filter out section headers
    invalid_headers = {
        "CONTACT", "PROFILE", "SKILLS", "EDUCATION", "WORK EXPERIENCE", "PROJECTS",
        "LANGUAGES", "EXPERIENCE", "CERTIFICATIONS", "ACHIEVEMENTS", "INTERNSHIPS",
        "TRAINING", "SUMMARY", "TECHNICAL SKILLS", "COURSES", "HOBBIES"
    }

    # Extract Name: Consider only the first 6 lines of text
    lines = text.strip().split("\n")[:6]

    for line in lines:
        line = line.strip()

        # Skip empty lines and section headers (case-insensitive)
        if not line or line.upper() in invalid_headers:
            continue

        # Look for a valid name format (allow uppercase names too)
        name_match = re.match(r'^[A-Z][a-z]+(?: [A-Z][a-z]+){0,2}$', line) or re.match(r'^[A-Z\s]{3,}$', line)

        if name_match:
            name = line.title()  # Convert to title case (e.g., "AVIK DAS" → "Avik Das")
            break  # Stop once we find a valid name

    # Extract Contact Details
    phone_match = re.search(r'(\+?\d{1,3}[-.\s]?\d{3,5}[-.\s]?\d{3,5}[-.\s]?\d{3,5})', text)
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

    contact = {
        'phone': phone_match.group(0) if phone_match else "Not found",
        'email': email_match.group(0) if email_match else "Not found"
    }

    return name, contact
