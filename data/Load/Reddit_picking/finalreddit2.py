import praw



# create main function
def main():
    reddit = praw.Reddit(
    client_id = "1s9rwR-kIsBTTh-nZBO7JA",
    client_secret = "HhrjDoYqItKREVXCWB7OzaRcAvoCwg",
    username = "Longjumping_Day337",
    password = "kalik123",
    user_agent = "my agent",
    )
    try:
        sub = reddit.submission(id="dbruyz")
    except Exception as e:
        print(e)
    sub.comment_sort = "top"
    print(sub.comments[0])

if __name__ == "__main__":
    main()

