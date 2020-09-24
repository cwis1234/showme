import React from 'react';
import { withStyle } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import TableBody from '@material-ui/core/TableBody';
import Dialog from '@material-ui/core/Dialog';
import DialogAction from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import List from './List';


const styles = {
    root: {
        flexGrow: 1,
    },
    menuButton: {
        marginRight: 'auto',
    },
};

class Freeboard extends React.Component {
    constructor(props) {
        super(props);
        // this.getBoardList = this.getBoardList.bind(this);
        this.state = {
            board: [],
            open: false,
            opencon:false,
            name: "",
            title: "",
            content: "",
            pw: "",
            number: "",
            num: 0,
            skip:0,
        }
    }
    componentDidMount() {
        fetch('http://116.255.94.41:3002/all/')
            .then((res) => {
                res.json().then((data) => {
                    this.setState({ board: data });
                })
            });
        
        fetch('http://116.255.94.41:3002/getnum/')
            .then((res) => {
                res.json().then((data) => {
                    this.setState({ num: data[0].num + 1 });
                })
            });

    }

    createContent = () => {
        this.setState({ open: true });
    }

    handleClose = () => {
        this.setState({
            open: false,
            name: "",
            title: "",
            content: "",
            pw: "",
            number: ""
        });
    }

    ValueChange = (e) => {
        let nextState = {};
        nextState[e.target.name] = e.target.value;
        this.setState(nextState);
    }

    contentSubmit = () => {
        console.log(this.state.num);
        fetch('http://116.255.94.41:3002/write/', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
            },
            body: JSON.stringify({
                'name': this.state.name,
                'title': this.state.title,
                'content': this.state.content,
                'pw': this.state.pw,
                'num': this.state.num,
            })
        })

        this.handleClose();


    }

    render() {
        return (
            <Table>
                <TableRow>
                    <TableCell>번호</TableCell>
                    <TableCell>제목</TableCell>
                    <TableCell>글쓴이</TableCell>
                    <TableCell>조회수</TableCell>
                    <TableCell>날짜</TableCell>
                </TableRow>
                <TableBody>
                    {
                        this.state.board.map(c => {
                            return <List num={c.num} title={c.title} name={c.name} hit={c.hit} createAt={c.createAt} />
                        })
                    }
                </TableBody>
                <Button variant="outlined" color="primary" size="large" onClick={this.createContent}>글쓰기</Button>
                <Dialog open={this.state.open} onClose={this.handleClose}>
                    <DialogTitle>글쓰기</DialogTitle>
                    <DialogContent>
                        <TextField label="닉네임" type="text" name="name" value={this.state.name} onChange={this.ValueChange} />
                        <br />
                        <TextField label="비밀번호" type="text" name="pw" value={this.state.pw} onChange={this.ValueChange} /><br />
                        <TextField label="제목" type="text" name="title" value={this.state.title} onChange={this.ValueChange} />
                        <br />
                        <TextField label="내용" type="text" name="content"
                            value={this.state.content} onChange={this.ValueChange}
                            multiline
                            rows="10" />
                        <br />
                    </DialogContent>
                    <DialogAction>
                        <Button variant="contained" color="primary" onClick={this.contentSubmit}>등록</Button>
                        <Button variant="outlined" color="primary" onClick={this.handleClose}>닫기</Button>
                    </DialogAction>
                </Dialog>
            </Table>
        )
    }
}


export default (Freeboard);