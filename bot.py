import logindetails
import praw
import time

animals = [' dog ', ' dogs ',
           ' cat ', ' cats '
           ' rabbit ', ' rabbits ']


def login():
    print("Account login")
    r_instance = praw.Reddit(
        username=logindetails.handle,
        password=logindetails.pw,
        client_id=logindetails.cId,
        client_secret=logindetails.cSecret,
        user_agent="bot v0.1"
    )
    return r_instance


def find_animals(comment):
    for animal in animals:
        if(type(comment) != praw.models.MoreComments):
            if animal in comment.body.lower():
                return animal
    return -1


def run_bot():
    while True:
        submissions = r_instance.subreddit('all').rising(limit=10)
        for submission in submissions:
            comments_with_animals = {}
            for comment in list(submission.comments):
                animal = find_animals(comment)
                if(animal != -1):
                    comments_with_animals[comment.id] = [comment, animal]
            print(comments_with_animals)

        print("search done, sleeping for 60 sec")
        time.sleep(60)


if __name__ == '__main__':
    r_instance = login()
    run_bot()
