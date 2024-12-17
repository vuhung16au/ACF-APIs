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
- `Active`: x: Rating expired - not active, a: active
- `Unrated`: Rated or Unrated (not rated yet)
- `New`: New (not played enough to have a rating) or Existing (has a rating)
- `ConfidenceLevel`: ??: Very Unreliable, ?: Unreliable, !: Reliable, !!: Very Reliable or Blank
- `NumericalRating`: `Rating` converted to numerical

## Active

Quoted from ACF website.

"A x following a rating indicates that it has expired since the player has not played a rated game in over 10 years. If a player with an expired rating returns and plays in an ACF rated event their new rating will be closely linked and in line with their performance rating and not necessarily their old expired rating. A player with an expired rating is not an unrated player."

## ConfidenceLevel

Quoted from ACF website.


"A rating is followed by either a !!, a !, a blank, a ?, a ?? or a g.

A !! indicates a very reliable rating.
A ! indicates a reliable rating.
A blank indicates the rating is unreliable..
A ? indicates the rating is very unreliable.
A ?? indicates the rating is extremely unreliable.
A g following a number indicates the player needs that many more games before he will get a rating."
