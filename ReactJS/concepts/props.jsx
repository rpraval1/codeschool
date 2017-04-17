{/*
:Author: Pravallika
:Description: Usage of props: pass values from a parent component to a child component.
              A child component can have values handed to it either through attributes, or
              through nested content.

*/}

import React from 'react';

export default class TodoBox extends React.Component {
    render() {
        return (
            <div className="todoBox">
                <h1>Todos</h1>
                <TodoList />
                <TodoForm />
            </div>
        );
    }
}

class TodoList extends React.Component {

  render(){
    return (
      <div class="todoList">
        <table style={{border: "2px solid black"}}>
            <tbody>
            <Todo title="Shopping">Milk</Todo>
            <Todo title="Hair cut">13:00</Todo>
            </tbody>
        </table>
      </div>
    )
  }
}

class Todo extends React.Component {

  render(){
    const {title} = this.props
    return (
      <tr>
        <td style="border:1px solid black;">{title}</td>
        <td style="border:1px solid black;">{this.props.children}</td>
      </tr>
    )
  }
}

class TodoForm extends React.Component {

  render(){
    return (
      <div class="todoForm">
        I am a TodoForm.
      </div>
    )
  }
}
