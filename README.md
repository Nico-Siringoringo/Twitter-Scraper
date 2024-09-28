
# Twitter Scraper

## Description
The **Twitter Scraper** is a Python application that allows users to scrape data from Twitter efficiently. This project utilizes the **Twikit** library to build an interactive interface for specifying search parameters and viewing results seamlessly. 

> **Acknowledgments** :
I extend my heartfelt gratitude to the creators and maintainers of **Twikit** for making this project possible.
You can find the Twikit library and its source code on GitHub: [Twikit](https://github.com/d60/twikit).


## Features
- Scrape tweets based on keywords or hashtags.
- Export scraped data to CSV.

## Installation
Install all the requirements

    pip install -r requirements.txt

### Prerequisites
- Python 3.10 or higher
- Internet connection

## How to Use
 1.  Edit the `config.ini` file
 
|Variables| Content |
|--|--|
| username | Your Twitter Username  |
| email | Your Twitter email |
| password | Your Twitter Password |
| query | What you want to search |
| type_of_tweets | Top, Latest or Media |
| limit | The amount of tweet you want to scrape |

 > **Note**
 > Don't use your main account
 2. Add query and limit of data  to  scrape on `config.ini` file
 3. run `main.py` file
 
 ### Advances Search Query
You can use Twitter's advance search to put limitations to your query, just setup the advance query and copy the resulting query in search form.  
[Twitter advance search](https://twitter.com/search-advanced)

<img src="https://github.com/user-attachments/assets/3d98a6ba-a24c-4cc7-adc8-a7fd505f15b7" width="500" height="500">

## Conclusion
Thank you for checking out this project! Feel free to contribute, enhance, or customize this project based on your requirements. Your feedback and improvements are always welcome!
