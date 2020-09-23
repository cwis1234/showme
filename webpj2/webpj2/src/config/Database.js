var mongoose = require('mongoose');
var express = require('express');
var bodyPaser = require('body-parser');
var app = express();
var cors = require('cors');

app.use(cors());
app.use(express.json());

var postSchema = mongoose.Schema({
    num:{type:String,required:true},
    title:{type:String,required:true},
    content:{type:String,required:true},
    createAt:{type:Date,default:Date.now},
    name:{type:String,required:true},
    pw:{type:String,required:true},
    hit:{type:String,default:0,},
    comments:[
        {
            type:mongoose.Schema.Types.ObjectId,
            ref:"Comment"
        }
    ],
});

mongoose.connect('mongodb+srv://admin:1234@cluster0.qaefs.gcp.mongodb.net/WebProject?retryWrites=true&w=majority');

const db = mongoose.connection;
db.on('error',function () {
  // error 처리
});
db.once('open',function(){
    console.log("connected");
});

var Board = mongoose.model('board',postSchema);

app.listen(3002,function(req,res){
    console.log("3002");
})

app.get('/all/',function(req,res){
    Board.find({}).sort({createAt:1}).find(function(err,posts){
        res.json(posts);
    })
    // Board.find({sort:createAt},function(err,docs){
    //     res.json(docs);
    // })
});

app.post('/write/',function(req,res){
    console.log(req.body)
    var board = new Board({
        num:"0",
        title:req.body.title,
        content:req.body.content,
        name:req.body.name,
        pw:req.body.pw,
    });
    console.log(board);
    board.save(function(err,boa){
        if(err) return console.error(err);
        console.log(boa.title + "save collection");
    })
})