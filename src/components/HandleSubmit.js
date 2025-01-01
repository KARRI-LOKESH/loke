const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      console.log('Submitting login...');
      const response = await axios.post('http://localhost:8000/api/token/', credentials);
      console.log('Login successful:', response.data);
      localStorage.setItem('access_token', response.data.access); // Storing token in localStorage
      alert('Login successful!');
      
      // Fetch user details after login
      const userDetails = await axios.get('http://localhost:8000/api/user/', {
        headers: { Authorization: `Bearer ${response.data.access}` }
      });
      console.log('User details:', userDetails.data); // Log user details
      setUser(userDetails.data); // Store user data in state
  
      // Redirect to job posts page after successful login
      navigate('/jobposts');
    } catch (error) {
      console.error('Error logging in:', error);
      alert('Login failed. Please check your credentials.');
    }
  };
  