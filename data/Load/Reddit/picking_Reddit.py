import datetime
import random
import time
import praw
import pandas as pd
import requests
from ratelimit import limits, sleep_and_retry

ONE_MINUTE = 60
MAX_CALLS_PER_MINUTE = 60

def main():
    start_time = time.perf_counter()

    '''
    cambiar el nombre del archivo en la linea de abajo
    y no olvidar tambien cambiarla en la linea 32
    '''
    df = csv_to_df(r"Crypto_Currency_News.csv")
    df["id"] = df["id"].apply(lambda x: 't3_' + x)
    '''
    Si la columna de 'created_utc' no tiene el formato correcto 
    descomentar la linea de abajo
    '''
    #df = unix_to_date(df, "created_utc")

    df = append_comments(df, get_praw())
    '''
    tambien cambiar el nobmre del archivo
    de preferencia agregar '(nombre del subreddit)_comments' para distinguir
    '''
    df.to_csv(r'Crypto_Currency_News_comments.csv', sep=',',index=False) 

    finish_time = time.perf_counter()
    print(f"Program finished in {finish_time-start_time} seconds")
    

"""
returns reddit object to get top comment
"""
def get_praw():
    reddit = praw.Reddit(
    client_id = "1s9rwR-kIsBTTh-nZBO7JA",
    client_secret = "HhrjDoYqItKREVXCWB7OzaRcAvoCwg",
    username = "Longjumping_Day337",
    password = "kalik123",
    user_agent = "my agent",
    )
    return reddit

"""
returns top comment for sumbission id

example: get_top_comment("dbruyz")

example 2:
for sub_id in data["data"]:
    print(sub_id)
    submission_praw = reddit.submission(id=sub_id)
    submission_praw.comment_sort = "top"
    print(submission_praw.comments[0].body)

Typical attributes of a comment are listed in link below:
- https://praw.readthedocs.io/en/stable/code_overview/models/comment.html
"""
@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def get_top3_comment(reddit, sumbission_id):
    max_attempts = 10
    attempts = 0
    while attempts < max_attempts:
        try:
            sub = reddit.submission(id=sumbission_id)
            sub.comment_sort = "top"
            return sub.comments[:3]
        except Exception as e:
            attempts += 1
            print(f"Error: {e}")
            print(f"Retrying... {attempts}/{max_attempts}")
            time.sleep((2 ** attempts) + random.random())
    return sub.comments[:3]

    

"""
Creates a request to pushshift api and returns a json object with the top ten posts found
Uses tag (function name) to determine which params to use
"""
def get_data(**kargs):
    url = "https://api.pushshift.io/reddit/search/submission/"
    params = {}
    if kargs.get("tag") == "get_submissions":
        params = {
            "subreddit": kargs.get("subreddit"),
            "size": kargs.get("size"),
            "fields": kargs.get("fields"),
            "sort": kargs.get("sort"),
            "sort_type": kargs.get("sort_type"),
            "after": kargs.get("after"),
            "before": kargs.get("before"),
        }
    elif kargs.get("tag") == "get_post_id":
        params = {
            "subreddit": kargs.get("subreddit"),
            #"limit": kargs.get("limit"),
            "size": kargs.get("size"),
            "fields": kargs.get("fields"),
            "sort_type": "created_utc",
            "after": kargs.get("after"),
            "before": kargs.get("before"),
        }
    else:
        return None
    
    max_attempts = 10
    attempts = 0
    while attempts < max_attempts:
        try:
            r = requests.get(url, params=params)
            return r.json()
        except requests.exceptions.RequestException as e:
            attempts += 1
            print(f"Error: {e}")
            print(f"Retrying... {attempts}/{max_attempts}")
            time.sleep((2 ** attempts) + random.random())
    

"""
Return dataframe containing top 10 posts in a day for each subreddit
only works with list of days!!!
"""
def get_submissions(subreddits, date_range_list):
    df = pd.DataFrame()
    l = len(date_range_list)
    for subreddit in subreddits:
        d = 0
        for day in date_range_list:
                data = get_data(tag="get_submissions",
                    subreddit=subreddit,
                    size=10,
                    fields=["subreddit", "title", "score", "num_comments", "permalink", "created_utc", "id"],
                    sort="desc",
                    sort_type="score",
                    after=day,
                    before=day+86400)
                df = pd.concat([df, pd.DataFrame(data["data"])])
                d += 1
                print(d, l)
    return df

def get_post_id(subreddits, after, before):
    df = pd.DataFrame()
    for subreddit in subreddits:
        data = get_data(tag="get_post_id",
            subreddit=subreddit,
            #limit=None,
            size=1000,
            fields=["subreddit","id"],
            after=after,
            before=before)
        df = pd.concat([df, pd.DataFrame(data["data"])])
                
    return df
"""
Return a list of days in unix time stamp
"""
def get_date_range(start, end):
    date_range = pd.date_range(start=start, end=end, freq="D")
    date_range_list = []

    for day in date_range:
        y, m, d = list(map(int, str(day).split(' ')[0].split('-')))
        date_range_list.append(int(datetime.datetime(y, m, d, 0, 0).timestamp()))
    return date_range_list

# csv to df function
def csv_to_df(file):
    df = pd.read_csv(file)
    return df

# @sleep_and_retry
# @limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def append_comments(df, reddit):
    # from df get column of post id
    # for each post id get top 3 comments
    # append to df
    comment_1 = []
    comment_2 = []
    comment_3 = []
    for i, submission in enumerate(reddit.info(fullnames=list(df['id']))):
        submission.comment_sort = "top"
        comments = submission.comments
        # append comment to list if it exists
        if len(comments) >= 1:
            comment_1.append(comments[0].body)
        else:
            comment_1.append("")
        if len(comments) >= 2:
            comment_2.append(comments[1].body)
        else:
            comment_2.append("")
        if len(comments) >= 3:
            comment_3.append(comments[2].body)
        else:
            comment_3.append("")
        print(f"done {i} of {len(df['id'])}")

    df["comment_1"] = pd.Series(comment_1)
    df["comment_2"] = pd.Series(comment_2)
    df["comment_3"] = pd.Series(comment_3)
    return df

# apply map unix time to date to df column
def unix_to_date(df, column):
    df[column] = df[column].apply(lambda x: datetime.datetime.fromtimestamp(x).strftime('%Y-%m-%d'))
    return df



if __name__ == '__main__':
    main()


"""
url_list = ['https://api.pushshift.io/reddit/search/submission/?subreddit=wallstreetbets&sort=desc&sort_type=score&size=10&after=7d&fields=score,title', 
            'https://api.pushshift.io/reddit/search/submission/?q=wallstreetbets']

def download_file(url, file_name):
    try:
        html = requests.get(url, stream=True)
        #js = json.loads(html.json())
        #print(json.dumps(js, ident=4))
        open(f'{file_name}.json', 'wb').write(html.content)
        return html.status_code
    except requests.exceptions.RequestException as e:
        return e

def runner():
    threads= []
    with ThreadPoolExecutor(max_workers=20) as executor:
        for url in url_list:
            file_name = uuid.uuid1()
            threads.append(executor.submit(download_file, url, file_name))
            
        for task in as_completed(threads):
            print(task.result()) 

"""
