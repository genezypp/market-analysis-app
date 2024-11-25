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
                setMessage('Urz¹dzenie zosta³o dodane!');
            })
            .catch(error => {
                setMessage('Wyst¹pi³ problem przy dodawaniu urz¹dzenia.');
            });
    };

    return (
        <div className="device-management">
            <h2>Dodaj Urz¹dzenie</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Nazwa urz¹dzenia:
                    <input type="text" value={deviceName} onChange={(e) => setDeviceName(e.target.value)} required />
                </label>
                <label>
                    Kategoria urz¹dzenia:
                    <input type="text" value={deviceCategory} onChange={(e) => setDeviceCategory(e.target.value)} required />
                </label>
                <button type="submit">Dodaj urz¹dzenie</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default DeviceManagement;
