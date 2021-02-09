# Q1 -- Load OSM Data into SQLite

Checklist:
* read up on the [OSM data model](http://wiki.openstreetmap.org/wiki/Elements) 
* install [Osmosis](http://wiki.openstreetmap.org/wiki/Osmosis)
* download a recent map of Alberta from the [Canadian section of the Geofabrik.de download site](https://download.geofabrik.de/north-america/canada.html)
* get the MBR of Edmonton from [the official boundaries of the City of Edmonton](https://data.edmonton.ca/Administrative/City-of-Edmonton-Corporate-Boundary/m45c-6may)
* use osmosis to extract all nodes and paths (with their tags) of Edmonton into an XML file
* process that file to extract the tuples into the SQLite database
* make sure the database has all constraints defined
* make sure your `.gitignore` file prevents you from uploading binary files or large XML files to GitHub (and make sure no such files exist in your repository as well)



## SQL DDL 

Write the DDL for your database here, including all constraints. 

```SQL
CREATE TABLE ... 
```


# TODO: Videos

* Link to Student 1's video: 
* Link to Student 2's video: 