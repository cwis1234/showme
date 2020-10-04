import { POST_LOADING_FAILURE, POST_LOADING_REQUEST, POST_LOADING_SUCCESS } from '../types'
import axios from 'axios'
import { all, call, put, takeEvery,fork } from 'redux-saga/effects'
import { push } from 'connected-react-router'


const loadPostAPI = () => {
    return axios.get("/api/post")
}

function* loadPosts() {
    try{
        const result = yield call(loadPostAPI)
        yield put({
            type:POST_LOADING_SUCCESS,
            payload:result.data

        })
    }catch(e){
        yield put({
            type:POST_LOADING_FAILURE,
            payload:e
        })
        yield push("/")
    }
}

function * watchLoadPost() {
    yield takeEvery(POST_LOADING_REQUEST,loadPosts)
}

export default function* postSaga(){
    yield all([
        fork(watchLoadPost),
    ]);
}