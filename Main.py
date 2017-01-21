import praw
import twichemote_lib
import time

# General information
BOT_NAME = "Twitch emote corrector"
CREATOR = "/u/lukevastus"
VERSION = "1.03"

# OAuth2 credentials, extremely important!
# If you have already edited your local praw.ini file, fill in your additional site name:
# (see http://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html)
SITE_NAME = "bot1"
# If not, you must fill these fields:
USERAGENT = ""
CLIENT_ID = ""
CLIENT_SECRET = ""
USERNAME = ""
PASSWORD = ""

# Custom configurations
SUBREDDIT = "dota2"
SUBMISSION_LIMIT = 20
COMMENT_LIMIT = 5
SLEEP_TIME = 47
BOT_INFO_TEXT = "***\n\n---*This is a testrun for the %s bot (V%s) created by %s, view its [source code]" \
                "(https://github.com/lukevastus/Twitch_emote_bot)*---" \
                %(BOT_NAME, VERSION, CREATOR)


def check(comment_name):
    if comment_name in comments_list:
        # print("Comment already visited.")
        return True
    else:
        comments_list.append(comment_name)
        # print("Adding new comment to file...")
        file.write(comment_name + "\n")
        return False


def find_emotes(submission):
    counter = 0
    # Flatten the comment tree under the submission into a list
    submission.comments.replace_more(limit=0)
    # Traverse the list of comment
    for comment in submission.comments.list():
        if check(comment.fullname):
            continue

        comment_text = comment.body
        comment_text_lower = comment_text.lower()

        # If the comment miscapitalizes an emote, reply it
        for emote, num in twichemote_lib.emote_lib.items():
            if (emote.lower() in comment_text_lower) and (emote not in comment_text):

                print("Miscapitalization found!")
                reply_text = "Do you mean **[%s](https://twitchemotes.com/emote/%s)** instead?\n\n" \
                             "Capitalization matters when you are typing emotes!\n\n" % (emote, str(num)) \
                             + BOT_INFO_TEXT
                print("Posting reply...")
                comment.reply(reply_text)

                counter += 1
                if counter == COMMENT_LIMIT:
                    return

                print("Waiting......")
                time.sleep(SLEEP_TIME)
                break

# Open the file containing data of all comments that are already traversed in previous runs
print("Importing visited comment data...")
file = open("comments_visited.txt", "r+")
comments_list = file.read().splitlines()

# Login onto Reddit
if SITE_NAME:
    r = praw.Reddit(site_name=SITE_NAME)
else:
    r = praw.Reddit(user_agent=USERAGENT, client_id=CLIENT_ID, client_secet=CLIENT_SECRET,
                    username=USERNAME, password=PASSWORD)

# Browse the subreddit of interest and traverse each submission
subreddit = r.subreddit(SUBREDDIT)
for thread in subreddit.hot(limit=SUBMISSION_LIMIT):
    print("Traversing submission...")
    find_emotes(thread)

# Close the data file
file.close()

# Fun Test: find arteezy!
"""rtz_text = ["arteezy", "artour", "rtz", "rtc"]


def find_arteezy(submission):
    submission.comments.replace_more(limit=0)
    for comment in submission.comments.list():
        comment_text = comment.body.lower()
        for item in rtz_text:
            if item in comment_text:
                print("RTZ found!")

                reply_text = "The glorious name of **Artour Arteezy Babaev** is mentioned again!\n\n" \
                             "[Here](https://www.twitch.tv/arteezy) is his stream. " \
                             "[Here](https://www.youtube.com/playlist?list=PLg8WgbCZRajTD1Kh5fHE_QSjGazxNCuxv) " \
                             "is his playlist.\n\n" \

                comment.reply(reply_text)
                print("Time 2 wait LUL...")
                time.sleep(SLEEP_TIME)
                return"""
