import {all,fork} from 'redux-saga/effects';
import axios from 'axios';

import authSaga from './authSaga';
import dotenv from 'dotenv'
import postSaga from './postSaga';
dotenv.config()

axios.defaults.baseURL = "http://localhost:7000"

export default function* rootSaga(){
    
    yield all([
        fork(authSaga),
        fork(postSaga),
    ]);
}