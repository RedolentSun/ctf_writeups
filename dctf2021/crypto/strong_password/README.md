# Strong Password

we are provided with a zip file which is password secured.

1-) we can try to brute force the password using [john the ripper](https://www.openwall.com/john/). first we use zip2john to make a hashfile. `zip2john strong_password.zip > zipped.hash`

<img width="568" alt="strong_1" src="https://user-images.githubusercontent.com/16979726/118506726-9226e080-b6fb-11eb-9d8e-4e839a4bf5bd.png">

2-) now we can use john against the hash file with our rockyou.txt wordlist. `john zipped.hash --wordlist=rockyou.txt`

<img width="570" alt="strong_2" src="https://user-images.githubusercontent.com/16979726/118507155-f8136800-b6fb-11eb-9bc9-2956e1d7f5cc.png">

3-) we see that john found the password so we can use `john zipped --show` to see the password.

<img width="565" alt="strong_3" src="https://user-images.githubusercontent.com/16979726/118507433-390b7c80-b6fc-11eb-8bad-7bd496bc82c8.png">

4-) now we can use that password to open the zip and get our flag

<img width="676" alt="strong_4" src="https://user-images.githubusercontent.com/16979726/118507654-6f48fc00-b6fc-11eb-81c4-57861c1937c1.png">

# Video:


https://user-images.githubusercontent.com/16979726/118509753-55101d80-b6fe-11eb-9658-d421bdf6b612.mov

