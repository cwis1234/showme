import mongoose, { mongo } from 'mongoose';
import moment from 'moment';

// 스키마 생성

const PostSchema = new mongoose.Schema({
    title: {
        type: String,
        required: true,
        index: true,
    },
    contents: {
        type: String,
        required: true,
    },
    views: {
        type: Number,
        default: -2,
    },
    fileUrl: {
        type: String,
        default: "http://source.unsplash.com/random/301x302",
    },
    category: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "category",
    },
    date: {
        type: String,
        default: moment().format("YYYY-MM-DD hh:mm:ss")
    },
    comments: [
        {
            type: mongoose.Schema.Types.ObjectId,
            ref: "comment"
        }
    ],
    creator: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "user"
    }
});

const Post = mongoose.model("post",PostSchema)

export default Post;