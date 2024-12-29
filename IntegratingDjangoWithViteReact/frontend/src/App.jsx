import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
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
      <div className="App">
        <header className="App-header">
          <h1>Welcome to My App</h1>
        </header>
        <div>
          <h1>Languages</h1>
          {error ? (
            <p style={{ color: "red" }}>{error}</p>
          ) : (
            <ul>
              {items.map((item) => (
                <li
                  key={item.id}
                  style={{
                    listStyleType: "none",
                    padding: "10px",
                    fontSize: "20px",
                  }}
                >
                  {item.name}
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </>
  );
}

export default App;
