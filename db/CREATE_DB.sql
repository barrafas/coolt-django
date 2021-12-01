PRAGMA foreign_keys = ON;
-- tables
-- Table: creators
CREATE TABLE creators (
    id INTEGER PRIMARY KEY,
    creator varchar(255) NOT NULL
);

-- Table: user

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username varchar(50) NOT NULL,
    name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    created TEXT NOT NULL DEFAULT (datetime('now'))
);


-- Table: works
CREATE TABLE works (
    id INTEGER PRIMARY KEY,
    name varchar(255) NOT NULL,
    type varchar(255) NOT NULL,
    publisher varchar(255) NULL,
    synopsis text NULL,
    released date NOT NULL,
    img_link text NULL
);

-- Table: genres
CREATE TABLE genres (
    id INTEGER PRIMARY KEY,
    genre varchar(255) NOT NULL
);

-- Table: statuses
CREATE TABLE statuses (
    id INTEGER PRIMARY KEY,
    status varchar(255) NOT NULL
);

--- SEM FK ---

-- Table: reviews
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    work_id INTEGER NOT NULL,
    review_id INTEGER NULL,
    score int NOT NULL,
    review text NULL,
    created TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(work_id) REFERENCES works(id),
    FOREIGN KEY(review_id) REFERENCES reviews(id)
);

-- Table: review_likes
CREATE TABLE review_likes (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    review_id INTEGER NOT NULL,
    type INT NOT NULL,
    created TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY(review_id) REFERENCES reviews(id)
);

-- Table: shelf
CREATE TABLE shelf (
    id INTEGER PRIMARY KEY,
    work_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY(work_id) REFERENCES works(id),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(status_id) REFERENCES statuses(id)
);

-- Table: user_followers
CREATE TABLE user_followers (
    id INTEGER PRIMARY KEY,
    source_id INTEGER NOT NULL,
    target_id INTEGER NOT NULL,
    created TEXT NOT NULL DEFAULT (datetime('now')),
    FOREIGN KEY(source_id) REFERENCES users(id),
    FOREIGN KEY(target_id) REFERENCES users(id)
);

-- Table: work_creators
CREATE TABLE work_creators (
    id INTEGER PRIMARY KEY,
    work_id INTEGER NOT NULL,
    creator_id INTEGER NOT NULL,
    FOREIGN KEY(work_id) REFERENCES works(id),
    FOREIGN KEY(creator_id) REFERENCES creators(id)
);

-- Table: work_genres
CREATE TABLE work_genres (
    id INTEGER PRIMARY KEY,
    work_id INTEGER NOT NULL,
    genre_id INTEGER NOT NULL,
    FOREIGN KEY(work_id) REFERENCES works(id),
    FOREIGN KEY(genre_id) REFERENCES genres(id)
);

-- End of file