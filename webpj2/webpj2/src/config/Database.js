var mongoose = require('mongoose');
var express = require('express');
var bodyPaser = require('body-parser');
var app = express();
var cors = require('cors');

app.use(cors());
app.use(express.json());

var postSchema = mongoose.Schema({
    num:{type:Number,required:true},
    title:{type:String,required:true},
    content:{type:String,required:true},
    createAt:{type:Date,default:Date.now},
    name:{type:String,required:true},
    pw:{type:String,required:true},
    hit:{type:Number,default:0,},
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
    Board.find({}).sort({num:-1}).find(function(err,posts){
        res.json(posts);
    })
    
    // Board.find({sort:createAt},function(err,docs){
    //     res.json(docs);
    // })
});

app.get('/getnum/',function(req,res){
    Board.find({}).sort({num:-1}).limit(1).find(function(err,posts){
        res.json(posts);
    })

})

app.get('/detail/:num',function(req,res){
    console.log(req.params.num);
    Board.find({num:req.params.num},function(err,post){
        if(err) return console.error(err);
        res.json(post)
    })

app.post('/delete/',function(req,res){
    console.log(req.body.num);
    
    Board.deleteOne({num:req.body.num},function(err){
        if(err) return console.error(err);

    });
    return;
})

    
})

app.post('/write/',function(req,res){
    console.log(req.body)
    var board = new Board({
        num:req.body.num,
        title:req.body.title,
        content:req.body.content,
        name:req.body.name,
        pw:req.body.pw,
    });
    board.save(function(err,boa){
        if(err) return;
        console.log(boa.title + "save collection");
    })
})