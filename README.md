# CS411_Project
## Team Members: Shuiling Yu, Yekai Chen, Zheying Lu, Chin-Han Lin

Small database for IMDB movie
---------
### Project Information:
* Backend database: sqlite
* Front-end interface: Django
* Needed Python packages:
	+ [sqlite3](https://docs.python.org/2/library/sqlite3.html): python sqlite connection
	+ [imdbpie](https://pypi.org/project/imdbpie/): IMDB data


### To run the server in localhost:
1. Activate the vitual environment:
`source projectenv/bin/activate`

   Install django if needed:
`pip install django`

2. run server on local host
`python manage.py runserver`

### Next Stage Work (after initial demo)
- [ ] Localhost to domain name (using Apache)?
- [ ] Add more information about other entity: Actors, Directors
- [ ] Add more information about movie: create seperate table for prize (i.e. Movie(Movie_ID, Prize)) if needed. Same for Actors, Directors
- [ ] Prediction and recommendation
- [ ] Better UI