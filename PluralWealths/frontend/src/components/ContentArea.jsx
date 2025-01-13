// components/ContentArea.jsx

import React from 'react';
import WelcomePage from "./WelcomePage";

const ContentArea = ({ activeSection, user }) => {
  return (
      <main className="flex-1 p-4">
        {user ? (
          <WelcomePage user={user} />
         ) : (
             <div className="bg-white p-6 rounded shadow-md">
                Select a menu to view.
             </div>
         )}
      </main>
  );
};

export default ContentArea;