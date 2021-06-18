import React from 'react';
import './Word.css';
import axios from 'axios';

export default class Word extends React.Component {
    constructor(props) {
        super(props);
        this.state = {word: null};

        this.render = this.render.bind(this);
    }
  
    componentDidMount() {
      axios.get(`https://bqe-api-staging.herokuapp.com/glossary/word/random/`)
        .then(res => {
          const word = res.data;
          this.setState({ word });
        })
    }
  
    render() {
        return(
            <div className="word">

                { this.state.word
                ? <div>
                    <div className="word-label">Word:</div>
                    <div className="word-value">{this.state.word.name}</div>
                  </div>
                : <div>
                    Loading...
                  </div>
                }
            </div>
        );
    }
  }
