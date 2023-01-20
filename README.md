# Ko-Fi Discord Alerts Server

Simple Flask server to translate Ko-fi webhook to Discord Webhook!

# Installation
    - Requires Python 3 or higher. Get it from [Here](https://www.python.org/downloads)
    - You need to install Libraries from requirements.txt `pip install -r requirements.txt`
    - After the installation has complemeted, configure the server by copying the .env.example, naming it to `.env` and editing the values inside it.
    - Start the server by `python app.py`

# Usage
    Go to https://ko-fi.com/manage/webhooks and enter your server IP/domain and add `/post` to the end. For example, `http://example.com/post`, hit **Update**. Remember to copy Ko-fi Token, As long as your server is running, you will receive notifications automatically to the webhook you have provided in the configuration file! Enjoy :)

Check out Glitch.com or Repl.it if you would like your server to be hosted for free rather than paying for VPS or Dedicated server!


# Issues and Contributors
    Feel free to submit issues, ideas and others as well as contribute to the project! 