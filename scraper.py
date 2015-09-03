# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
import time
# # Read in a page
#html = scraperwiki.scrape("http://www.cetlebanon.com/projects/")

# # Find something on the page using css selectors
#root = lxml.html.fromstring(html)
#root.cssselect("table")
from splinter import Browser

with Browser("phantomjs") as browser:
    # Optional, but make sure large enough that responsive pages don't
    # hide elements on you...
    browser.driver.set_window_size(1280, 1024)

    # Open the page you want...
    browser.visit("http://www.cetlebanon.com/projects/")
    table =  browser.find_by_css("table div table")
    # submit the search form...
    for tr in table.find_by_tag("tr"):
        #companyName = tr.find_by_tag("td")[0]
        #print companyName.value.encode('utf-8')
        tr.click()
        project = browser.find_by_css("#project_box table")
        rows = project.find_by_tag("tr")
        name = rows[0].find_by_tag("td")
       # details = project.find_by_tag("tr td")[1]
        print name.value
        overlay = browser.find_by_css("#menu")
        overlay.click()
        time.sleep(0.5)
        #print details.get_text()

# # Write out to the sqlite database using scraperwiki library

#scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
