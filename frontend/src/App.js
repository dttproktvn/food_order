import {
  BrowserRouter as Router,
  Route,
  Switch
} from "react-router-dom";
import Home from './pages/Home'
import Login from './pages/Login'
import Signup from "./pages/Signup";
function App() {
  return (    
      <Router>
        <Switch>
          <Route path="/" exact><Home/></Route>
          <Route path="/login" exact><Login/></Route> 
          <Route path="/Signup" exact><Signup/></Route> 
        </Switch>
      </Router>         
  );
}
export default App;
