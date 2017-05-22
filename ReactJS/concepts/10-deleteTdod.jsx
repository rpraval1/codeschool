{/*
:Author: Pravallika
:Description: Usage of props: pass values from a parent component to a child component.
              A child component can have values handed to it either through attributes, or
              through nested content.

*/}

import React from 'react';
import PropTypes from 'prop-types';

export default class TodoBox extends React.Component {
    render() {
        return (
            <div className="todoBox">
                <h1>Todos</h1>
                <TodoList data={this.props.data}/>
                <TodoForm />
            </div>
        );
    }
}

class TodoList extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      data: this.props.data,
      titleValue: "",
      detailValue: ""
    }
  }

  changeTitle(e){
    this.setState({
      titleValue: e.target.value
    })
  }

  changeDetail(e){
    this.setState({
      detailValue: e.target.value
    })
  }

  addTodo(){
    let newData = this.state.data;
    newData.push({
      title: this.state.titleValue,
      detail: this.state.detailValue
    });
    this.setState({
      data: newData,
      titleValue: "",
      detailValue: ""
    })
  }

  render(){
    var todo = this.state.data.map(obj => {
      return <Todo title={obj.title} key={obj.title}>{obj.detail}</Todo>;
    })
    return (
      <div className="todoList">
        <div>
          Title:<input type="text" value={this.state.titleValue} onChange={this.changeTitle.bind(this)} />
        Detail:<input type="text" value={this.state.detailValue} onChange={this.changeDetail.bind(this)} />
      <button onClick={this.addTodo.bind(this)}>Add</button>
        </div>
        <table style={{border: "2px solid black"}}>
            <tbody>
              {todo}
            </tbody>
        </table>
      </div>
    )
  }
}

class Todo extends React.Component {
  constructor(props){
    super(props);
    this.state={
      checked: false,
      TodoStyle: style.notCheckedTodo
    }
  }

  handleChange(e){
    this.setState({
      checked: e.target.checked
    })
    if(e.target.checked){
      this.setState({
        TodoStyle: style.checkedTodo
      })
    }else{
      this.setState({
        TodoStyle: style.notCheckedTodo
      })
    }
  }

  _onDelete(){
    this.props.onDelete(this.props.title);
  }
  render(){
    const {title} = this.props
    return (
      <tr style={this.state.TodoStyle}>
        <td style={style.tableContent}>
          <button onClick={this._onDelete.bind(this)}>X</button>
        </td>
        <td style={style.tableContent}>
          <input type="checkbox" checked={this.state.checked} onChange={this.handleChange.bind(this)} />
        </td>
        <td style={style.tableContent}>{title}</td>
        <td style={style.tableContent}>{this.props.children}</td>
      </tr>
    )
  }
}

Todo.propTypes = {
  title: PropTypes.string.isRequired
};
class TodoForm extends React.Component {

  render(){
    return (
      <div className="todoForm">I am a TodoForm.</div>
    )
  }
}



let style = {
  checkedTodo: {
      textDecoration: "line-through"
  },
  notCheckedTodo: {
      textDecoration: "none"
  },
  tableContent: {
      border: "1px solid black"
  }
};
