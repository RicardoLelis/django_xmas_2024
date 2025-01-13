import React, { useState, useEffect } from 'react';

const WelcomePage = ({ user }) => {
    const [userData, setUserData] = useState(null);
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState(null);
    
    useEffect(() => {
        const fetchData = async () => {
        setLoading(true);
        try {
            const response = await fetch('/data/user_data.json');
            if (!response.ok){
                throw new Error(`HTTP Error: ${response.status}`)
            }
            const data = await response.json();
            setUserData(data)

        }catch (error) {
            setError(error.message)
        }finally{
            setLoading(false)
        }
    }
    fetchData()
    },[])

    if (loading) {
   return <div className="p-4">Loading user data...</div>;
   }
     if (error){
         return <div className="p-4 text-red-500">Error: {error}</div>;
     }


 if (!userData) {
      return <div className="p-4">User data not available.</div>;
    }
  return (
    <div className="p-4">
      <h2 className="text-2xl font-semibold mb-4">Welcome, {user}!</h2>
     <div className='mb-4'>
        <p>
            Last Login: {userData.lastLogin}
        </p>
    </div>
      <h3 className="text-xl font-semibold mb-2">Net Worth</h3>
      <div className="flex justify-center mb-4">
        <div className="w-1/2 h-40 border border-gray-300 rounded shadow-sm">
          {/* Placeholder chart */}
          <div className="flex items-center justify-center h-full">
            {userData.netWorthChartData.map((val, index) => (
               <div key={index} className="flex flex-col items-center p-2 text-center">
                    <div className="bg-blue-500 text-white p-2 rounded shadow-md" style={{height: val}} > {val} </div>
                     <div className="text-xs">{index + 1}</div>
               </div>
            ))}
          </div>
        </div>
      </div>
     
      <h3 className="text-xl font-semibold mb-2">Last Transactions</h3>
        <table className="w-full table-auto border-collapse border border-slate-500">
             <thead>
                 <tr >
                     <th className="border border-slate-600 p-2">Date</th>
                      <th className="border border-slate-600 p-2">Description</th>
                     <th className="border border-slate-600 p-2">Amount</th>
                 </tr>
             </thead>
             <tbody>
                {userData.transactions.map(transaction => (
                  <tr key={transaction.id} className="hover:bg-gray-100">
                       <td className="border border-slate-700 p-2 text-center">{transaction.date}</td>
                      <td className="border border-slate-700 p-2 text-center">{transaction.description}</td>
                      <td className="border border-slate-700 p-2 text-center">{transaction.amount}</td>
                  </tr>
                ))}
             </tbody>
        </table>
    </div>
  );
};

export default WelcomePage;