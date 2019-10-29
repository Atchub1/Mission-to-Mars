  
# Create a function to scrape multiple websites and return one result, a python dictionary of scraping reulsts 
# function was created in jupyter notebook and exported as a python file


def scrape():    
    
    #!/usr/bin/env python
    # coding: utf-8

    # ## NASA Mars News
    # 
    # Scrape the NASA Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
    # https://mars.nasa.gov/news/
    # 

    # In[5]:


    from splinter import Browser
    from bs4 import BeautifulSoup
    import requests


    # In[6]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[7]:


    #I first attempted this without chromedriver, however, the correct articles could not be retrieved without the driver 

    # URL of page to be scraped
    nasa_url = 'https://mars.nasa.gov/news/'

    # Retrieve the page
    browser.visit(nasa_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())


    # In[8]:


    # query beautiful soup result for the first article title
    title_results = soup.find('div', class_='content_title').a.text.strip()
    # title_results


    # In[10]:


    # query beautiful soup result for the first article description 
    desc_results = soup.find('div', class_='article_teaser_body').text.strip()
    # print(desc_results)


    # ## JPL Mars Space Images - Featured Image
    # 
    # Visit the url for JPL Featured Space Image here. https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
    #     
    # Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.

    # In[12]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[13]:


    # URL of page to be scraped
    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    # Retrieve the page
    browser.visit(image_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # print(soup.prettify())


    # In[14]:


    # get the url of the image
    base_image_url ='https://www.jpl.nasa.gov'

    # grab the partial featured image link
    partial_featured_image_url = soup.find('article', class_='carousel_item').a['data-fancybox-href']
    # print(partial_featured_image_url)

    featured_image_url = base_image_url + partial_featured_image_url
    print(featured_image_url)


    # ## Mars Weather
    # 
    # Visit the Mars Weather twitter account here, https://twitter.com/marswxreport?lang=en
    # and scrape the latest Mars weather tweet from the page. Save the tweet text for the weather report as a variable called mars_weather.

    # In[ ]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[ ]:


    # URL of page to be scraped
    weather_url = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve the page
    browser.visit(weather_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())


    # In[ ]:


    mars_weather = soup.find('p', class_ ='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.strip()
    print(mars_weather)


    # ## Mars Facts
    # 
    # Visit the Mars Facts webpage here https://space-facts.com/mars/
    # and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # Use Pandas to convert the data to a HTML table string.

    # In[ ]:


    import pandas as pd

    # import the list of tables from the webpage
    mars_table_url = 'https://space-facts.com/mars/'
    mars_list = pd.read_html(mars_table_url)
    # mars_list


    # In[ ]:


    # extract the mars dataframe from the list
    mars_df = mars_list[1]
    mars_df.columns = ['Type', 'Measurment']
    mars_df.set_index('Type', inplace=True)
    # mars_df.head()


    # In[18]:


    #export mar dataframe to html
    mars_html_table = mars_df.to_html()
    # mars_html_table


    # ## Mars Hemispheres
    # 
    # 
    # Visit the USGS Astrogeology site here https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
    # to obtain high resolution images for each of Mar's hemispheres

    # In[ ]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # In[ ]:


    # URL of page to be scraped
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # Retrieve the page
    browser.visit(hemisphere_url)

    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())


    # In[ ]:


    thumb_results = soup.find_all('img', class_ = 'thumb')
    # print(thumb_results)

    base_url = 'https://astrogeology.usgs.gov/'
    thumb_img_links = []

    for thumb_result in thumb_results:
        partial_thumb_image_link = thumb_result['src']
        thumb_img_link = base_url + partial_thumb_image_link
        thumb_img_links.append(thumb_img_link)
    #     print('-----------------------------------')
    #     print(thumb_img_link)


    # In[ ]:


    # thumb_title_results = soup.find('div', class_ ='item').div.a.h3.text

    thumb_title_results = soup.find_all('div', class_ ='item')
    # print(thumb_title_results)

    thumb_titles = []

    for result in thumb_title_results:
        thumb_title = result.div.a.h3.text.rsplit(' ', 1)[0]
        thumb_titles.append(thumb_title)
    #     print('--------------------')
    #     print(thumb_title)
    # print(thumb_titles)


    # In[ ]:


    #Make dictionary with title and image link as key and values respectively 

    mars_hem_dict = [{'title': thumb_titles[0], 'img_url':thumb_img_links[0]},
                    {'title': thumb_titles[1], 'img_url':thumb_img_links[1]},
                    {'title': thumb_titles[2], 'img_url':thumb_img_links[2]},
                    {'title': thumb_titles[3], 'img_url':thumb_img_links[3]}]

    # mars_hem_dict

    mars_web_dict = {
        'latest_news_title':title_results,
        'latest_news_description':desc_results,
        'featured_image_url':featured_image_url,
        'mars_weather':mars_weather,
        'mars_html_table':mars_html_table,
        'mars_hem_dict':mars_hem_dict

    }


    return mars_web_dict 

