import './App.css';
import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Copyright from './components/Copyright/Copyright';
import BottomTab from './components/BottomTab/BottomTab';

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
      <BottomTab label="Copyright">
        <Copyright/>
      </BottomTab>
    </div>
  );
}

export default App;
