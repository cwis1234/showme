import React from 'react';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';

class List extends React.Component {

    handleCellClick = (e)=>{
        console.log(e.target.textContent);
    }

    render() {
        return (
            <TableRow onClick={this.handleCellClick}>
                <TableCell>{this.props.num}</TableCell>
                <TableCell>{this.props.title}</TableCell>
                <TableCell>{this.props.name}</TableCell>
                <TableCell>{this.props.hit}</TableCell>
                <TableCell>{this.props.createAt}</TableCell>
            </TableRow>
        )
    }
}

export default List;