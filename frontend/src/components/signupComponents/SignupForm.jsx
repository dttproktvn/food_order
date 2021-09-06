import React, { Component } from 'react';
import '../../styles/style.css'
import loginLogo from "../../images/loginLogo.png"
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faEnvelope, faKey } from '@fortawesome/free-solid-svg-icons'
const SignupForm = () => (  
    <div class="wrap-login100">
    	<div class="login100-pic js-tilt">
            <img src={loginLogo}></img>
        </div>
    
    <form class="login100-form validate-form">
        <span class="login100-form-title">
            Create new account
        </span>
        <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
            <input class="input100" type="text" name="email" placeholder="Email" required/>
            <span class="focus-input100"></span>
            <span class="symbol-input100">
                <FontAwesomeIcon icon={faEnvelope} />
            </span>
        </div>

        <div class="wrap-input100 validate-input">
            <input class="input100" type="password" name="password" placeholder="Password" required/>
            <span class="focus-input100"></span>
            <span class="symbol-input100">
                <FontAwesomeIcon icon={faKey} />
            </span>
        </div>

        <div class="wrap-input100 validate-input">
            <input class="input100" type="password" name="password" placeholder="confirm password" required/>
            <span class="focus-input100"></span>
            <span class="symbol-input100">
                <FontAwesomeIcon icon={faKey} />
            </span>
        </div>

        <div class="container-login100-form-btn">
            <button class="login100-form-btn">
                Sign up
            </button>
        </div>

        <div style={{"padding-top":"30px","padding-left":"20px"}}>
				<a class="txt2" href="http://192.168.24.135:3000/login">
					If you have a account, login here
					<i class="fa fa-long-arrow-right m-l-5" aria-hidden="true"></i>
				</a>
	    </div>
    </form>
    </div>   
);
export default SignupForm;