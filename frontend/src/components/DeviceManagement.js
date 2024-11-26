import React, { useState } from 'react';
import axios from 'axios';

const DeviceManagement = () => {
    const [deviceName, setDeviceName] = useState('');
    const [deviceCategory, setDeviceCategory] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();

        axios.post('/api/devices', {
            name: deviceName,
            category: deviceCategory
        })
            .then(response => {
                setMessage('Urzadzenie zostalo dodane!');
            })
            .catch(error => {
                setMessage('Wystapil problem przy dodawaniu urzadzenia.');
            });
    };

    return (
        <div className="device-management">
            <h2>Dodaj Urz퉐zenie</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Nazwa urz퉐zenia:
                    <input type="text" value={deviceName} onChange={(e) => setDeviceName(e.target.value)} required />
                </label>
                <label>
                    Kategoria urz퉐zenia:
                    <input type="text" value={deviceCategory} onChange={(e) => setDeviceCategory(e.target.value)} required />
                </label>
                <button type="submit">Dodaj urz퉐zenie</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default DeviceManagement;
