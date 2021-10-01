# bisCrawler: An Automation Webcrawler for Extracting Central Bankers' Speeches 🛠️🧰

An automation web crawling framework for retrieving for Extracting Central Bankers' Speeches on the Website of **Bank for International Settlements (https://www.bis.org)** based on Selenium and Chrome browser.

<p align="center">
  <img width="1000" height="550" src="https://raw.githack.com/davidycliao/bisCrawler/main/images/speech.png" >
</p>



## Environment Setup

1. Need to install [Anaconda Navigator](https://www.anaconda.com/products/individual-b) and [Python>=3.9](https://www.python.org/downloads/release/python-3810/) beforehand. And then, open the terminal and download `bisCrawler` repository by using `git clone`. About how to use git and Github, please have a look at this [Tutorial for Beginners](https://www.youtube.com/watch?v=RvnM6EEwp1I). 

```
git clone  git@github.com:davidycliao/bisCrawler.git
```

2. Copy the commands below and paste them into the terminal:

```
# Change the directory by typing `cd` command once `bisCrawler` repository is downloaded.
cd bisCrawler

# Create the enviroment by using conda and name the enviroment `bisCrawler`.
conda create -n bisCrawler python=3.9
```

## Instruction

1. Activate the pre-named enviroment. Alternatively, the environment for bisCrawler can be opened via [Anaconda Navigator](https://www.anaconda.com/products/individual-b)

```
conda activate bisCrawler 
```

2. Install the dependencies from `requirements.txt` using `pip` methond.

```
pip install -r requirements.txt   
```

3. Call `bisCrawler` Moduel

- In the terminal:
```
# Note: you need to run it in the terminal where you activated the enviroment.
python bisCrawler.py
```

- In Jupyter Notebook:

```
from bisCrawler import scraper 
```

```
scraper()
```

4. When Running bisCrawler

When **bisCrawler** is running, you will be asked which page you would like to scrape (please, type any single digit from 1 to last page). Then **bisCrawler** will automatically generate pandas dataframe to restore the banker speeches and the urls to the textual document.  

<p align="center">
  <img width="900" height="280" src="https://raw.githack.com/davidycliao/bisCrawler/main/images/module.png" >
</p>






## What **bisCrawler** Scrapes
This designed crawler automatically webscrapes  the central bankers' speeches from the offical website, including a bunch of information with regards to each name of central banker, date and title and corresponding url to the textual document. 

<p align="center">
  <img width="900" height="280" src="https://raw.githack.com/davidycliao/bisCrawler/main/images/bank2.png" >
</p>



## Websraped Data

The scraped dataframe will be stored as _central_bank_speeches.csv_ in the bisCrawler folder.  


<p align="center">
  <img width="700" height="380" src="https://raw.githack.com/davidycliao/bisCrawler/main/images/speech_data_frame.png" >
</p>



## Cite

Please cite this page if you use this toolkit for your research.

For example, with BibTeX:
```
@misc{bisCrawler,
    howpublished = {\url{https://github.com/davidycliao/bisCrawler}},
    title = {bisCrawler: An Automation Webcrawler for Extracting Central Bankers' Speeches},
    author = {David Yen-Chieh Liao and Li Tang},
    publisher = {GitHub},
    year = {2021}
}
```


