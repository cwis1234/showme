import mongoose, { mongo } from 'mongoose';
import moment from 'moment';

// 스키마 생성

const UserSchema = new mongoose.Schema({
    name:{
        type:String,
        required: true,
    },
    email:{
        type:String,
        required:true,
        unique:true,
    },
    password:{
        type:String,
        required:true,
    },
    role:{
        type:String,
        enum:["Admin","User"],
        default:"User",
    },
    register_date:{
        type:Date,
        default:moment().format("YYYY-MM-DD hh:mm:ss"),
    },
    comment:[
        {
            post_id:{
                type:mongoose.Schema.Types.ObjectId,
                ref:"post",
            },
            comment_id:{
                type:mongoose.Schema.Types.ObjectId,
                ref:"comments",
            },
        },
    ],
    post:[
        {
            type:mongoose.Schema.Types.ObjectId,
            ref:"post",
        },
    ],
});

const User = mongoose.model("user",UserSchema);

export default User;