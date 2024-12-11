import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import ResumeBuilder from './ResumeBuilder';
import TemplateSelector from './TemplateSelector';

class App extends React.Component {
  render() {
    return (
      <Router>
        <div>
          <Switch>
            <Route path="/resume-builder" component={ResumeBuilder} />
            <Route path="/template-selector" component={TemplateSelector} />
            <Route path="/" exact component={ResumeBuilder} />
          </Switch>
        </div>
      </Router>
    );
  }
}

export default App;