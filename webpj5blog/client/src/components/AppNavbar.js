import React, { Fragment, useCallback,useState,useEffect } from 'react';
import {Button,Nav,Navbar,Container, NavbarToggler, Collapse, NavItem, Form} from 'reactstrap';
import {Link} from 'react-router-dom';
import LoginModal from './auth/LoginModal'
import RegisterModal from './auth/RegisterModal'
import { useDispatch, useSelector } from 'react-redux';
import { LOGOUT_REQUEST } from '../redux/types';

const AppNavebar = () => {

    const [isOpen,setIsOpen] = useState(false)
    const {isAuthenticated,user,userRole} = useSelector((state)=>state.auth)
    
    const dispatch = useDispatch()
    const onLogout = useCallback(()=>{
        dispatch({
            type:LOGOUT_REQUEST
        })
    },[dispatch])

    useEffect(()=>{
        setIsOpen(false)
    },[user])

    const handleToggle = () => {
        setIsOpen(!isOpen)
    }

    const addPostClick = () => {

    }

    const authLink = (
        <Fragment>
            <NavItem>
                {userRole === "Admin" ? (
                    <Form className="col mt-2">
                        <Link to="post" className="btn btn-success block text-white px-3" onClick={addPostClick}>
                            글쓰기
                        </Link>
                    </Form>
                ) : ""}
            </NavItem>
            <NavItem className="d-flex justify-content-center">
                <Form className="col mt-2">
                    {user && user.name ? (
                        <Link to ="#">
                        <Button outline color="light" className="px-3" block>
                            <strong>{user ? `Welcome ${user.name}`:""}</strong>
                        </Button>
                        </Link>
                    ):(
                        <Button outline color="light" className="px-3" block>
                            <strong>NO USER</strong>
                        </Button>
                    )}
                </Form>
            </NavItem>
            <NavItem>
                <Form className="col">
                    <Link onClick={onLogout} to="#">
                        <Button outline color="light" className="mt-2" block>
                            Logout
                        </Button>
                    </Link>
                </Form>
            </NavItem>
        </Fragment>
    )

    const guestLink = (
        <Fragment>
            <NavItem>
                <RegisterModal/>
            </NavItem>
            <NavItem>
                <LoginModal/>
            </NavItem>
        </Fragment>
    )

    return(
        <Fragment>
            <Navbar color="dark" expand="lg" className="sticky-top">
                <Container>
                    <Link to="/" className="text-white text-decoration-none">
                        Main
                    </Link>
                    <NavbarToggler onClick={handleToggle}/>
                    <Collapse isOpen={isOpen} navbar>
                        <Nav className="ml-auto d-flex justify-content-around" navbar>
                            {isAuthenticated ? (authLink) : guestLink}
                        </Nav>
                    </Collapse>
                </Container>
            </Navbar>
        </Fragment>
    )
}
export default AppNavebar;