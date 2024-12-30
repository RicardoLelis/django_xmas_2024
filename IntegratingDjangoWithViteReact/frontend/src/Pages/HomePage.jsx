import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";

function HomePage() {
  const [items, setItems] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/list/")
      .then((response) => {
        const data = response.data;
        if (Array.isArray(data)) {
          setItems(data); // Only set items if the data is an array
        } else {
          console.error("Unexpected response format:", data);
          setError("Invalid data format received from server");
        }
      })
      .catch((error) => {
        console.error("There was an error fetching the items!", error);
        setError("Failed to fetch items. Please try again later.");
      });
  }, []);

  return (
    <>
      <div className="mx-10">
          <h1 className="text-purple-100">Languages</h1>
          {error ? (
            <p style={{ color: "red" }}>{error}</p>
          ) : (
            <ul className="flex space-x-6">
              {items.map((item) => (
                <li
                    className="text-purple-100 hover:text-purple-400 transition duration-200 text-xl font-semibold hover:underline "
                    key={item.id}
                >   
                    <Link to={`/${item.id}`}>
                        {item.id}: {item.name}
                    </Link>
                </li>
              ))}
            </ul>
          )}
      </div>
    </>
  );
}

export default HomePage;
