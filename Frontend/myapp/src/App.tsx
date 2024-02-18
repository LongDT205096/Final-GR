import React from 'react';
import axios from 'axios';


type Account = {
    email: string;
    password: string;
};

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://localhost:8000';


class App extends React.Component<{}, Account> {
    constructor(props: any) {
        super(props);
        this.state = {
            email: '',
            password: '',
        };

        this.handleEmailChange = this.handleEmailChange.bind(this);
        this.handlePasswordChange = this.handlePasswordChange.bind(this);
        this.handleLogin = this.handleLogin.bind(this);
        this.handleLogout = this.handleLogout.bind(this);
    }

    handleEmailChange(event: { target: { value: string; }; }) {
        this.setState({ email: event.target.value });
    };

    handlePasswordChange (event: { target: { value: string; }; }) {
        this.setState({ password: event.target.value });
    };

    handleLogin = (event: { preventDefault: () => void; }) => {
        event.preventDefault();
        const user = {
            email: this.state.email,
            password: this.state.password,
        };

        axios.post('/account/login/',
            {  
                email: user.email,
                password: user.password
            },
            {
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': 'csrftoken',
                }
            })
            .then(res => {
                console.log(res);
                console.log(res.data);
            })
            .catch(error => {
                console.log(error);
            });
    };

    handleLogout = (event: { preventDefault: () => void; }) => {
        event.preventDefault();
        axios.post('/account/logout/', 
        {
            headers: {
                'withCredentials': 'true'
            }
        })
            .then(res => {
                console.log(res);
                console.log(res.data);
            })
            .catch(error => {
                console.log(error);
            });
    };
    
    render() {
        return (
            <div>
                <form onSubmit={this.handleLogin}>
                    <input
                        type="text"
                        placeholder="email"
                        value={this.state.email}
                        onChange={this.handleEmailChange}
                    />
                    <input
                        type="password"
                        placeholder="password"
                        value={this.state.password}
                        onChange={this.handlePasswordChange}
                    />
                    <button type="submit" onClick={this.handleLogin}>Login</button>
                </form>

                <form onSubmit={this.handleLogout}>
                    <button type="submit" onClick={this.handleLogout}>Logout</button>
                </form>
            </div>
        );
    }

}


export default App;
