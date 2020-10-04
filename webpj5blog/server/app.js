import express from 'express';
import mongoose from 'mongoose';
import config from './config';
import hpp from 'hpp';
import helmet from 'helmet';
import cors from 'cors';
import morgan from 'morgan';

import postsRoutes from './route/api/post';
import usersRoutes from './route/api/user';
import authRouter from './route/api/auth';
import auth from './middleware/auth';

const app = express();
const {MONGO_URI} = config;

app.use(hpp())
app.use(helmet())

app.use(cors({origin:true, credentials:true}))
app.use(morgan("dev"))

app.use(express.json());



mongoose.connect(MONGO_URI,{
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useCreateIndex:true,
}).then(()=>console.log("MongoDB Connected"))
    .catch((e)=>console.log(e))


//라우터 
app.get('/');
app.use('/api/post',postsRoutes);
app.use('/api/user',usersRoutes);
app.use('/api/auth',authRouter);

export default app;