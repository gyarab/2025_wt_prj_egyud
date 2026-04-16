from django.contrib import admin

from .models import Comment, League, Player, Rating, Season, Statistic, Team


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "founded_year")
    list_filter = ("country",)
    search_fields = ("name", "country")
    ordering = ("name",)


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = ("name", "start_year", "end_year", "is_current")
    list_filter = ("is_current", "start_year")
    search_fields = ("name",)
    ordering = ("-start_year",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "league", "city", "stadium")
    list_filter = ("league", "city")
    search_fields = ("name", "city", "stadium", "league__name")
    ordering = ("name",)
    autocomplete_fields = ("league",)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "team", "position", "age", "nationality")
    list_filter = ("position", "nationality", "team")
    search_fields = ("first_name", "last_name", "nationality", "team__name")
    ordering = ("last_name", "first_name")
    autocomplete_fields = ("team",)


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = (
        "player",
        "season",
        "goals",
        "assists",
        "appearances",
        "yellow_cards",
        "red_cards",
    )
    list_filter = ("season", "player")
    search_fields = ("player__first_name", "player__last_name", "season__name")
    ordering = ("player__last_name", "-season__start_year")
    autocomplete_fields = ("player", "season")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("player", "user", "created_at", "short_text")
    list_filter = ("created_at", "player", "user")
    search_fields = (
        "player__first_name",
        "player__last_name",
        "user__username",
        "text",
    )
    ordering = ("-created_at",)
    autocomplete_fields = ("player", "user")

    @admin.display(description="Text")
    def short_text(self, obj):
        return obj.text[:50]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("player", "user", "star_count", "created_at")
    list_filter = ("star_count", "created_at", "player", "user")
    search_fields = (
        "player__first_name",
        "player__last_name",
        "user__username",
    )
    ordering = ("-created_at",)
    autocomplete_fields = ("player", "user")
