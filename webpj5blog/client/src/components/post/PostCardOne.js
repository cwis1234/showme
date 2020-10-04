import React, { Fragment } from 'react'
import { CardImg,Card, CardBody, CardTitle,Button,Row, Badge } from 'reactstrap'
import { Link } from 'react-router-dom'

const PostCardOne = ({posts}) => {
    posts = posts[0]
    return(
        <Fragment>
            {
                Array.isArray(posts) ? posts.map((post) =>{
                    return(
                        <div key = {post._id} className="col-md-4">
                            <Link to={`/posts/${post._id}`} className="text-dark text-decoration-none">
                                <Card className="mb-3">
                                    <CardImg top alt="이미지" src={post.fileUrl}/>
                                    <CardBody>
                                        <CardTitle className="text-truncate d-flex justify-content-between">
                                            <span className="text-truncate">{post.title}</span>
                                            <span className="text-truncate">
                                                hit
                                                &nbsp;
                                                <span>{post.views}</span>
                                            </span>
                                        </CardTitle>
                                        <Row>
                                            <Button color="primary" className="p-2 btn-block">
                                                More <Badge color="light">{post.comments.length}</Badge>
                                            </Button>
                                        </Row>
                                    </CardBody>
                                </Card>
                            </Link>
                        </div>
                    )
                })
            :"gg"
            }
        </Fragment>
    )
}

export default PostCardOne;