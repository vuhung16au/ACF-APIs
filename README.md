# ACF-APIs
APIs to fetch ACF chess players' info

# Clean and Prepare the Data 

- Run `clean-master.py` to create the ACF players info file. The output file is `master-ratings-unsorted.csv`. This file will be used as the players' database for the API server
- 
# How to Run 

- install requirements `pip install -r requirements.txt`
- run the API server `fastapi dev ACF-Classical-API.py`

# Call the APIs 

## Request player info by ID
`http://127.0.0.1:8000/players/1712662/info`

Response:
```
{"player_id":1712662,"Rating":"2016!!","Federation":"NSW","Name":"Nguyen, Vu Ky Anh","Active":"a","Unrated":"Rated","New":"Existing","ConfidenceLevel":"Very Reliable","NumericalRating":2016}
```

## Request player rating by ID
`http://127.0.0.1:8000/players/1712662/ratings`

Response:
```
{"player_id":1712662,"NumericalRating":2016}
```

# Format of the Players' database 

```
ID,Rating,Federation,Name,Active,Unrated,New,ConfidenceLevel,NumericalRating
3070011,1331x,VIC,"A'Burrow, Barry",x,Rated,New,,1331
1063040,Unr,ACT,"A'Hearn, Belinda",a,Unrated,Existing,,0
```

- `ID`: ACF ID 
- `Rating`: Raw ratings provided by ACF
- `Federation`: OS: Oversea. NSW, VIC, QLD: Australia states
- `Name`: Players' full name
- `Active`: x: not active, a: active
- `Unrated`: Rated or Unrated (not rated yet)
- `New`: New (not played enough to have a rating) or Existing (has a rating)
- `ConfidenceLevel`: ??: Very Unreliable, ?: Unreliable, !: Reliable, !!: Very Reliable or Blank
- `NumericalRating`: `Rating` converted to numerical
