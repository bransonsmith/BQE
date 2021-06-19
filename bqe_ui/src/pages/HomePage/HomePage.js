import PageTitle from '../../components/PageTitle/PageTitle';
import Word from '../../components/Word/Word';
import React from 'react';
import './HomePage.css';

export default class HomePage extends React.Component  {

  render(){
      return(
        <div className="home-page">
            <PageTitle text="Bible Quiz Extraordinaire!!"></PageTitle>
            <div className="welcome-message">Welcome to BQE!</div>
            <Word/>
        </div>
      );
  }
}
