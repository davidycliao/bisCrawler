# bisCrawler: An Automation Webcrawler for Extracting Central Bankers' Speeches 🛠️🧰

An automation web crawling framework for retrieving for Extracting Central Bankers' Speeches from Bank for International Settlements (https://www.bis.org)

<p align="center">
  <img width="700" height="500" src="https://raw.githack.com/davidycliao/bisCrawler/main/images/bank2.png.png" >
</p>



## Instruction

- Need to install [Anaconda Navigator](https://www.anaconda.com/products/individual-b) and [Python>=3.9](https://www.python.org/downloads/release/python-3810/) beforehand. And then, open the terminal and download `bisCrawler` repository by using `git clone`.

- About how to use git and Github, please have a look at this [Tutorial for Beginners](https://www.youtube.com/watch?v=RvnM6EEwp1I). 

```
git clone  git@github.com:davidycliao/bisCrawler.git
```

- Copy the commands  below and paste them into the terminal:
```
# Change the directory by typing `cd` command once `bisCrawler` repository is downloaded.
cd bisCrawler

# Create the enviroment by using conda and name the enviroment `bisCrawler`.
conda create -n bisCrawler python=3.9

# Activate the pre-named enviroment. 
conda activate bisCrawler 

# Install the dependencies from `requirements.txt` using `pip` methond.
pip install -r requirements.txt   
```

- Run `bisCrawler` in your Python:
```
# Note: you need to run it in the terminal where you activated the enviroment.
python bisCrawler.py
```


- When **bisCrawler** is running, you will be asked which page you would like to scrape (please, type any single digit from 1 to last page). Then **bisCrawler** will automatically create a folder to restore the retrieval of parliamentary questions by individual member.  

<p align="center">
  <img width="700" height="500" src="https://raw.githack.com/davidycliao/bisCrawler/main/images/speech.png" >
</p>




## What **bisCrawler** Scrapes
This designed crawler automatically webscrapes  the central bankers' speeches from the ofical website, including a bunch of information with regards to each central banker, date and title and corresponding url to the textual document. 
<p align="center">
  <img width="700" height="500" src="https://raw.githack.com/davidycliao/bisCrawler/main/images/speech_data_frame.png" >
</p>



## Cite

For citing this work, you can refer to the present GitHub project. For example, with BibTeX:
```
@misc{bisCrawler,
    howpublished = {\url{https://github.com/davidycliao/bisCrawler}},
    title = {An Automation Webcrawling Toolkit for Extracting Central Bankers' Speeches},
    author = {David Yen-Chieh Liao and Li Tang},
    publisher = {GitHub},
    year = {2021}
}
```

