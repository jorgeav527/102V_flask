DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

INSERT INTO posts (title, content) VALUES ('Primer post', 'Que tal pythonistas');
INSERT INTO posts (title, content) VALUES ('Segundo post', 'Buen dia con todos');

.headers on
.mode column