import time
import pandas as pd
import praw
from pmaw import PushshiftAPI
from ratelimit import limits, RateLimitException, sleep_and_retry

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 60

# create main function
def main():
    reddit = praw.Reddit(
    client_id = "1s9rwR-kIsBTTh-nZBO7JA",
    client_secret = "HhrjDoYqItKREVXCWB7OzaRcAvoCwg",
    username = "Longjumping_Day337",
    password = "kalik123",
    user_agent = "my agent",
    )
    # read csv file with pandas and create a list of post id
    start_time = time.perf_counter()
    df = pd.read_csv(r"eth2_id.csv")
    list_id = df["id"].tolist()
    l = len(list_id)
    df = pd.DataFrame()
    for i, id in enumerate(list_id):
        data = get_post_info(id, reddit)
        if data.empty:
            i += 1
            continue
        df = pd.concat([df, data])
        i+=1
        print(f"{i}/{l}")
    
    # df to csv
    df.to_csv(r"done1.csv", index=False)
    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time-start_time} seconds")

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def get_post_info(post_id, reddit):
    data = {}
    submission_praw = reddit.submission(id=post_id)
    submission_praw.comment_sort = "top"
    num_comments = submission_praw.num_comments
    score = submission_praw.score
    if score > 0 and num_comments > 2:
        created = submission_praw.created
        num_comments = submission_praw.num_comments
        score = submission_praw.score
        subreddit = submission_praw.subreddit
        title = submission_praw.title
        try:
            comment_1 = submission_praw.comments[0].body
        except IndexError:
            comment_1 = ""
        try:
            comment_2 = submission_praw.comments[1].body
        except IndexError:
            comment_2 = ""
        try:
            comment_3 = submission_praw.comments[2].body
        except IndexError:
            comment_3 = ""
        data = {
            "created": created,
            "num_comments": num_comments,
            "score": score,
            "subreddit": subreddit,
            "title": title,
            "comment_1": comment_1,
            "comment_2": comment_2,
            "comment_3": comment_3,
        }
    data = pd.DataFrame(data, index=[0])
    return data
    



if __name__ == "__main__":
    main()

