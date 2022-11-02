from time import sleep
from pmaw import PushshiftAPI
import datetime
import time
import pandas as pd


def main():
    date_range = pd.date_range(start="2019-10-01", end="2022-9-30", freq='W')
    date_range_list = []

    for day in date_range:
        y, m, d = list(map(int, str(day).split(' ')[0].split('-')))
        date_range_list.append(int(datetime.datetime(y, m, d, 0, 0).timestamp())+86400)

    print(date_range_list)
    num_post_list = []
    start = time.perf_counter()
    api = PushshiftAPI(num_workers=40,shards_down_behavior=None,rate_limit=30,)
    subreddit = "ethereum"
    print("-------------start-------------")
    print("Beginning search for", subreddit)
    d = 0
    i = 0
    for day in date_range_list:
        r = search(subreddit, abs(day-86400*7), day, api)
        while len(r) == 0 and i < 6:
            sleep(5)
            r = search(subreddit, day, abs(day-86400*7), api)
            i += 1
        num_post_list.append(len(r))
        d += 1
        print(d, len(r), len(date_range_list), i)
        i = 0
    print("Ended search for", subreddit)
    print("--------------end--------------")

    print(len(num_post_list))
    print(num_post_list)
    df = pd.DataFrame(num_post_list, columns=['Number of posts'])
    df.to_csv(r'num_post_week.csv', sep=',',index=False)
    finish = time.perf_counter()
    print(f"Program finished in {finish-start} seconds")

def search(subreddit, after, before, api):
    submissions = api.search_submissions(subreddit=subreddit,
            after=after,
            before=before,
            filter=[],)
    return submissions



if __name__ == "__main__":
    main()