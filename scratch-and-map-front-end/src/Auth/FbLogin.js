import React, { Component } from "react";
import { Button } from "semantic-ui-react";
import FacebookLogin from "react-facebook-login";

class FbLogin extends Component {
  constructor() {
    super();
    this.state = {};
  }

  handleInputChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  render() {
    return (
      <div className="login-register-wrapper">
        <FacebookLogin
          appId={process.env.REACT_APP_FB_APP_ID}
          autoLoad={true}
          fields="name,email,picture"
          onClick={this.handleInputChange}
          callback={response => {
            return <img src={response.picture.data.url} />;
          }}
        />
      </div>
    );
  }
}

export default FbLogin;