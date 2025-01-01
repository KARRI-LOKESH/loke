import React, { useState } from 'react';
import axios from 'axios';

function JobApplication() {
  const [application, setApplication] = useState({
    job_post: '',
    cover_letter: '',
  });

  const handleChange = (e) => {
    setApplication({ ...application, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const token = localStorage.getItem('access_token');

    if (!token) {
      alert('Please login first.');
      return;
    }

    try {
      await axios.post('http://localhost:8000/api/applications/', application, {
        headers: { Authorization: `Bearer ${token}` },
      });
      alert('Application submitted successfully!');
    } catch (error) {
      console.error('Error applying for job:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Apply for Job</h2>
      <input type="text" name="job_post" placeholder="Job Post ID" onChange={handleChange} required />
      <textarea name="cover_letter" placeholder="Cover Letter" onChange={handleChange} required></textarea>
      <button type="submit">Submit Application</button>
    </form>
  );
}

export default JobApplication;
