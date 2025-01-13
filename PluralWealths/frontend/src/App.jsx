// App.jsx
import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import ContentArea from './components/ContentArea';
import LoginPage from './components/LoginPage';
import RegisterPage from './components/RegisterPage';
import WelcomePage from "./components/WelcomePage";

const App = () => {
    const [activeSection, setActiveSection] = useState('');
    const [user, setUser] = useState('');


    const handleSectionChange = (sectionId) => {
        setActiveSection(sectionId);
    };
    const handleUserChange = (username) => {
        setUser(username);
    };

    const handleLogout = () => {
        setUser('');
    };


    return (
        <Router>
            <Routes>
                <Route path="/login" element={<LoginPage onLoginSuccess={handleUserChange} />} />
                <Route path="/register" element={<RegisterPage />} />
                <Route path="/" element={
                         user ? (
                            <div className="flex">
                                <Sidebar
                                    activeSection={activeSection}
                                    onSectionChange={handleSectionChange}
                                    onLogout={handleLogout}
                                    user={user}
                                />
                                  <ContentArea activeSection={activeSection} user={user}  />
                            </div>
                        ) : (
                            <Navigate to="/login" replace />
                        )
                     }
                 />
                <Route path="/welcome" element={<WelcomePage user={user} />} />
            </Routes>
        </Router>
    );
};

export default App;