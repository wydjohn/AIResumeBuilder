import React, { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

// Lazy load components
const ResumeBuilder = lazy(() => import('./ResumeBuilder'));
const TemplateSelector = lazy(() => import('./TemplateSelector'));

class App extends React.Component {
  render() {
    return (
      <Router>
        <div>
          {/* Use Suspense to wrap lazy-loaded components */}
          <Suspense fallback={<div>Loading...</div>}>
            <Switch>
              <Route path="/resume-builder" component={ResumeBuilder} />
              <Route path="/template-selector" component={TemplateSelector} />
              <Route path="/" exact component={ResumeBuilder} />
            </Switch>
          </Suspense>
        </div>
      </Router>
    );
  }
}

export default App;