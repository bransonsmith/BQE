import React from 'react';
import './PageTitle.css';

export default class PageTitle extends React.Component  {

  render(){
      return(
        <div className="page-title">
            <h2 className="page-title-text">
                {this.props.text}
            </h2>
        </div>
      );
  }
}
