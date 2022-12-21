import praw
import random
from decouple import config

submissions = []

reddit = praw.Reddit(
    client_id=config('CLIENT_ID'),
    client_secret=config('CLIENT_SECRET'),
    password=config('PASSWORD'),
    user_agent=config('USER_AGENT'),
    username=config('USERNAME'),
)

subreddits = [
    'AmItheAsshole',
    'confession',
    'nosleep'
]

def getRandomSubreddit():
    randomSubreddit = random.choice(subreddits)

    return randomSubreddit

def getRandomSubmission():
    subreddit = getRandomSubreddit()
    for submission in reddit.subreddit(subreddit).hot(limit=25):
        submissions.append(submission.selftext)
    
    randomSubmission = random.choice(submissions)
    print(randomSubmission)

    return randomSubmission
