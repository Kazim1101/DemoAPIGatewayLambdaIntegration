# DemoAPIGatewayLambdaIntegration
Lambda will implement restApi for Get method to return the objects and content of S3 bucket

Get Api  : /list
Response : 
{
  "response_id": "da0b86cd-e25f-41fd-ac2a-664d6726384f",
  "bucket_response": [
    {
      "object-name": "TestFile1.txt",
      "content": "b'Hellow from the other side :)'"
    },
    {
      "object-name": "contacts_.csv",
      "content": "b'first_name,last_name,company_name,address,city,county,state,zip,phone1,phone,email\\r\\nJames,Butt,\"Benton, John B Jr\",6649 N Blue Gum St,New Orleans,Orleans,LA,70116,504-621-8927,504-845-1427,jbutt@gmail.com\\r\\nJosephine,Darakjy,\"Chanay, Jeffrey A Esq\",4 B Blue Ridge Blvd,Brighton,Livingston,MI,48116,810-292-9388,810-374-9840,josephine_darakjy@darakjy.org\\r\\nArt,Venere,\"Chemel, James L Cpa\",8 W Cerritos Ave #54,Bridgeport,Gloucester,NJ,8014,856-636-8749,856-264-4130,art@venere.org\\r\\nLenna,Paprocki,Feltz Printing Service,639 Main St,Anchorage,Anchorage,AK,99501,907-385-4412,907-921-2010,lpaprocki@hotmail.com\\r\\nDonette,Foller,Printing Dimensions,34 Center St,Hamilton,Butler,OH,45011,513-570-1893,513-549-4561,donette.foller@cox.net\\r\\nSimona,Morasca,\"Chapman, Ross E Esq\",3 Mcauley Dr,Ashland,Ashland,OH,44805,419-503-2484,419-800-6759,simona@morasca.com\\r\\nMitsue,Tollner,Morlong Associates,7 Eads St,Chicago,Cook,IL,60632,773-573-6914,773-924-8565,mitsue_tollner@yahoo.com\\r\\nLeota,Dilliard,Commercial Press,7 W Jackson Blvd,San Jose,Santa Clara,CA,95111,408-752-3500,408-813-1105,leota@hotmail.com\\r\\nSage,Wieser,Truhlar And Truhlar Attys,5 Boston Ave #88,Sioux Falls,Minnehaha,SD,57105,605-414-2147,605-794-4895,sage_wieser@cox.net\\r\\n'"
    }
  ]
}

Note: Due to not having much experience is LinkedServiceRole creation I did with the normal roles with other AWS account bit the cloudfoemation with be compatible with the other account as well

I have also commit the service linked role yml just to discuss in the meeting :)