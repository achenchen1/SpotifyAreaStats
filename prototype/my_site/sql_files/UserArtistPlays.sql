CREATE TABLE UserArtistPlays (
    user_id INTEGER NOT NULL,
    artist_id INTEGER NOT NULL,
    plays INTEGER NOT NULL,
    PRIMARY KEY (user_id, artist_id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (artist_id) REFERENCES Artists(id)
);
