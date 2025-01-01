import React, { useState, useEffect } from 'react';
import axios from 'axios';

function EditJobPost({ selectedJobId, fetchJobs, closeEdit }) {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    category: '',
    experience_level: '',
    location: '',
    salary: '',
  });

  useEffect(() => {
    if (selectedJobId) {
      axios
        .get(`http://localhost:8000/api/jobs/posts/${selectedJobId}/`)
        .then((response) => setFormData(response.data))
        .catch((error) => console.error('Error fetching job:', error));
    }
  }, [selectedJobId]);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios
      .put(`http://localhost:8000/api/jobs/posts/${selectedJobId}/`, formData)
      .then((response) => {
        alert('Job Updated Successfully!');
        fetchJobs(); // Refresh job list
        closeEdit(); // Close edit form
      })
      .catch((error) => console.error('Error updating job:', error));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Edit Job Post</h2>
      {Object.keys(formData).map((key) => (
        <input
          key={key}
          type="text"
          name={key}
          placeholder={`Enter ${key.replace('_', ' ')}`}
          value={formData[key]}
          onChange={handleChange}
        />
      ))}
      <button type="submit">Update Job</button>
    </form>
  );
}

export default EditJobPost;
