import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox310acb08f8354f25b2d1bc90ab362c24.mailgun.org/messages",
        auth=("api", "27c7030faf26f7d5124222aa5bb179a2-b0aac6d0-8d3a824e"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox310acb08f8354f25b2d1bc90ab362c24.mailgun.org>",
              "to": "Rahul Vyas <rahul.class@gmail.com>",
              "subject": "Eat bitch!",
              "text": "Congratulations Rahul Vyas, you just sent an email with Mailgun!  You are truly awesome!"})

send_simple_message()