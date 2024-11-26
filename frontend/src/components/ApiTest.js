import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ApiTest = () => {
    const [message, setMessage] = useState('');
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get('/api/test')
            .then(response => {
                setMessage(response.data.message); // Ustaw komunikat na dane z backendu
            })
            .catch(error => {
                setError('Error connecting to API');
                console.error(error); // Zaloguj błąd w konsoli
            });
    }, []);

    return (
        <div>
            <h1>API Test</h1>
            {error ? <p style={{ color: 'red' }}>{error}</p> : <p>{message}</p>}
        </div>
    );
};

export default ApiTest;
