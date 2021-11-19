"""    
edit your crontab and you can run this script at each hour:
    0 * * * * /path/to/app/venv/bin/python3 /path/to/app/bot2.py >> /path/to/app/log 2>&1
"""

# imports
from instapy import InstaPy
from instapy import smart_run
import random

exit()

# login credentials
insta_username = 'YOURUSERNAME'  # <- enter username here
insta_password = 'YOURPASS'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    # general settings
    session.set_relationship_bounds(enabled=True,
                                    delimit_by_numbers=True,
                                    min_followers=104,
                                    max_followers=10004,
                                    min_following=104,
                                    max_following=10004,
                                    min_posts=3)

    session.set_skip_users(skip_private=False)

    session.set_user_interact(amount=3, randomize=False, percentage=100)

    tags = ["onetagyouwanttoliketheposts"]
    session.like_by_tags(tags, amount=3, randomize=True)

    following = ["select", "random", "profiles", "and", "this", "bot", "will", "follow", "its", "followers"]

    following = random.sample(following, 4)

    session.follow_user_followers(following, amount=6, randomize=True, interact=True, sleep_delay=444)
