import axios from 'axios'
import { all, call, put, takeEvery,fork } from 'redux-saga/effects'
import { LOGIN_FAILURE, LOGIN_SUCCESS,LOGIN_REQUEST, LOGOUT_SUCCESS, LOGOUT_FAILURE, LOGOUT_REQUEST, USER_LOADING_SUCCESS, USER_LOADING_FAILURE, USER_LOADING_REQUEST, REGISTER_SUCCESS, REGISTER_FAILURE, REGISTER_REQUEST, CLEAR_ERROR_REQUEST, CLEAR_ERROR_FAILURE, CLEAR_ERROR_SUCCESS } from '../types'

// Login

const loginUserAPI = (loginData) => {
    const config = {
        header:{
            "Content-Type":"application/json"
        }
    }
    return axios.post('api/auth',loginData,config)
}

function* loginUser(action){
    try{
        const result = yield call(loginUserAPI,action.payload)
        yield put({
            type:LOGIN_SUCCESS,
            payload:result.data
        })
    }catch(e){
        yield put({
            type:LOGIN_FAILURE,
            payload:e.response
        })
    }
}

function* watchLoginUser(){
    yield takeEvery(LOGIN_REQUEST,loginUser)
}




function* logout(action){
    try{
        yield put({
            type:LOGOUT_SUCCESS,
        })
    }catch(e){
        yield put({
            type:LOGOUT_FAILURE,
            payload:e.response
        })
    }
    
}

function* watchlogout(){
    yield takeEvery(LOGOUT_REQUEST,logout)
}



const userLoadingAPI = (token) => {
    const config = {
        headers:{
            "Content-Type":"application/json",
        },
    }
    if(token){
        config.headers["x-auth-token"] = token
    }
    const result = axios.get('api/auth/user', config)
    return result
}

function* userLoading(action){
    try{
        const result = yield call(userLoadingAPI,action.payload)
        yield put({
            type:USER_LOADING_SUCCESS,
            payload:result.data
        })
    }catch(e){
        yield put({
            type:USER_LOADING_FAILURE,
            payload:e.response
        })
    }
}

function* watchUserLoading(){
    yield takeEvery(USER_LOADING_REQUEST,userLoading)
}

//REGISTER


const registerUserAPI = (req) => {
    return axios.post('api/user',req)
}

function* registerUser(action){
    try{
        const result = yield call(registerUserAPI,action.payload)
        yield put({
            type:REGISTER_SUCCESS,
            payload:result.data
        })
    }catch(e){
        yield put({
            type:REGISTER_FAILURE,
            payload:e.response
        })
    }
}

function* watchregisterUser(){
    yield takeEvery(REGISTER_REQUEST,registerUser)
}


//CLEAR ERROR

function* clearError(){
    try{
        yield put({
            type:CLEAR_ERROR_SUCCESS,
        })
    }catch(e){
        yield put({
            type:CLEAR_ERROR_FAILURE,
        })
    }
}

function* watchclearError(){
    yield takeEvery(CLEAR_ERROR_REQUEST,clearError)
}



export default function* authSaga() {
    yield all([
        fork(watchLoginUser),
        fork(watchlogout),
        fork(watchUserLoading),
        fork(watchregisterUser),
        fork(watchclearError),
    ])
}