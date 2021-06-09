import React from 'react';
import './PageTitle.css';

export default function PageTitle(props) {
  return(
    <div className="page-title">
        <h2 className="page-title-text">
            {props.text}
        </h2>
    </div>
  );
}
