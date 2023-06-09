# Generated by Django 4.1.7 on 2023-04-05 20:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_appuser_all_interests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='all_interests',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=('Art', 'Music', 'Sports', 'Games', 'Food', 'Travel', 'Fashion', 'Technology', 'Science', 'Nature', 'Animals', 'Politics', 'Religion', 'History', 'Education', 'Health', 'Fitness', 'Finance', 'Business', 'Entertainment', 'News', 'Weather', 'Ocean', 'Space', 'Cars', 'Plants', 'Books', 'Movies', 'TV', 'Theater', 'Comedy', 'Dance', 'Museums', 'Gardens', 'Parks', 'Zoos', 'Festivals', 'Concerts', 'Parties', 'Clubs', 'Bars', 'Coffee', 'Restaurants', 'Shopping', 'Hiking', 'Camping', 'Skiing', 'Snowboarding', 'Surfing', 'Swimming', 'Running', 'Biking', 'Yoga', 'Meditation', 'Cooking', 'Dining', 'Cruises', 'Road Trips', 'Vacations', 'Sightseeing', 'Photography', 'Painting', 'Sculpting', 'Writing', 'Poetry', 'Drama', 'Singing', 'Gaming', 'Board Games', 'Card Games', 'Video Games', 'Puzzles', 'Chess', 'Checkers', 'Backgammon', 'Monopoly', 'Scrabble', 'Candy', 'Ice Cream', 'Chocolate', 'Cookies', 'Pizza', 'Burgers', 'Sandwiches', 'Sushi', 'Tacos', 'Burritos', 'Pasta', 'Salads', 'Soups', 'Stews', 'Seafood', 'Steak', 'Chicken', 'Beef', 'Lamb', 'Pork', 'Vegetarian', 'Vegan', 'Gluten Free', 'Dairy Free', 'Eggs', 'Nuts', 'Spicy', 'Sweet', 'Salty', 'Sour', 'Bitter', 'Hot', 'Cold', 'Warm', 'Dry', 'Wet', 'Fast', 'Slow', 'High', 'Low', 'Big', 'Small', 'Long', 'Short', 'Round', 'Square', 'Flat', 'Tall', 'Short', 'Wide', 'Narrow', 'Deep', 'Shallow', 'Light', 'Heavy', 'Soft', 'Hard', 'Smooth', 'Rough', 'Windy', 'Rainy', 'Sunny', 'Cloudy', 'Snowy', 'Hot', 'Cold', 'Wet', 'Dry', 'Breezy', 'Humid', 'Foggy', 'Misty', 'Stormy', 'Tropical', 'Tundra', 'Reading', 'Sleep'), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='interests',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, default=[], null=True, size=None),
        ),
    ]
