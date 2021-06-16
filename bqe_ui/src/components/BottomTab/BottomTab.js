import React, {useState} from 'react';
import './BottomTab.css';

export default function BottomTab(props)  {

  const [expanded, setExpanded] = useState(false);

  return(
    <div className="bottom-tab" onClick={() => setExpanded(!expanded)}>
      { expanded
      ? <div className="expanded-tab">
          {props.children}
          <div className="close">close</div>
        </div>
      : <div className="collapsed-tab">
          <div className="tab-label"> {props.label} </div>
        </div>
      }
    </div>
  );
}
