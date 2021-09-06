import React, { Component } from 'react';
import SignupForm from "../components/signupComponents/SignupForm"
import '../styles/style.css'

class Signup extends Component {
    componentDidMount() {
        document.title = "signup"
    }
    render() {
        return(            
            <div className="container-login100">
                <SignupForm/>
            </div>
        )
    }
}

export default Signup;