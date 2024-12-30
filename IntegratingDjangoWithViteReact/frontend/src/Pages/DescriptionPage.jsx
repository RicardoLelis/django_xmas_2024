import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams, useNavigate } from "react-router-dom";

function DescriptionPage() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [item, setItem] = useState([]);


  useEffect(() => {
    axios
      .get(`http://127.0.0.1:8000/api/desc/${id}/`)
      .then((response) => {
        const data = response.data;
        setItem(data);
        console.log(data);
      })
      .catch((error) => {
        console.log("There was an error fetching the items!", error);
      });        
  }, []);

  return (
    <>
      <div className="mx-10 space-y-4">
        <h1 className="text-purple-100 text-3xl font-bold">{item.name}</h1>
        <p className="text-purple-100">{item.description}</p>
        <div className="flex justify-end">
            <button
                onClick={() => navigate(-1)}
                className="bg-purple-400 hover:bg-purple-600 transition duration-200 px-4 py-2 rounded-lg"
            >
                Go Back
            </button>
        </div>
      </div>
    </>
  );
}

export default DescriptionPage;
