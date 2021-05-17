# Secure Website

for this challenge we are presented with a login page as well as the source code for the login page and our goal is to find the vulnerability with the code.

<img width="1387" alt="secure_website_1" src="https://user-images.githubusercontent.com/16979726/118498220-cb5b5280-b6f3-11eb-818a-5fed7732d296.png">
<img width="790" alt="secure_website_2" src="https://user-images.githubusercontent.com/16979726/118498224-cc8c7f80-b6f3-11eb-97d0-a0e32f2e9783.png">

1-) first we can try take a look at the username, we can either try to guess the common suspects such as guest or admin (admin happens to work). alternatively we can take the hash from the source code and use a tool such as [md5hashing.net](https://md5hashing.net/hash/tiger128%2C4/51c3f5f5d8a8830bc5d8b7ebcb5717df) and it corfirms that the username is indeed admin.

<img width="1137" alt="secure_website_3" src="https://user-images.githubusercontent.com/16979726/118498813-66542c80-b6f4-11eb-8f7a-a0f7085a9e97.png">

2-) for password on the otherhand you cant use [md5hashing.net](https://md5hashing.net/hash/tiger128%2C4/51c3f5f5d8a8830bc5d8b7ebcb5717df) since it yields no results. However, doing some research we can see that for the password the hash starts with "0e" followed by all digits. The "==" comparison treats the whole hash as a float meaning that it is treated as a 0 so we dont necessarily need to find the correct password, just something that will hash to 0 or in the form of "0e" followed by numbers. Using [whitehatsec.com](https://www.whitehatsec.com/blog/magic-hashes/) we do find a list of such strings/hashes (magic hashes).

<img width="1003" alt="secure_website_4" src="https://user-images.githubusercontent.com/16979726/118500577-e8912080-b6f5-11eb-8441-4912d871d904.png">

3-) we can just take the string we found and use it as the password and it should let us login.

<img width="309" alt="secure_website_5" src="https://user-images.githubusercontent.com/16979726/118500937-39087e00-b6f6-11eb-89b3-b4de5ec2c8ca.png">

# Video:


https://user-images.githubusercontent.com/16979726/118501514-cd72e080-b6f6-11eb-9c40-8df1ded6c0b8.mov

