import React from "react";
import { RouterProvider, createBrowserRouter } from "react-router-dom";

import HomePage from "./Pages/HomePage";
import DescriptionPage from "./Pages/DescriptionPage";

function App(){
  const router = createBrowserRouter([
    {
      path: "/",
      element: <HomePage />
    },
    {
      path: "/:id",
      element: <DescriptionPage />
    },
  ]);

  return (
    <div className="bg-black min-h-[100vh] w-full">
      <div className="flex flex-col w-[80%] mx-auto bg-slate-900 min-h-[100vh]">
        <header>
          <h1 className="text-center text-purple-100 text-3xl font-bold">
            Welcome to my App
          </h1>
        </header>
        <RouterProvider router={router}></RouterProvider>
      </div>
    </div>
  );
}

export default App;