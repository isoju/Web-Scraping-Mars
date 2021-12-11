# Web Scraping Mission to Mars

![mission_to_mars](Images/mission_to_mars.png)

## Scraping

Completed initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.


### NASA Mars News

* Scraped the [Mars News Site](https://redplanetscience.com/) and collect the latest News Title and Paragraph Text. 
* Assigned Title and Paragraph into variables.

```python
news_title = "NASA's Next Mars Mission to Investigate Interior of Red Planet"

news_p = "Preparation of NASA's next spacecraft to Mars, InSight, has ramped up this summer, on course for launch next May from Vandenberg Air Force Base in central California -- the first interplanetary launch in history from America's West Coast."
```

### JPL Mars Space Images - Featured Image

* Used splinter to navigate the [JPL Mars Website](https://spaceimages-mars.com) and find current Featured Mars Image url and assign the url string to a variable called `featured_image_url`.

```python
featured_image_url = 'https://spaceimages-mars.com/image/featured/mars2.jpg'
```

### Mars Facts

* Used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc from [Mars Facts webpage](https://galaxyfacts-mars.com).

* Used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Scraped [Astrogeology site](https://marshemispheres.com/) to obtain high resolution images for each of Mars's hemispheres.

* Used a Python dictionary to store the data using the keys `img_url` and `title`.

* Appended the dictionary with the image url string and the hemisphere title to a list. 

```python
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    {"title": "Cerberus Hemisphere", "img_url": "..."},
    {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    {"title": "Syrtis Major Hemisphere", "img_url": "..."},
]
```

- - -

## MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Converted Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that executes all scraping code and return one Python dictionary containing all of the scraped data.

* Created a route called `/scrape` that imports `scrape_mars.py` script and calls `scrape` function.

  * Stored the return value in Mongo as a Python dictionary.

* Created a root route `/` that query Mongo database and pass the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 
* 
![final_app_part1.png](Images/final_app.png)

- - -

