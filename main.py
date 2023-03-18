from pyrogram import Client

plugins = dict(root="plugins")

app = Client(
    name="youtube",
    plugins=plugins,
    api_id=,
    api_hash="",
    bot_token="",
    workers=50
)

app.run()
