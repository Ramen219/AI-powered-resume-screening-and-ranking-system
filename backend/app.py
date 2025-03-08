# from flask import Flask, request, jsonify  # Import necessary modules from Flask
# from modules.resume_parser import extract_text # Import the extract_text function from resume_parser module
# from modules.can_details import extract_candidate_details
# from modules.ranking import rank_resumes  # Import the rank_resumes function from ranking module
# from flask_cors import CORS


# # Create a Flask application instance
# app = Flask(__name__)  
# CORS(app)

# # Define a route for the '/upload' URL that accepts POST requests
# @app.route('/upload', methods=['POST'])
# def upload_resume():
#     if 'resumes' not in request.files:
#         return jsonify({'error': 'No file uploaded'}), 400  # Handle missing file
#     print("Received Files:", request.files)

    
#     files = request.files.getlist('resumes')  # Use parentheses () get multiple files
#     results = []  # Initialize an empty list to store the results

#     if not files:
#         return jsonify({'error': 'No files uploaded'}), 400  # Handle missing file
    
#     for file in files:
#         if file.filename == '':
#             continue
        
#         try:
#             text = extract_text(file) # Extracts text from the resume
#             name, contact = extract_candidate_details(text) # Extracts Name & Contact
#             score = rank_resumes(text) # Rank the resume

#             # Append the results to the list
#             results.append({
#                 'filename' : file.filename,
#                 'name' : file.filename,
#                 'contact' : contact,
#                 'score' : score
#             })

#         except Exception as e:
#             results.append({
#                 'filename' : file.filename,
#                 'error' : str(e)
#             })

#     # Returns scores & details of all uploaded resumes (both single & multiple)
#     return jsonify({'results' : results})

# if __name__ == '__main__':  # Check if the script is run directly (not imported as a module)
#     app.run(debug=True)  # Run the Flask application in debug mode


from flask import Flask, request, jsonify  # Import necessary modules from Flask
from modules.resume_parser import extract_text  # Import the extract_text function from resume_parser module
from modules.can_details import extract_candidate_details  # Import the candidate details extraction module
from modules.ranking import rank_resumes  # Import the rank_resumes function from ranking module
from flask_cors import CORS

# Create a Flask application instance
app = Flask(__name__)  
CORS(app)

# Define a route for the '/upload' URL that accepts POST requests
@app.route('/upload', methods=['POST'])
def upload_resume():
    print("🔍 Debug: Request received.")

    # Print all received form data
    print("🔍 Debug: Form Data Received ->", request.form)
    print("🔍 Debug: Files Received ->", request.files)

    if 'resumes' not in request.files:
        print("❌ Debug: No files found in request.")
        return jsonify({'error': 'No file uploaded'}), 400  

    job_description = request.form.get('job_description', "").strip()
    if not job_description:
        print("❌ Debug: Job description missing in request.")
        return jsonify({'error': 'Job description is required'}), 400

    print(f"✅ Debug: Job Description Received: {job_description}")

    files = request.files.getlist('resumes')
    if not files:
        print("❌ Debug: No resumes found in request.")
        return jsonify({'error': 'No files uploaded'}), 400

    results = []
    for file in files:
        if file.filename == '':
            print("⚠️ Debug: Empty filename detected, skipping.")
            continue
        
        try:
            text = extract_text(file)
            name, contact = extract_candidate_details(text)
            score = rank_resumes([text], job_description)[0]

            results.append({
                'filename': file.filename,
                'name': name,
                'contact': contact,
                'score': score
            })
            print(f"✅ Debug: Processed {file.filename} successfully.")
        except Exception as e:
            print(f"❌ Debug: Error processing {file.filename}: {str(e)}")
            results.append({'filename': file.filename, 'error': str(e)})

    return jsonify({'results': results})


if __name__ == '__main__':  # Check if the script is run directly (not imported as a module)
    app.run(debug=True)  # Run the Flask application in debug mode
