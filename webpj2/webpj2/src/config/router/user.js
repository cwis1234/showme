var express = require('express');
var router = express.Router();

router.get('/',function(req,res){
    res.send('ss World');
});
router.get('/:id',function(req,res){
    res.send('Receive a GET request, param:' + req.params.id);
});
router.put('/',function(req,res){
    res.status(400).json({message:'Bad Request'});
});
router.post('/',function(req,res){
    console.log(JSON.stringify(req.body,null,2));
    res.json({
        succes:true,
        user: req.body.username
    });
});

router.delete('/',function(req,res){
    res.send('Receive DELETE request');
});

module.exports = router;