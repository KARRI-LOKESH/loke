import React, { useEffect, useState } from 'react';
import JobPosts from './components/JobPosts';

const App = () => {
  const [jobPosts, setJobPosts] = useState([]);
  const [error, setError] = useState(null);

  // Fetch job posts from the Django API
  useEffect(() => {
    const fetchJobPosts = async () => {
      try {
        const token = localStorage.getItem('access_token'); // Get JWT from local storage
        const response = await fetch('http://localhost:8000/api/jobposts/', {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
          },
        });

        if (!response.ok) {
          throw new Error('Failed to fetch job posts');
        }

        const data = await response.json();
        setJobPosts(data);
      } catch (error) {
        setError(error.message);
      }
    };

    fetchJobPosts();
  }, []);

  return (
    <div>
      {error && <p>{error}</p>}
      <h1>Job Posts</h1>
      <JobPosts jobPosts={jobPosts} />
    </div>
  );
};

export default App;
