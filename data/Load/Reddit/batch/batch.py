import time
import pandas as pd
import praw
from ratelimit import limits, sleep_and_retry

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

    start_time = time.perf_counter()

    df = pd.read_csv(r"eth_id.csv")
    list_id = df["id"].tolist()
    list_id2 = [i if i.startswith('t3_') else f't3_{i}' for i in list_id]
    
    l = len(list_id)
    

    df = pd.DataFrame(get_post_info(list_id2, reddit))
    
    # df to csv
    df.to_csv(r"ethbatch.csv", index=False)
    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time-start_time} seconds")

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def get_post_info(post_id, reddit):
    data = {"num_comments": [], "score": [], "created": [], "subreddit": [], "title": [], "comment_1": [], "comment_2": [], "comment_3": [],}
    for i, submission in enumerate(reddit.info(fullnames=post_id)):
        submission.comment_sort = "top"
        num_comments = submission.num_comments
        score = submission.score
        if score > 0 and num_comments> 2:
            data["num_comments"].append(num_comments)
            data["score"].append(score)
            data["created"].append(submission.created)
            data["title"].append(submission.title)
            data["subreddit"].append(submission.subreddit)
            try:
                data["comment_1"].append(submission.comments[0].body)
            except IndexError:
                data["comment_1"].append(" ")
            try:
                data["comment_2"].append(submission.comments[1].body)
            except IndexError:
                data["comment_2"].append(" ")
            try:
                data["comment_3"].append(submission.comments[2].body)
            except IndexError:
                data["comment_3"].append(" ")
            print(f"{i}/{len(post_id)}")
    
    print(len(data["num_comments"]))
    print(len(data["created"]))
    print(len(data["comment_1"]))
    
    return data
    



if __name__ == "__main__":
    main()

