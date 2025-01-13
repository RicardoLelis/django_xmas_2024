import { useEffect, useState } from 'react'

import './App.css'

function App() {
  const [books, setBooks] = useState([]);
  const [title, setTitle] = useState("");
  const [releaseYear, setReleaseYear] = useState(0);
  const [error, setError] = useState("");
  const [newTitle, setNewTitle] = useState("");
  
  useEffect(() => {
    fetchBooks();
  }, [])

  const fetchBooks = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8001/api/books/")
      if (!response.ok){
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json()
      setBooks(data)
    } catch (error) {
      setError(`Failed to fetch books: ${error.message}`);
      console.log(error);      
    }
  };

  const clearForm = () => {
    setTitle("");
    setReleaseYear("");
    setError("");
  }

  const addBook = async () => {
    // Basic validation
    if (!title.trim()){
      setError("Please enter a title!");
      return;
    }

    const year = parseInt(releaseYear);
    if (isNaN(year) || year < 1000 || year > 9999){
      setError("Please enter a valid year (1000 - 9999");
      return;
    }

    const bookData = {
      title: title.trim(),
      release_year: year,
    };

    try {
        const response = await fetch("http://127.0.0.1:8001/api/books/create/", {
          method: "POST",
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(bookData),
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        console.log("Creating...", data);
        
        // Update the books list and clear the form
        await fetchBooks();
        clearForm();

        // setBooks((prev) => [...prev, data]);
    } catch (error) {
      setError(`Failed to add book: ${error.message}`);
      console.error("Add book error:", error);
    }
  }

  const updateTitle = async (pk, release_year) => {
    // Basic validation
    if(!newTitle.trim()){
      setError("Please enter the new title!");
      return;
    }

    const bookData = {
      title: newTitle.trim(),
      release_year,
    };

    try {
        const response = await fetch(`http://127.0.0.1:8001/api/books/${pk}/`, {
          method: "PUT",
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(bookData),
        });

        if (!response.ok){
          const errorData = await response.json();
          throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json()
        console.log("Updating...", data);

        setBooks((prev) => prev.map((book) => {
          if (book.id === pk){
            return data;
          } else {
            return book;
          }
        })
      );
      setNewTitle(''); // clear input after successful update
      setError(''); // clear any existing errors
    } catch (error) {
      setError(`Failed to update title: ${error.message}`);
      console.error("Update title error:", error);
    }
  };

  const deleteBook = async (pk) => {

    try {
      const response = await fetch(`http://127.0.0.1:8001/api/books/${pk}/`, {
        method: "DELETE",
      });

      if (!response.ok){
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      setBooks((prev) => prev.filter((book) => book.id !== pk))
      setError(''); // clear any existing errors
    } catch (error) {
      setError(`Failed to delete book: ${error.message}`);
      console.error("Delete book error:", error);
    }
  };

  return (
    <>
    <h1>Book Website</h1>

    <div>
      <input 
        type="text" 
        placeholder="Book title.." 
        onChange={(e) => setTitle(e.target.value)}
        />
      <input 
        type="number" 
        placeholder="Release Year.." 
        onChange={(e) => setReleaseYear(e.target.value)}
      />
      <button onClick={addBook}>Add Book</button>
    </div>
    {books.map((book) => (
      <div key={book.id}>
        <p>Title: {book.title}</p>
        <p>Release Year: {book.release_year}</p> 
        <input 
          type="text" 
          placeholder='New Title...' 
          onChange={(e) => setNewTitle(e.target.value)}
        />
        <button onClick={() => updateTitle(book.id, book.release_year)}>Change Title</button>
        <button onClick={() => deleteBook(book.id)}>Delete</button>
      </div>
    ))}
    </>
  )
}

export default App
