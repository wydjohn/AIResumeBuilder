import React, { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';

const ResumeBuilder = lazy(() => import('./ResumeBuilder'));
const TemplateSelector = lazy(() => import('./TemplateSelector'));

function App() {
  return (
    <Router>
      <Suspense fallback={<div>Loading...</div>}>
        <Switch>
          <Route exact path="/" component={ResumeBuilder} />
          <Route path="/resume-builder" component={ResumeBuilder} />
          <Route path="/template-selector" component={TemplateSelector} />
        </Switch>
      </Suspense>
    </Router>
  );
}

export default App;