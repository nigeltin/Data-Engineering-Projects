#### Scenario

A startup wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. 
The analytics team is particularly interested in understanding what songs users are listening to. 
Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

#### Objective

To create a database schema and etl pipeline for the analytics team

#### Dataset

- **Song datasets**: all json files are nested in subdirectories under */data/song_data*. A sample of this files is:

```
{"num_songs": 1, 
"artist_id": "ARJIE2Y1187B994AB7", 
"artist_latitude": null, 
"artist_longitude": null, 
"artist_location": "", 
"artist_name": "Line Renaud", 
"song_id": "SOUPIRU12A6D4FA1E1", 
"title": "Der Kleine Dompfaff", 
"duration": 152.92036, "year": 0}
```

- **Log datasets**: all json files are nested in subdirectories under */data/log_data*. 

#### Database schema

Since we know before-hand the sctructure of the jsons we need to analyze, and where and how to extract and transform each field; the data types are structure. Data needed to answer business questions can be modeled using simple ERD models. We need to use JOINS for this scenario.

Hence, a star schema is appropriate for this case.




















