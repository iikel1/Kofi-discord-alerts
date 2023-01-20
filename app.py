import json
import os
from flask import Flask, request
from discord_webhook import DiscordWebhook, DiscordEmbed

app = Flask(__name__)

@app.route('/')
def index():
    return 'Kofi is online'

@app.route('/post', methods=['POST'])
def post():
    data = request.form['data']
    data = json.loads(data)
    KofiToken = os.getenv('KOFITOKEN')
    ShowAmount = os.getenv('SHOWAMOUNT')
    color = os.getenv('EMBEDCOLOR')

    webhook = DiscordWebhook(url = os.getenv('WEBHOOK'))
    # Check if the post from Ko-Fi
    if data['verification_token'] == f'{KofiToken}':
        user = data['from_name']
        amount = data['amount']
        
            
        embed = DiscordEmbed(title='**New Ko-Fi Supporter!**', color=color)
        embed.description = f'Thanks {user} for your Support'
        if ShowAmount == True :
            embed.description = f'Thank {user}, for your support of ${amount}'
        
        # Send the webhook
        webhook.add_embed(embed)
        response = webhook.execute()
        
        return 'succses'


if __name__ == "__main__":
    # app.run(
    #     host=os.getenv("HOST", "0.0.0.0"),
    #     port=os.getenv("PORT", 8000),
    # )
    app.run(debug=True)