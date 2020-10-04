import express from 'express';
import auth from '../../middleware/auth';
import Post from '../../models/post';

const router = express.Router()

//api/post
router.get('/', async(req,res)=>{
    console.log("asdfasdf")
    const postFindResult = await Post.find();
    console.log(postFindResult,"All Post get");
    res.json(postFindResult);
})

router.post('/',auth,async(req,res,next) =>{
    try{
        console.log(req,"req");
        const{title,contents,fileUrl,creator} = req.body
        const newPost = await Post.create({
            title,contents,fileUrl,creator,
        });
        res.json(newPost)
    }catch(e){
        console.log(e)
    }
});

module.exports = router;