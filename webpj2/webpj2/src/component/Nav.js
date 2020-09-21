import React from 'react';

import {withStyle} from '@material-ui/core/styles';
import AppBar from '@material-ui/core/Appbar';
import Drawer from '@material-ui/core/Drawer';
import MenuItem from '@material-ui/core/MenuItem';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/core/Menu';



const styles = {
    root:{
        flexGrow: 1,
    },
    menuButton:{
        marginRight:'auto',
    },
};

export default class Nav extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            toggle:false
        };
        this.homeClick = this.homeClick.bind(this);
        this.realClick = this.realClick.bind(this);
        this.vedioClick = this.vedioClick.bind(this);
        this.freeClick = this.freeClick.bind(this);
        this.repoClick = this.repoClick.bind(this);
        this.content = <div>홈</div>;
    }
    
    handleDrawerToggle = () => this.setState({toggle:!this.state.toggle})

    homeClick(){
        this.setState({toggle:!this.state.toggle});
        this.content = <div>홈</div>
    }
    
    freeClick(){
        this.setState({toggle:!this.state.toggle});
        this.content = <div>자게</div>
    }
    
    repoClick(){
        this.setState({toggle:!this.state.toggle});
        this.content = <div>저장소</div>
    }

    realClick(){
        this.setState({toggle:!this.state.toggle});
        this.content = <div>실화</div>
    }

    vedioClick(){
        this.setState({toggle:!this.state.toggle});
        this.content = <div>실비</div>
    }

    render(){
        const {classes} = this.props;
        return(
            <div className={classes.root}>
                <AppBar position = "static">
                    <IconButton className={classes.menuButton} color = "inherit" onClick={this.handleDrawerToggle}>
                        <MenuIcon/>
                    </IconButton>
                </AppBar>
                <Drawer open={this.state.toggle}>
                    <MenuItem onClick={this.homeClick}>홈</MenuItem>
                    <MenuItem onClick={this.freeClick}>자유 게시판</MenuItem>
                    <MenuItem onClick={this.repoClick}>자료실</MenuItem>
                    <MenuItem onClick={this.realClick}>실시간 화제</MenuItem>
                    <MenuItem onClick={this.vedioClick}>화제 동영상</MenuItem>
                </Drawer>
                {this.content}
            </div>
        )
    }
}