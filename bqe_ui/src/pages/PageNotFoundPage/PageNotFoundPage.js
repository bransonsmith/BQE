import React from 'react';
import './PageNotFoundPage.css';
import PageTitle from '../../components/PageTitle/PageTitle';

export default class PageNotFoundPage extends React.Component  {

  goToHomePage() {
    window.location.href = "/";
  }

  render(){
      return(
        <div className="page-not-found-page">
            <PageTitle text="Page Not Found"></PageTitle>
            <button className="go-home" onClick={this.goToHomePage}>Home</button>
        </div>
      );
  }
}
