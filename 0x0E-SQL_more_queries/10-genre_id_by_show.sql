-- Showing the tv shws and their genre
SELECT tv_shows.title, tv_shows_genres.genre_id tv_shows INNER JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id;
