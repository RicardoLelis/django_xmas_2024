import React, { useState } from 'react';

const VerifyEmailForm = () => {
  const [token, setToken] = useState('');
   const [error, setError] = useState('');
   const [success, setSuccess] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
     setSuccess('');
    try {
      const response = await fetch('/api/verify-email/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token }),
      });

      if (response.ok) {
        setSuccess("Email Verification Successful!");
        setToken('');
      } else {
          const errorData = await response.json()
         setError(errorData.detail || 'Email Verification failed');
      }
    } catch (error) {
       setError("Error during request: " + error.message);
    }
  };

  return (
    <div className="bg-white p-6 rounded shadow-md">
      <h2 className="text-2xl font-semibold mb-4">Verify Email</h2>
      <form onSubmit={handleSubmit}>
         <div className="mb-4">
           <label
              className="block text-gray-700 text-sm font-bold mb-2"
              htmlFor="token"
            >
            Token
           </label>
          <input
            className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            type="text"
            id="token"
            placeholder="Enter token from email"
            value={token}
            onChange={(e) => setToken(e.target.value)}
            required
          />
        </div>

       {error && <p className="text-red-500 mb-2">{error}</p>}
        {success && <p className="text-green-500 mb-2">{success}</p>}
        <button
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          type="submit"
        >
         Verify
        </button>
      </form>
    </div>
  );
};

export default VerifyEmailForm;