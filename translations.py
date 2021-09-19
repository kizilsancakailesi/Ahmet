from config import ASSISTANT_NAME
from helpers.bot_utils import BOT_NAME, USERNAME


START_TEXT = f"👋🏻 **Merhaba**, \n\nThis is **{BOT_NAME}** \nBen Canlı yayın Botuyum, Radios, YouTube Videos & Telegram Audio / Video Telegram gruplarının Sesli sohbetlerinde video izletebilirim. Arkadaşlarınızla Grup Video Oynatıcısının Sinematik Görünümünün Tadını Çıkaralım 😉! \n\n**Telegramın Çirkin Kralı❤️ By @KizilsancakSahibi!** 👑"
HELP_TEXT = f"""
🛠-- **Setting Up Bot**:--

\u2022 Start Voice Chat In Your Group!
\u2022 Add Me (@{USERNAME}) & My Assistant (@{ASSISTANT_NAME}) To Your Group!
\u2022 Give Admin To Me (@{USERNAME}) & My Assistant (@{ASSISTANT_NAME}) In Your Group!

⚔️-- **Available Commands**:--

\u2022 `/play` - Stream An Audio
\u2022 `/stream` - Stream An Video
\u2022 `/pause` - Pause Current Stream
\u2022 `/resume` - Resume Paused Stream
\u2022 `/endstream` - End Stream & Left VC
\u2022 `/restart` - Restart Bot (Sudo Only)
"""
ABOUT_TEXT = f"💡-- **Information**:-- \n\nThis bot is created for streaming videos in telegram group video chats using several methods from WebRTC. Powered by pytgcalls the async client API for the Telegram Group Calls and Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users and Bots. \n\n**This bot licensed under GNU-GPL 3.0 License!**"
