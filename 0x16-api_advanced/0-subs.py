#!/usr/bin/python3
import requests
import json


def number_of_subscribers(subred):
    """ queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    try:
        url = 'https://www.reddit.com/r/{}/about.json'.format(subred)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_count = response.json()['data']['subscribers']
            return (user_count)
        else:
            return 0
    except Exception:
        return (0)
