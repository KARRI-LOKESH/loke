import React from 'react';

const JobPosts = ({ jobPosts }) => {
  return (
    <div>
      {jobPosts.length === 0 ? (
        <p>No job posts available</p>
      ) : (
        <ul>
          {jobPosts.map((jobPost) => (
            <li key={jobPost.id}>
              <h2>{jobPost.title}</h2>
              <p>{jobPost.description}</p>
              <p>{jobPost.location}</p>
              <p>Salary: {jobPost.salary}</p>
              <p>Job Type: {jobPost.job_type}</p>
              <hr />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default JobPosts;
