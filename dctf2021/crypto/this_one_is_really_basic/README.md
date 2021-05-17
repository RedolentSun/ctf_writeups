# This one is really basic

 we are given a really big file of cipher text.
 
 1-) i copied part of the cipher text and used [dcode.fr](https://www.dcode.fr/cipher-identifier) to identify the cipher and it was determined to most likely be base58 or base64 encoded.
 
 <img width="797" alt="basic_1" src="https://user-images.githubusercontent.com/16979726/118511485-f21f8600-b6ff-11eb-93b5-d95cd07959c0.png">

2-) i made a python script to decode it since it was really big to decode using [dcode.fr](https://www.dcode.fr/cipher-identifier).

3-) on the first decode i got back another base64 text so i looped over it 100 more times printing the index during each iteration of loop

<img width="566" alt="basic_2" src="https://user-images.githubusercontent.com/16979726/118512499-da94cd00-b700-11eb-8210-bfa69708f02b.png">

4-) i noticed that my script crashed when it got to the 41st iteration so i capped it to run 40 times and output the result during the 40th iteration and got the flag.

<img width="337" alt="basic_3" src="https://user-images.githubusercontent.com/16979726/118512818-26477680-b701-11eb-8367-b5af0c721a17.png">

