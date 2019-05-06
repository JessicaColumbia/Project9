#Project 9 Group

- We have created a file including all the five scoring functions to evaluate all 1000 song lyrics by comparing the words with pre-created word lists. 

For preparation, we created a gre words txt for complexity evaluation, a bad words txt for kid_safe evaluation, and several word lists for love and mood evaluation. 

TO evaluate kid_safe, love, mood and complexity, we split the lyrics into words, compared the words with the word lists we prepared, and scored each index according to the proportion.
To evaluate the length of the lyrics file, we used 300 words as an upper benchmark and then normalized the output between 0 and 1.

To detect the language of each song, we imported a package called "cld2", which could successfully detect English, French, Romanian and other languages when we ran our program. 

!!!!!!:Please note, you may need to install the package by entering "$ pip install cld2-cffi" in terminal before test our program. Thanks!!!!!!!!!!

Because this language detector package can detect str but not list, we decided to detect every first line of each song in the corresponding lyrics txt, as well as to save the execution time.

Finally, we created a test file to make sure all the functions run with no error and the results are reasonable. We did some adjustments of scoring functions based on the test results to make the scoring more reasonalbe and as precise as possible.

run our program by type in the following command in VM: "python main.py Path/to/LyricsFolder"

- Project 9, Section IEOR 4501 E sec 001

- Xuefei Cheng xc2449, Jiaxi Wen jw3693