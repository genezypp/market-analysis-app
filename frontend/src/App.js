import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import DeviceManagement from './components/DeviceManagement';
import LoginForm from './components/LoginForm';
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
        </Switch>
      </div>
    </Router>
  );
};

export default App;
