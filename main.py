import sys
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
    assert len(sys.argv)>=2, "please provide the target user's name."
    user = get_member_id(sys.argv[1])
    notifications = [get_emoji() + ' ' + m for m in db.messages]
    response = sc.post_notifications(user, notifications)
    print("Status code: " + str(response.status_code))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"--- {time.time()-start_time} seconds ---")
