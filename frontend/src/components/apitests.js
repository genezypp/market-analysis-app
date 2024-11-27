import React, { useEffect, useState } from "react";
import axios from "axios";

const ApiTest = () => {
    const [message, setMessage] = useState("");

    useEffect(() => {
        axios
            .get("/api/test")
            .then((response) => setMessage(response.data.message))
            .catch((error) => setMessage("Error fetching API"));
    }, []);

    return (
        <div>
            <h2>API Test</h2>
            <p>{message}</p>
        </div>
    );
};

export default ApiTest;
