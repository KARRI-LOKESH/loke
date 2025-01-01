import React, { useState } from 'react';
import axios from 'axios';

function CreateJob() {
    const [job, setJob] = useState({
        title: '',
        description: '',
        location: '',
        salary: '',
    });

    const handleChange = (e) => {
        setJob({ ...job, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const token = localStorage.getItem('access_token');
        axios.post('http://localhost:8000/api/jobs/', job, {
            headers: {
                Authorization: `Bearer ${token}`,
            },
        })
        .then(() => alert('Job created!'))
        .catch(error => console.error('Error creating job:', error));
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Create Job</h2>
            <label>Title:</label>
            <input type="text" name="title" onChange={handleChange} required />
            
            <label>Description:</label>
            <textarea name="description" onChange={handleChange} required />

            <label>Location:</label>
            <input type="text" name="location" onChange={handleChange} required />

            <label>Salary:</label>
            <input type="number" name="salary" onChange={handleChange} required />

            <button type="submit">Create</button>
        </form>
    );
}

export default CreateJob;
