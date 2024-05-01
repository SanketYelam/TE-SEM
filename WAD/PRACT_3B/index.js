const dbConnect=('/mongodb')
const express=require('express');
const app=express();
app.use(express.json())

app.get('/',async(req,res)=>{
    let result=await dbConnect();
    result=await result.find().toArray();
    res.send(result);
})


app.post('/',async(req,res)=>{
    let result=await dbConnect();
    result=await result.insertOne(req.body);
    res.send("Data Inserted Successfully")
})

app.post('/',async(req,res)=>{
    let result=await dbConnect();
    result=await result.updateOne(req.body);
    res.send("Data Updted Successfully")
})

app.listen(3000);