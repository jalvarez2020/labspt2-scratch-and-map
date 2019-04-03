import React, {Component} from "react";
import axios from 'axios'
import { Dropdown } from "semantic-ui-react";

class SidebarDrop extends Component {
  state = {
    options: []
  };

  async componentDidMount() {
    await axios
      .get(`${process.env.REACT_APP_BACKEND_URL}/api/users`)
      .then(res => {
        this.setState({
          options: res.data.users
        });
      });
  }

  handleInputChange = e => {
    this.setState({
      [e.target.name]: e.target.value
    });
  };

  render() {
    console.log("OPTIONS DATA", this.state.options);
    return (
      <div>
        <Dropdown
          onChange={this.handleInputChange} 
          placeholder="Select Friend"
          clearable
          fluid
          multiple
          search
          selection
          options={this.state.options.map((item) => <option key={item.id} value={item.id}>{item.username}</option>)}
          />
      </div>
    );
  }
}
export default SidebarDrop;
