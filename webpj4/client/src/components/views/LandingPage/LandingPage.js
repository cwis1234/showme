import React, { useEffect, useState } from 'react'
import { FaCode } from "react-icons/fa";
import axios from "axios";
import { Col, Card, Row, Carousel } from 'antd';
import { Icon } from '@ant-design/compatible';
import ImageSlider from '../../utils/ImageSlider';
import CheckBox from './Section/CheckBox';
import {continents,price} from './Section/Datas';
import Radiobox from './Section/RadioBox';
import SearchFeature from './Section/SearchFeature';
const { Meta } = Card;

function LandingPage() {

    const [Products, setProducts] = useState([]);
    const [Skip, setSkip] = useState(0)
    const [Limit, setLimit] = useState(6)
    const [PostSize, setPostSize] = useState(0)
    const [Filters,setFilters] = useState({
        continents:[],
        price:[]
    })
    const [SearchTerm,setSearchTerm] = useState("");

    useEffect(() => {
        let body = {
            skip: Skip,
            limit: Limit,
        }

        getProduct(body)


    }, [])

    const getProduct = (body) => {
        axios.post('http://localhost:5000/api/product/products', body)
            .then(response => {
                if (response.data.success) {
                    if (body.loadMore) {
                        setProducts([...Products, ...response.data.productInfo])
                    } else {
                        setProducts(response.data.productInfo)
                    }
                    setPostSize(response.data.postSize)
                } else {
                    alert("상품 정보 가져오기 실패");
                }
            })
    }

    const loadMoreHandler = () => {
        let skip = Skip + Limit

        let body = {
            skip: skip,
            limit: Limit,
            loadMore: true,
        }

        getProduct(body)
        setSkip(skip)
    }

    const renderCards = Products.map((product, index) => {
        return (
            <Col lg={6} md={8} xs={24} key={index}>
                <Card
                    cover={<ImageSlider images={product.images} />}
                >
                    <Meta
                        title={product.title}
                        description={`$${product.price}`}
                    />
                </Card>
            </Col>
        )
    })

    const showFilteredResults = (filters) => {
        let body = {
            skip:0,
            limit:Limit,
            filters:filters
        }
        getProduct(body)
        setSkip(0)
    }

    const handlePrice = (value) => {
        const data = price;
        let array = [];


        for(let key in data){
            if(data[key]._id === parseInt(value,10)){
                array = data[key].array;
            }
        }
        return array;
    }

    const handleFilters = (filters,category) => {
        const newFilters = {...Filters}

        newFilters[category] = filters

        if(category === "price"){
            let priceValue = handlePrice(filters)
            newFilters["price"] = priceValue
        }
        showFilteredResults(newFilters)
        setFilters(newFilters)
    }

    const updateSearchTerm = (newSearchTerm) => {

        let body = {
            skip:0,
            limit:Limit,
            filters:Filters,
            searchTerm:newSearchTerm
        }
        setSearchTerm(newSearchTerm)
        setSkip(0)
        getProduct(body)
    }

    return (
        <div style={{ width: '75%', margin: '3rm auto' }}>
            <div style={{ textAlign: 'center' }}>
                <h2>Let's Travel Anywhere<Icon type="rocket" /></h2>
            </div>


            <Row gutter={[16,16]}>
                <Col lg={12} xs={24}>
                    <CheckBox list={continents} handleFilters = {filters => handleFilters(filters,"continents")}/>
                </Col>
                <Col lg={12} xs={24}>
                    <Radiobox list={price} handleFilters = {filters => handleFilters(filters,"price")}/>
                </Col>
            </Row>


            <div style={{display:'flex', justifyContent:'flex-end',margin:'1rem auto'}}>
                <SearchFeature
                    refreshFunction={updateSearchTerm}
                />
            </div>


          


            <Row gutter={[16, 16]}>
                {renderCards}
            </Row>

            <br/>

            {PostSize >= Limit &&
                <div style={{ display: 'flex', justifyContent: 'center' }}>
                    <button onClick={loadMoreHandler}>더보기</button>
                </div>
            }


        </div>
    )
}

export default LandingPage
