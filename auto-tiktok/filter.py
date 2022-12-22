import re
from better_profanity import profanity

#MIGHT ADD FILTERING NEW LINES SIGNS (\N\N) AS WELL

def censorBadWords(text):
    censored = profanity.censor(text)
    return censored

def removeUrlsFromText(text):
    text = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", text)
    return text
