import time
import random
import storage as db
import simple_client as sc


def get_member_id(username):
    return "@" + db.members[username]


def get_channel_id(channelname):
    return "#" + db.channels[channelname]


def get_emoji():
    emoji = random.choice(db.emojis)
    return ":" + emoji + ":"


def main():
    user = get_member_id("kenji")
    responses = [sc.post_notification(user, m, get_emoji()) for m in db.messages]


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"--- {time.time()-start_time} seconds ---")
