import praw
import random
from decouple import config
import filter

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
    'nosleep',
    'TrueOffMyChest',
    'pettyrevenge',
    'ProRevenge'
]


def getRandomSubreddit():
    randomSubreddit = random.choice(subreddits)

    return randomSubreddit


def getRandomSubmission():
    subreddit = getRandomSubreddit()
    for submission in reddit.subreddit(subreddit).hot(limit=25):
        submissions.append({
            "subreddit": subreddit,
            "author": submission.author.name,
            "title": submission.title,
            "text": submission.selftext
        })

    randomSubmission = random.choice(submissions)

    randomSubmission['text'] = filter.removeUrlsFromText(
        randomSubmission['text'])
    randomSubmission['text'] = randomSubmission['text'][:1500]

    print(randomSubmission)

    return randomSubmission
