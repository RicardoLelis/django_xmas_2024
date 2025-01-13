// components/RegisterPage.jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';
import RegisterForm from './RegisterForm';

const RegisterPage = () => {
    const navigate = useNavigate();

    return (
        <div className="flex items-center justify-center h-screen bg-gray-100">
            <div className="bg-white p-8 rounded shadow-md w-96">
                <h2 className="text-2xl font-semibold mb-6 text-center">Register</h2>
                <RegisterForm />
                <div className="mt-4 text-center">
                    <p>
                        Already have an account?{' '}
                        <button onClick={() => navigate('/login')} className="text-blue-500 hover:underline">
                            Login here
                        </button>
                    </p>
                </div>
            </div>
        </div>
    );
};

export default RegisterPage;