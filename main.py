import simple_client as sc

# channel = "#random"

messages = [
    "http://kerio.ydrogiosonline.gr still has no TLS encryption.",
    "Web apps and servers still use 5 billion different certificates.",
    "fl1rd still dies once every now and then.",
    "Prometheus still doesn't monitor the main production web server (amadeus)."
]


def main():
    user = "@trafalgar1618"
    responses = sc.post_notifications(user, messages)


if __name__ == "__main__":
    main()
