# Text to Timeline

The goal of this project is to make a timeline web page by writing a text file such as diary. 

You can revise the .css file for your own preferences.



The project have the following characters:

* Using text files to generate a timeline web page;

* Supporting different text style;

* Supporting local images and url of web images;

* Showing heart when click on the page;



Result of this project is like this:

<img src="https://i.loli.net/2020/04/18/t6uAryS84F7VwPH.png" width=700  align='center' />

The origin text file is:
```
-2019
test_images/test.png
# Title1

-1.1
## Title2
### Title3

-1.2
text text text text

-1.3 
text text
text text
text text
```

---

## Usage

1. Using `-time` and line break to start a point at time and the content just behind the line;

```
-3.17 
A nice day!
```

2. Adding a relative image path ( my suggestion is move the images to ./image dir) or a web image link in the content；

```
-3.17 
A nice day!
image/WechatIMG99.jpeg
```

3. Using different font styles by different numbers of `#`, which means h1/h2/h3 of font style;

```
-2019
image/0.png
#200天快乐!
   
-2019
image/1.png
###This is the story of Ray and Amanda
###Let's start! 
```

4. Running the python file with the flags we want to use, the default parameters are 'story.txt','index.css',True.

```
python txt_to_timeline.py --path diary.txt --css index.css --add_heart True
```

