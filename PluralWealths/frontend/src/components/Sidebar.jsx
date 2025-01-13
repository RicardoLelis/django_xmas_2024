// components/Sidebar.jsx
import React from 'react';
import { useNavigate } from 'react-router-dom';

const Sidebar = ({ activeSection, onSectionChange, user, onLogout }) => {
    const navigate = useNavigate();

     const handleLogoutClick = () => {
       onLogout();
       navigate('/login', {replace: true});
    };

    return (
        <aside className="bg-gray-800 text-white w-64 h-screen fixed top-0 left-0">
            <div className="p-4">
                <h2 className="text-2xl font-semibold mb-6">App Menu</h2>
                <nav>
                    <button
                        onClick={() => onSectionChange('dashboard')}
                        className={`block py-2 px-4 hover:bg-gray-700 ${
                            activeSection === 'dashboard' ? 'bg-gray-700' : ''
                        }`}
                    >
                        Dashboard
                    </button>
                      <button
                        onClick={() => onSectionChange('accounts')}
                        className={`block py-2 px-4 hover:bg-gray-700 ${
                            activeSection === 'accounts' ? 'bg-gray-700' : ''
                        }`}
                    >
                        Accounts
                    </button>
                      <button
                        onClick={() => onSectionChange('transactions')}
                        className={`block py-2 px-4 hover:bg-gray-700 ${
                            activeSection === 'transactions' ? 'bg-gray-700' : ''
                        }`}
                    >
                        Transactions
                    </button>
                </nav>
            </div>
            {user && (
              <div className="p-4">
                  <button onClick={handleLogoutClick}
                      className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                  >
                    Logout
                 </button>
              </div>
            )}
        </aside>
    );
};
export default Sidebar;