from django.db import models
from django.utils import timezone

# CREATE TABLE creators (
#     id INTEGER PRIMARY KEY,
#     creator varchar(255) NOT NULL
# );


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/user_{0}/{1}'.format(instance.user.username, filename)


class Creator(models.Model):
    creator = models.CharField(max_length=255)

    def __str__(self):
        return self.creator

####

# CREATE TABLE users (
#     id INTEGER PRIMARY KEY,
#     username varchar(50) NOT NULL,
#     name varchar(255) NOT NULL,
#     email varchar(255) NOT NULL,
#     password varchar(255) NOT NULL,
#     created TEXT NOT NULL DEFAULT (datetime('now'))
# );


class User(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)
    pic = models.FileField(upload_to=user_directory_path)

#####

# CREATE TABLE works (
#     id INTEGER PRIMARY KEY,
#     name varchar(255) NOT NULL,
#     type varchar(255) NOT NULL,
#     publisher varchar(255) NULL,
#     synopsis text NULL,
#     released date NOT NULL,
#     img_link text NULL
# );


class Work(models.Model):
    TYPES = (
        ('anime', 'Anime'),
        ('livro', 'Livro'),
        ('filme', 'Filme'),
        ('jogo', 'Jogo'),
        ('serie', 'Série')
    )
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=TYPES)
    publisher = models.CharField(max_length=255, null=True)
    synopsis = models.TextField(null=True)
    released = models.DateField()
    img_link = models.URLField(max_length=200, null=True)
    avg_rating = models.FloatField(null=True)
    qtd_rating = models.FloatField(null=True)

    def __str__(self):
        return self.name

####

# CREATE TABLE genres (
#     id INTEGER PRIMARY KEY,
#     genre varchar(255) NOT NULL
# );


class Genre(models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.genre


# COM FOREIGNKEY

# CREATE TABLE reviews (
#     id INTEGER PRIMARY KEY,
#     user_id INTEGER NOT NULL,
#     work_id INTEGER NOT NULL,
#     review_id INTEGER NULL,
#     score int NOT NULL,
#     review text NULL,
#     created TEXT NOT NULL DEFAULT (datetime('now')),
#     FOREIGN KEY(user_id) REFERENCES users(id),
#     FOREIGN KEY(work_id) REFERENCES works(id),
#     FOREIGN KEY(review_id) REFERENCES reviews(id)
# );


class Review(models.Model):
    user_id = models.ForeignKey(
        User, on_delete=models.PROTECT,  related_name='%(class)s_reviews_created')
    work_id = models.ForeignKey(
        Work, on_delete=models.PROTECT,  related_name='%(class)s_reviews_created')
    review_id = models.ForeignKey(
        'self', on_delete=models.PROTECT,  related_name='%(class)s_reviews_created')
    score = models.IntegerField()
    review = models.TextField()
    created = models.DateTimeField(default=timezone.now)

####

# CREATE TABLE review_likes (
#     id INTEGER PRIMARY KEY,
#     user_id INTEGER NOT NULL,
#     review_id INTEGER NOT NULL,
#     type INT NOT NULL,
#     created TEXT NOT NULL DEFAULT (datetime('now')),
#     FOREIGN KEY(review_id) REFERENCES reviews(id)
# );


class Review_Like(models.Model):
    TYPES = (
        (0, 'Não Curti'),
        (1, 'Curti')
    )
    user_id = models.ForeignKey(
        User, on_delete=models.PROTECT,  related_name='%(class)s_reviews_likes_created')
    review_id = models.ForeignKey(
        Review, on_delete=models.PROTECT,  related_name='%(class)s_reviews_likes_created')
    type = models.CharField(max_length=25, choices=TYPES)
    created = models.DateTimeField(default=timezone.now)

####

# CREATE TABLE shelf (
#     id INTEGER PRIMARY KEY,
#     work_id INTEGER NOT NULL,
#     status_id INTEGER NOT NULL,
#     user_id INTEGER NOT NULL,
#     FOREIGN KEY(work_id) REFERENCES works(id),
#     FOREIGN KEY(user_id) REFERENCES users(id),
#     FOREIGN KEY(status_id) REFERENCES statuses(id)
# );


class Shelf(models.Model):
    STATUSES = (
        ('in consume', 'In Consume'),
        ('consumed', 'Consumed'),
        ('interest list', 'Interest List'),
        ('dropped', 'Dropped')
    )
    work_id = models.ForeignKey(
        Work, on_delete=models.PROTECT,  related_name='%(class)s_shelves_created')
    user_id = models.ForeignKey(
        User, on_delete=models.PROTECT,  related_name='%(class)s_shelves_created')
    status = models.CharField(max_length=30, choices=STATUSES)
    # score = models.IntegerField() --  Será que deveríamos?

####

# CREATE TABLE user_followers (
#     id INTEGER PRIMARY KEY,
#     source_id INTEGER NOT NULL,
#     target_id INTEGER NOT NULL,
#     created TEXT NOT NULL DEFAULT (datetime('now')),
#     FOREIGN KEY(source_id) REFERENCES users(id),
#     FOREIGN KEY(target_id) REFERENCES users(id)
# );


class User_Follower(models.Model):
    source_id = models.ForeignKey(
        User, on_delete=models.PROTECT,  related_name='source_user_followers_created')
    target_id = models.ForeignKey(
        User, on_delete=models.PROTECT,  related_name='target_user_followers_created')
    created = models.DateTimeField(default=timezone.now)

####

# CREATE TABLE work_creators (
#     id INTEGER PRIMARY KEY,
#     work_id INTEGER NOT NULL,
#     creator_id INTEGER NOT NULL,
#     FOREIGN KEY(work_id) REFERENCES works(id),
#     FOREIGN KEY(creator_id) REFERENCES creators(id)
# );


class Work_Creator(models.Model):
    work_id = models.ForeignKey(
        Work, on_delete=models.PROTECT,  related_name='%(class)s_work_creators_created')
    creator_id = models.ForeignKey(
        Creator, on_delete=models.PROTECT,  related_name='%(class)s_work_creators_created')

####

# CREATE TABLE work_genres (
#     id INTEGER PRIMARY KEY,
#     work_id INTEGER NOT NULL,
#     genre_id INTEGER NOT NULL,
#     FOREIGN KEY(work_id) REFERENCES works(id),
#     FOREIGN KEY(genre_id) REFERENCES genres(id)
# );


class Work_Genre(models.Model):
    work_id = models.ForeignKey(
        Work, on_delete=models.PROTECT,  related_name='%(class)s_work_genres_created')
    genre_id = models.ForeignKey(
        Genre, on_delete=models.PROTECT,  related_name='%(class)s_work_genres_created')
