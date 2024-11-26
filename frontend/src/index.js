// src/index.js
import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css"; // Import globalnych stylów

// Prosty komponent główny aplikacji
const App = () => {
  return (
    <div className="app-container">
      <h1>Market Analysis App is working!</h1>
    </div>
  );
};

// Renderowanie aplikacji w elemencie "root"
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
