import React from 'react'
import {Row,Col} from 'reactstrap';

const Header = () => {
    return (
        <div id="page-haeder" className="mb-3">
            <Row>
                <Col md="6" sm="auto" className="text-center m-auto">
                    <h1>Our Blog</h1>
                    <p>my blog</p>
                </Col>
            </Row>
        </div>
    )
}
export default Header;