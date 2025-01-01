import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Dashboard() {
  const [applications, setApplications] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem('access_token');

    if (!token) {
      alert('Please login first.');
      return;
    }

    axios
      .get('http://localhost:8000/api/applications/', {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((response) => {
        setApplications(response.data);
      })
      .catch((error) => {
        console.error('Error fetching applications:', error);
      });
  }, []);

  return (
    <div>
      <h2>Your Applications</h2>
      {applications.length > 0 ? (
        applications.map((app) => (
          <div key={app.id}>
            <p><strong>Job:</strong> {app.job_post}</p>
            <p><strong>Status:</strong> {app.status}</p>
          </div>
        ))
      ) : (
        <p>No applications found.</p>
      )}
    </div>
  );
}

export default Dashboard;
