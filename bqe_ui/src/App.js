import './App.css';
import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

// Load pages when they are needed
const HomePage = lazy(() => import('./pages/HomePage/HomePage'));
const PageNotFoundPage = lazy(() => import('./pages/PageNotFoundPage/PageNotFoundPage'));

function App() {

  return (
    <div className="app">
      <Router>
        <Suspense fallback={<div>Loading...</div>}>
          <Switch>
            <Route exact path="/" 
              component={HomePage}
            />

            {/* If no path above matched, show page not found. */}
            <Route path="**" 
              component={PageNotFoundPage}
            />
          </Switch>
        </Suspense>
      </Router>
    </div>
  );
}

export default App;
