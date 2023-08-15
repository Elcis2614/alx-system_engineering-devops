#!/usr/bin/python3
""" Conatains a function that retrieve reddit API data without
    authentication """

import json
import praw


def top_ten(subred):
    """ queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit"""
    reddit = praw.Reddit(
            client_id='Scdg-XXJgMbMrM2mvkISng',
            client_secret='eB0QJ65vWg-BoNwlghrWLQbzAHp2Ew',
            user_agent='MyAPI/0.0.1')
    try:
        subreddit = reddit.subreddit(subred)
        posts = subreddit.hot(limit=10)

        for post in posts:
            print(post.title)
    except praw.exceptions.RedditAPIException :
        print("None")
