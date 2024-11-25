import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Dashboard = () => {
  const [items, setItems] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Pobranie danych o przedmiotach z backendu
    axios.get('/api/items')
      .then(response => {
        setItems(response.data);
      })
      .catch(err => {
        setError('Wyst¹pi³ problem podczas ³adowania danych.');
      });
  }, []);

  return (
    <div className="dashboard">
      <h1>Dashboard - OLX Market Analysis</h1>
      {error && <p>{error}</p>}
      {!error && items.length > 0 ? (
        <table>
          <thead>
            <tr>
              <th>Nazwa</th>
              <th>Cena</th>
              <th>Kategoria</th>
            </tr>
          </thead>
          <tbody>
            {items.map(item => (
              <tr key={item.id}>
                <td>{item.name}</td>
                <td>{item.price}</td>
                <td>{item.category}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>Brak dostêpnych przedmiotów.</p>
      )}
    </div>
  );
};

export default Dashboard;
