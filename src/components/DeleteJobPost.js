import axios from 'axios';

function DeleteJobPost({ jobId }) {
  const handleDelete = () => {
    axios.delete(`http://localhost:8000/api/jobs/posts/${jobId}/`)
      .then(() => alert('Job Deleted Successfully'))
      .catch(error => console.error('Error deleting job post:', error));
  };

  return <button onClick={handleDelete}>Delete</button>;
}

export default DeleteJobPost;
