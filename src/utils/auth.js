// Utility function to retrieve the JWT access token from localStorage
export const getAccessToken = () => {
    return localStorage.getItem('access_token');  // Retrieve the JWT token from localStorage
  };
  