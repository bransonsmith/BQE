import React from 'react';
import './BottomTab.css';

export default class BottomTab extends React.Component  {

  constructor(props) {
    super(props);
    this.state = {
        expanded: false
    }

    this.toggle = this.toggle.bind(this);
    this.render = this.render.bind(this);
  } 

  toggle() {
      const currentExpandedValue = this.state.expanded;
      this.setState({ expanded: !currentExpandedValue })
  }

  render() {
      return(
        <div className="bottom-tab" onClick={this.toggle}>
            { this.state.expanded
            ? <div className="expanded-tab">
                {this.props.children}
                <div className="close">close</div>
              </div>
            : <div className="collapsed-tab">
                <div className="tab-label"> {this.props.label} </div>
              </div>
            }
        </div>
      );
  }
}
