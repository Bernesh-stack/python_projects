import requests
UserName = "xxxxx"
Token = "xxxxx"
graf_Id = "xxx"

Pixels_Api = "https://pixe.la/v1/users"
user_Paramas = {
    "token":Token,
    "username":UserName,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

requested_paramas={
    "id":graf_Id,
    "name":"Streak",
    "unit":"calory",
    "type":"float",
    "color":"ajisai"
}

headers ={
    "X-USER-TOKEN":Token
}

response = requests.post(Pixels_Api,json=user_Paramas)

# Graph m os here
Graph_Api = f"{Pixels_Api}/{UserName}/graphs"
Graph_request = requests.post(url=Graph_Api,json=requested_paramas,headers=headers)

print(Graph_request.text)



Pixel_creation_endpoint = f"{Pixels_Api}/{UserName}/graphs/{graf_Id}"

Pixel_data = {
    "date":"20200724",
    "quantity":"9.74"
}
responsed = requests.post(url=Pixel_creation_endpoint,json=Pixel_data,headers=headers)
print(responsed.text)


