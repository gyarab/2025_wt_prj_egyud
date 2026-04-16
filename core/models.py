from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class League(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Liga"
        verbose_name_plural = "Ligy"

    def __str__(self):
        return f"{self.name} ({self.country})"


class Season(models.Model):
    name = models.CharField(max_length=20, unique=True)
    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ["-start_year", "-end_year"]
        verbose_name = "Sezona"
        verbose_name_plural = "Sezony"

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    stadium = models.CharField(max_length=100)
    league = models.ForeignKey(
        League,
        on_delete=models.CASCADE,
        related_name="teams",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Tým"
        verbose_name_plural = "Týmy"
        constraints = [
            models.UniqueConstraint(
                fields=["name", "league"],
                name="unique_team_name_per_league",
            )
        ]

    def __str__(self):
        return self.name


class Player(models.Model):
    POSITION_GOALKEEPER = "GK"
    POSITION_DEFENDER = "DF"
    POSITION_MIDFIELDER = "MF"
    POSITION_FORWARD = "FW"
    POSITION_CHOICES = [
        (POSITION_GOALKEEPER, "Brankář"),
        (POSITION_DEFENDER, "Obránce"),
        (POSITION_MIDFIELDER, "Záložník"),
        (POSITION_FORWARD, "Útočník"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    nationality = models.CharField(max_length=100)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="players",
    )

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Hráč"
        verbose_name_plural = "Hráči"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Statistic(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="statistics",
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        related_name="statistics",
    )
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    yellow_cards = models.PositiveIntegerField(default=0)
    red_cards = models.PositiveIntegerField(default=0)
    appearances = models.PositiveIntegerField(default=0)
    minutes_played = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["player__last_name", "-season__start_year"]
        verbose_name = "Statistika"
        verbose_name_plural = "Statistiky"
        constraints = [
            models.UniqueConstraint(
                fields=["player", "season"],
                name="unique_player_statistic_per_season",
            )
        ]

    def __str__(self):
        return f"{self.player} - {self.season}"


class Comment(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="player_comments",
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Komentář"
        verbose_name_plural = "Komentáře"

    def __str__(self):
        return f"Komentář: {self.user} -> {self.player}"


class Rating(models.Model):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="ratings",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="player_ratings",
    )
    star_count = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Hodnocení"
        verbose_name_plural = "Hodnocení"
        constraints = [
            models.UniqueConstraint(
                fields=["player", "user"],
                name="unique_player_rating_per_user",
            )
        ]

    def __str__(self):
        return f"{self.player} - {self.star_count}/5"
