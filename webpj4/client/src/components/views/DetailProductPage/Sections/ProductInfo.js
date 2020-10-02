import React from 'react';
import {Button,Descriptions} from 'antd';

function ProductInfo(props) {
    return (
        <div>
            <Descriptions title="ProductInfo Info">
                <Descriptions.Item label="Price">{props.detail.price}</Descriptions.Item>
                <Descriptions.Item label="Sold">{props.detail.sold}</Descriptions.Item>
                <Descriptions.Item label="View">{props.detail.views}</Descriptions.Item>
                <Descriptions.Item label="Description">{props.detail.description}</Descriptions.Item>
            </Descriptions>
        </div>
    )
}

export default ProductInfo;