// components/LoginForm.jsx
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const LoginForm = ({onLoginSuccess}) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');

        try {
            const response = await fetch('http://127.0.0.1:8000/api/login/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password }),
            });
            if (response.ok) {
                const data = await response.json();
               onLoginSuccess(data.username)
               navigate('/')
            } else {
                 const errorData = await response.json();
                  if (errorData.non_field_errors && errorData.non_field_errors[0] === "User is not active"){
                      setError("Please verify your email address before logging in.")
                 } else if (errorData.non_field_errors){
                      setError(errorData.non_field_errors[0])
                  } else if (errorData.email) {
                      setError(errorData.email[0])
                  } else if (errorData.password){
                      setError(errorData.password[0])
                  } else {
                     setError("Login failed")
                 }
            }
        } catch (error) {
            setError("Error during request: " + error.message);
        }
    };

    return (
        <div className="bg-white p-6 rounded shadow-md">
            <form onSubmit={handleSubmit}>
                <div className="mb-4">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="email">
                        Email
                    </label>
                    <input
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        type="email"
                        id="email"
                        placeholder="Enter email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div className="mb-4">
                    <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="password">
                        Password
                    </label>
                    <input
                        className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                        type="password"
                        id="password"
                        placeholder="Enter password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                {error && <p className="text-red-500 mb-2">{error}</p>}
                <button
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                    type="submit"
                >
                    Login
                </button>
            </form>
        </div>
    );
};

export default LoginForm;