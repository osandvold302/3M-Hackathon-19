# Post-It Hub  
This is the repo for the 3M 2019 Hackathon project hack "Post-It Portal".  

## Goals  
We would like to build a Post-It dispenser with a wireless charging port, amplifying speaker, 
and Amazon dash button. This dash button will be used as an emergency supply stock purchase button 
and will trigger a web application to display the order. 

## AWS Set-up  
TODO:  

1. Generate certificate in IOT Core  
2. Create Thing in IOT Core [Tutorial](https://docs.aws.amazon.com/iot/latest/developerguide/iot-plant-step2.html)   
3. Generate certificates for Thing  
4. Get custom endpoint from IOT Core/Settings  
5. Create new S3 bucket for static web hosting  
6. Create Lambda that is triggered by API gateway and posts to Cloudwatch Log (?)  
7. Create API Gateway with methods for GET (?) 
8. Update the js for bundle.js to update the page when a request is sent (?) 
