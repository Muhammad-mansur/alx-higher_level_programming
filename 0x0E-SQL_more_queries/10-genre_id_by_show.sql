-- Import the database dump from hbtn_0d_tvshows to your MySQL server.

SELECT tv_shows.title, genre_id FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;