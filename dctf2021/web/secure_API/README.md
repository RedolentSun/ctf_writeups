# Secure API

when going to the challenge webpage it will give a response letting you know that you are not authorized and should login with guest credentials
https://www.openwall.com/john/)

<img width="642" alt="secure_api_1" src="https://user-images.githubusercontent.com/16979726/118485410-677e5d00-b6e6-11eb-8164-5cd9b0c2e98b.png">

1-) first we can assume that there is a login endpoint and that the login credentials for a guest are username = guest and password = guest. We can then use [Postman](https://www.postman.com/downloads/) to test if this works.

<img width="846" alt="secure_api_2" src="https://user-images.githubusercontent.com/16979726/118486351-7f0a1580-b6e7-11eb-9d42-0920ca140a38.png">

2-) after submitting our post request to the login endpoint, we see that we are returned a bearer token to authenticate our requests.

<img width="830" alt="secure_api_3" src="https://user-images.githubusercontent.com/16979726/118486422-9812c680-b6e7-11eb-9412-b1508493abd8.png">

3-) we can see that this is a json web token, therefore we can use something like [jwt.io](jwt.io) to see the contents of our token as well as to build our future token to get admin rights.

<img width="1196" alt="secure_api_4" src="https://user-images.githubusercontent.com/16979726/118487180-7403b500-b6e8-11eb-8fc2-2b760be6c0e5.png">

4-) from the token we can see that the algorithm used is HS512 / HMAC-SHA512. We can then use [john the ripper](https://www.openwall.com/john/) to brute force the key. We just paste token into a file (i named mine secure_api.hash) and let john the ripper run using the following command: `john secure_api.hash --format=HMAC-SHA512` and it should crack it almost instantly.(tested on 2017 macbook pro)

<img width="567" alt="secure_api_5" src="https://user-images.githubusercontent.com/16979726/118491920-77e60600-b6ed-11eb-8d11-a7e4ba6f930d.png">

5-) using that key we can now make the changes to our token and using [jwt.io](jwt.io) we can just paste the key in the secret key section and change user to admin. (if token is expired edit the time as well)

<img width="1183" alt="secure_api_6" src="https://user-images.githubusercontent.com/16979726/118492558-212cfc00-b6ee-11eb-8c88-d32b69b8554a.png">

6-) using [Postman](https://www.postman.com/downloads/) we can now put our edited token in as bearer token and make a get request to the "/" endpoint and we get the flag.

<img width="855" alt="secure_api_7" src="https://user-images.githubusercontent.com/16979726/118493296-f2fbec00-b6ee-11eb-945d-def04c084bd2.png">

# Video:

https://user-images.githubusercontent.com/16979726/118495743-7d454f80-b6f1-11eb-953f-29e866f2e7d5.mov



