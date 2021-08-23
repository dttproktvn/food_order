import React, { Component } from 'react';
import LoginForm from '../components/loginComponents/Form'
import '../styles/style.css'

class Login extends Component {
    componentDidMount() {
        document.title = "login"
    }
    render() {
        return(            
            <div className="container-login100">
                <LoginForm/>             
            </div>
        )
    }
}

export default Login;