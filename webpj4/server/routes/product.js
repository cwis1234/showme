const express = require('express');
const router = express.Router();
const { User } = require("../models/User");
const multer = require('multer');
const { Product } = require('../models/Product');

const { auth } = require("../middleware/auth");

//=================================
//             Product
//=================================


var storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, 'uploads/');
    },
    filename: function (req, file, cb) {
        cb(null, `${Date.now()}_${file.originalname}`)
    }
})

var upload = multer({ storage: storage }).single("file");


router.post('/image', (req, res) => {
    upload(req, res, err => {
        if (err) {
            return req.json({ success: false, err })
        }
        return res.json({ success: true, filePath: res.req.file.path, fileName: res.req.file.fileName })
    })
})


router.post('/', (req, res) => {
    //db에 저장
    const product = new Product(req.body);
    product.save((err) => {
        if (err) return res.status(400).json({ success: false, err })
        return res.status(200).json({ success: true })
    })
})

router.post('/products', (req, res) => {

    //products collection에 들어있는 모든 상품정보 가져오기

    let limit = req.body.limit ? parseInt(req.body.limit) : 20;
    let skip = req.body.skip ? parseInt(req.body.skip) : 0;

    let findArgs = {};
    let term = req.body.searchTerm;


    for (let key in req.body.filters) {
        if (req.body.filters[key].length > 0) {

            if (key === "price") {
                findArgs[key] = {
                    $gte: req.body.filters[key][0],
                    $lte: req.body.filters[key][1],
                }
            }
            else {
                findArgs[key] = req.body.filters[key];
            }

        }
    }


    if (term) {
        console.log(term);
        Product.find(findArgs)
            .find( { $text:{ $search:term } })
            .populate("writer")
            .skip(skip)
            .limit(limit)
            .exec((err, productInfo) => {
                if (err) {
                     res.status(400).json({ success: false, err }) ;
                     console.log(err)
                     return
                }
                return res.status(200).json({
                    success: true, productInfo,
                    postSize: productInfo.length
                });
            })
    } else {
        Product.find(findArgs)
            .populate("writer")
            .skip(skip)
            .limit(limit)
            .exec((err, productInfo) => {
                if (err) return res.status(400).json({ success: false, err });
                return res.status(200).json({
                    success: true, productInfo,
                    postSize: productInfo.length
                });
            })
    }



})


router.get('/product_by_id', (req, res) => {
    //상품 가져오기

    let type = req.query.type;
    let productId = req.query.id;

    Product.find({_id:productId})
        .populate('writer')
        .exec((err,product)=>{
            if(err) return res.status(400).send(err)
            return res.status(200).send({success:true,product})
        })

})



module.exports = router;
