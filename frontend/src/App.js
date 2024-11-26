import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import DeviceManagement from './components/DeviceManagement';
import LoginForm from './components/LoginForm';
import ApiTest from './components/ApiTest'; // Import testowego komponentu
import './style.css';

const App = () => {
  return (
    <Router>
      <div className="app">
        <h1>Market Analysis App</h1>
        <Switch>
          <Route path="/" exact component={Dashboard} />
          <Route path="/device-management" component={DeviceManagement} />
          <Route path="/login" component={LoginForm} />
          <Route path="/api-test" component={ApiTest} /> {/* Dodanie nowej trasy */}
        </Switch>
      </div>
    </Router>
  );
};

export default App;
