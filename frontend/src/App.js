import React, { useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";

const App = () => {
  const [files, setFiles] = useState([]);
  const [jobDescription, setJobDescription] = useState("");
  const [customJobDescription, setCustomJobDescription] = useState("");
  const [results, setResults] = useState([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const jobOptions = [
    "Software Engineer", "Data Scientist", "Product Manager", "Sales Manager",
    "Cyber Security Analyst", "UX/UI Designer", "AI/ML Engineer", "Business Analyst",
    "Web Developer", "Network Engineer", "DevOps Engineer", "Cloud Architect",
    "Database Administrator", "Systems Analyst", "IT Manager", "Technical Support",
    "QA Engineer", "Scrum Master", "Project Manager", "Network Administrator",
    "Security Engineer", "Help Desk Technician", "IT Director", "IT Coordinator",
    "IT Specialist", "IT Consultant", "IT Engineer", "MERN Developer", "Other"
  ];

  const handleFileChange = (event) => {
    setFiles(event.target.files);
    setError("");
  };

  const handleJobChange = (event) => {
    setJobDescription(event.target.value);
  };

  const handleCustomJobChange = (event) => {
    setCustomJobDescription(event.target.value);
  };

  const handleUpload = async () => {
    if (!files.length) {
      setError("Please select at least one file.");
      return;
    }
    if (!jobDescription) {
      setError("Please select a job description.");
      return;
    }
    if (jobDescription === "Other" && !customJobDescription) {
      setError("Please enter a custom job description.");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
      formData.append("resumes", files[i]);
    }
    formData.append("job_description", jobDescription === "Other" ? customJobDescription : jobDescription);

    console.log("📤 Debug: Form Data Contents");
    for (let pair of formData.entries()) {
      console.log(`${pair[0]}:`, pair[1]);
    }

    try {
      const response = await axios.post("http://127.0.0.1:5000/upload", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      if (response.data && response.data.results) {
        setResults(response.data.results);
        setError("");
      } else {
        setError("No results returned from the server.");
      }
    } catch (error) {
      setError("Failed to upload files. Ensure the backend is running.");
      console.error("❌ Error uploading files:", error.response ? error.response.data : error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="d-flex flex-column align-items-center justify-content-center" style={{
      background: "linear-gradient(135deg, #1e3c72, #2a5298)",
      minHeight: "100vh",
      color: "white",
      padding: "20px",
      overflow: "hidden"
    }}>
      <div className="container p-5 rounded shadow-lg text-center" style={{ backgroundColor: "rgba(0, 0, 0, 0.7)"}}>
        <h2 className="text-center fw-bold">AI Powered Resume Screening & Ranking System</h2>
        <p className="text-center text-light">Upload resumes to rank candidates based on relevance.</p>

        <div className="d-flex flex-column align-items-center w-100">
          <select onChange={handleJobChange} className="form-control mb-3 w-75">
            <option value="">Select Job Description</option>
            {jobOptions.map((job, index) => (
              <option key={index} value={job}>{job}</option>
            ))}
          </select>

          {jobDescription === "Other" && (
            <input
              type="text"
              placeholder="Enter Custom Job Description"
              className="form-control w-75 mb-3"
              onChange={handleCustomJobChange}
            />
          )}

          <input type="file" multiple onChange={handleFileChange} className="form-control w-75 mb-3" />
          <button onClick={handleUpload} className="btn btn-primary btn-lg px-5" disabled={loading}>
            {loading ? "Uploading..." : "Upload"}
          </button>
          {error && <p className="text-danger mt-2">{error}</p>}
        </div>

        {results.length > 0 && (
  <div className="mt-4 w-100">
    <h4 className="text-center">Ranked Resumes</h4>
    <div className="table-responsive" style={{ width: "100%", overflowX: "hidden" }}>
      <table className="table table-dark table-striped table-hover mt-3">
        <thead>
          <tr>
            <th>Sl.</th>
            <th>File Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Score (%)</th> {/* Ensure Score Column is Here */}
          </tr>
        </thead>
        <tbody>
          {results.sort((a, b) => b.score - a.score).map((res, index) => (
            <tr key={index}>
              <td>{index + 1}</td>
              <td>{res.filename || "Unknown"}</td>
              <td>{res.contact?.email || "Not found"}</td>
              <td>{res.contact?.phone || "Not found"}</td>
              <td><strong>{res.score ? `${res.score}%` : "Error"}</strong></td> {/* Ensure Score is Here */}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  </div>
)}

      </div>
    </div>
  );
};

export default App;
