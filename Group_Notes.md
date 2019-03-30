## 03.26 (Before demo 1)
### Next Stage Work (after first demo)
- [ ] Add more information about other entity: Actors, Directors
- [ ] Another information for Movies entity:
	* Using IMDB movie ID (e.g 0499549) in Movie data
	  **This time manually-created ID is used (from 1 to 1100)**
	* Link
	* poster (for better visulization)
	* (trailer)
- [ ] Add more information about movie: create seperate table for prize:
	* Prize(movieID, prize)
	* Movie_Genre(movieID, Genre_1, Genre_2, Genre_3) 
	* .... (to be added)
Same for Actors, Directors
- [ ] Prediction and recommendation
- [ ] Better UI
- [ ] More search types with dropdown box
- [ ] Pagination

(If time allows)
- [ ] Localhost to domain name (using Cpanel): Extract credit

### Misc Notes
* Useful Python packages:
	+ [sqlite3](https://docs.python.org/2/library/sqlite3.html): python sqlite connection
	+ [imdbpie](https://pypi.org/project/imdbpie/): IMDB data
* Possible sofrware to open .sqlite: [sqlitebrowser](https://sqlitebrowser.org/blog/version-3-11-1-released/)
* Similar Projects:
	+ [Media-Hub](https://github.com/JeeveshN/Media-Hub)
	+ [NBA DB](https://www.youtube.com/watch?v=KvlmgWRDzqo&t=9s)
	+ [Moviehunter](https://github.com/BruceHenry/movie-website-django)
* Add data into `db.sqlite3`:
    `python3 add_data.py`
* Superuser: group50, yslenjoy@gmail.com, 411group50
