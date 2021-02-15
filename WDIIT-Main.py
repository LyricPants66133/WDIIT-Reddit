print("What Day Is It Today Bot initializing", end = "...")
import praw
from datetime import datetime, timedelta, date
from threading import Timer

reddit = praw.Reddit(client_id='',
                    client_secret='',
                    user_agent='<Windows>:<WDIIT-Reddit>:<1> (by u/LyricPants66133)',
                    username='', password='')
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
sub = "WhatDayOfTheWeekIsIt"
subreddit = reddit.subreddit(sub)
print("initialized.")

x=datetime.today()
y = x.replace(day=x.day, hour=8, minute=0, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()
print(x)
def submit():
   ldigit = date.today().day%10
   ending = "^th"
   if ldigit == 1: ending = "^st"
   if ldigit == 2: ending = "^nd"
   if ldigit == 3: ending = "^rd"

   title = "What day is it today?"
   Body = "Today is " + str(days[date.today().weekday]) + " the " + str(date.today().day) + str(ending) + " of " + str(months[date.today().month - 1])

   print(str(Body))
   print(str(datetime.time(datetime.now())))

   subreddit.submit(str(title), str(Body))
   print("Submitted post to " + sub)

t = Timer(secs, submit)
t.start()
