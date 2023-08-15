#!/usr/bin/python3
""" Conatains a function that retrieve reddit API data without
    authentication """

import json
import requests


def top_ten(subred):
    """ queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit"""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    try:
        url = 'https://www.reddit.com/r/{}/top.json'.format(subred)
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            posts = response.json()['data']['children'][:10]
            for post in posts:
                print(post['data']['title'])
    except Exception:
        return (0)
