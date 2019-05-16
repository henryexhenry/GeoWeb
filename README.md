# Web db project

## Web structure
- continent page
- country page

## Data
- The resource is integrated from the CIA World Factbook, the International Atlas, and the TERRA database among other sources.

## Objective
- showing countries by its continent respectively
- showing location of a country on map by Google map API
- showing descriptions of countries and natural environment of countries


## XPath used
- to find attribute given its parent node's attribute
    - `'continent[@id="'+ctnid+'"]//img/@src'`
- to find element given its child's attribute
    - `'country[./encompassed/@continent="'+ctnid+'"]'`
- to find attribut given another attribute in the same node
    - `'country[@name="'+ctryName+'"]/@id'`
- to find node given its attribute
    - `'country[@id="'+ctryid+'"]'`
- to find node containing a specific attribute given its ancestor node's attribute
    - `'country[contains(@id, "'+ctryid+'")]//city[contains(@latitude, ".")]'`

## bugs
- not well-formed : Ampersand (&) in url
    - `&` should be replaced by `&amp;`
- SyntaxError: invalid predicate
    - `ElementTree`'s XPath support is limited. Use other library like `lxml`
- missing data
    - use `if` statement to filter the missing data


## Report
- detailed design of the web application:
- system structure
    - data layer
        - db -> crawling + xml
    - application layer
        - web server -> flask 
        - service
    - representation layer
- components of the system
    - functionality aspect
        - GoogleMap
            - Using Google map API to help visaulizing the actual area in the map.
        - Eco-system
            - The page can enumerate the eco-environment inside a country such as mountains, rivers, lakes as well as islands.
        - Cache
            - The website can remember the visit record of users, if user close the browser and open again, the record will still be there.
            - I use the flask_session feature to build this function. it help me record the visit history for each session.
    - presentation aspect
        - side bar
            - clearly display every continent, convenient to navigate
        - drop down list element
            - keep the page clean instead of showing too many elements on the page.
- class diagrams
    - continent
    - country
    - mountain
- database
    - xml format, adv, disadv
    - where data come from
- programming languages and tools used
    - python
    - framework flask
    - library
        - requests
        - lxml
            - xpath
        - flask_session
            - to cache history
        - bootstrap
- testing strategies and results
    - website layout
        - is it comfortable to use
        - well constructed
        - responsive
    - navigation
        - make sure the hyperlinks bring user to the correct pages
    - data
        - correct and relevant
- user manual
- package of source code and installation guide for deployment