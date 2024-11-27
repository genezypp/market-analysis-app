import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import DeviceManagement from "./components/DeviceManagement";
import LoginForm from "./components/LoginForm";
import ApiTest from "./components/ApiTest";

const App = () => {
    return (
        <Router>
            <div className="app-container">
                <h1>Market Analysis App</h1>
                <Routes>
                    <Route path="/" element={<Dashboard />} />
                    <Route path="/device-management" element={<DeviceManagement />} />
                    <Route path="/login" element={<LoginForm />} />
                    <Route path="/api-test" element={<ApiTest />} />
                </Routes>
            </div>
        </Router>
    );
};

export default App;
