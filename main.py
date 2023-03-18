from pyrogram import Client

plugins = dict(root="plugins")

app = Client(
    name="youtube",
    plugins=plugins,
    api_id=27932826,
    api_hash="5df31febb1087b80c404396f4d00360c",
    bot_token="6223322236:AAHZ3qqs3vPc5o-Wiz-pdFOJ4SpQcnrlLHo",
    workers=50
)

app.run()
