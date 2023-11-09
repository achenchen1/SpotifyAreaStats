from django.db import models


# Create your models here.
class Artists(models.Model):
    name = models.CharField(("Artist's name"), max_length=64)


class Users(models.Model):
    name = models.CharField(("User's name"), max_length=64)


class UserArtistPlays(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, to_field="id")
    artist = models.ForeignKey(Artists, on_delete=models.CASCADE, to_field="id")
    plays = models.IntegerField("Number of times this user has played this artist")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["user", "artist"], name="user_artist_key")
        ]

        indexes = [models.Index(fields=["user", "artist"], name="user_artist_key")]
