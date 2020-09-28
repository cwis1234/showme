import React from 'react';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import Dialog from '@material-ui/core/Dialog';
import DialogAction from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import { TabletAndroidTwoTone } from '@material-ui/icons';

class List extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            open: false,
            opencon:false,
            name: "",
            title: "",
            content: "",
            number: "",
            num: 0,
            skip:0,
        }
    }

    handleCellClick = (number)=>{
        this.setState({
            num:number,
        })
        var url = "http://116.255.94.41:3002/detail/" + number;

        fetch(url)
            .then((res) => {
                res.json().then((data) => {
                    this.setState({
                        name:data[0].name,
                        title:data[0].title,
                        content:data[0].content,
                        open:true,
                    });
                })
            });

    }

    handleDelete = () => {
        var number = this.state.num;
        console.log(number);
        fetch('http://116.255.94.41:3002/delete/', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
            },
            body: JSON.stringify({
                'num': number,
            })
        })

        this.handleClose();
    }

    handleClose = () => {
        this.setState({
            open: false,
            opencon:false,
            name: "",
            title: "",
            content: "",
            number: "",
            num: 0,
            skip:0,
        });
    }
    render() {
        return (
            <div>
            <TableRow>
                <TableCell>{this.props.num}</TableCell>
                <TableCell onClick={()=>{this.handleCellClick(this.props.num)}}>{this.props.title}</TableCell>
                <TableCell>{this.props.name}</TableCell>
                <TableCell>{this.props.hit}</TableCell>
                <TableCell>{this.props.createAt}</TableCell>
            </TableRow>
            <Dialog open={this.state.open} onClose={this.handleClose}>
                <DialogTitle>게시글</DialogTitle>
                <DialogContent>
                    <TextField label="닉네임" type="text" name="name" value={this.state.name} onChange={this.ValueChange} />
                    <br />
                    <TextField label="제목" type="text" name="title" value={this.state.title} onChange={this.ValueChange} />
                    <br />
                    <TextField label="내용" type="text" name="content"
                        value={this.state.content} onChange={this.ValueChange}
                        multiline
                        rows="10" />
                    <br />
                </DialogContent>
                <DialogAction>
                    <Button variant="contained" color="primary" onClick={this.handleClose}>닫기</Button>
                    <Button variant="contained" color="primary" onClick={this.handleDelete}>삭제</Button>
                </DialogAction>
            </Dialog>
            </div>
            
        )
    }
}

export default List;