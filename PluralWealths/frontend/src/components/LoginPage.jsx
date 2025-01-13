// components/LoginPage.jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';
import LoginForm from './LoginForm';

const LoginPage = ({onLoginSuccess}) => {
    const navigate = useNavigate();

    return (
        <div className="flex items-center justify-center h-screen bg-gray-100">
            <div className="bg-white p-8 rounded shadow-md w-96">
                <h2 className="text-2xl font-semibold mb-6 text-center">Login</h2>
                <LoginForm onLoginSuccess={onLoginSuccess} />
                <div className="mt-4 text-center">
                    <p>
                        Don't have an account?{' '}
                        <button onClick={() => navigate('/register')} className="text-blue-500 hover:underline">
                            Register here
                        </button>
                    </p>
                </div>
            </div>
        </div>
    );
};

export default LoginPage;