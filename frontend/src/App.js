import {
  BrowserRouter as Router,
  Route,
  Switch
} from "react-router-dom";
import Home from './pages/HomePage'
import Login from './pages/Login'
function App() {
  return (    
      <Router>
        <Switch>
          <Route path="/" exact><Home/></Route>
          <Route path="/login" exact><Login/></Route> 
        </Switch>
      </Router>         
  );
}
export default App;
