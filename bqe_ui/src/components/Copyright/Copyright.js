import React from 'react';
import './Copyright.css';

export default class Copyright extends React.Component  {

  render(){
      return(
        <div className="esv-copyright">
            <div className="esv-copyright-text">
                Scripture quotations marked “ESV” are from the ESV® Bible 
                (The Holy Bible, English Standard Version®), copyright © 2001 by Crossway,
                a publishing ministry of Good News Publishers. Used by permission. 
                All rights reserved. You may not copy or download more than 500 consecutive
                verses of the ESV Bible or more than one half of any book of the ESV Bible.
            </div>
        </div>
      );
  }
}
