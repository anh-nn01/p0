My bot is name `AnhBot`. The bot can interact with different messages from the users, either only me (creator of the bot) or other users, depending on the message. 
However, to avoid spamming the group chat, the bot is developed to avoid interacting with other bots or the system.

To run the bot, simply go to `groupme-bot` directory (same directory of this README.md) and run the command `python3 bot.py`. 
Then, you can start interacting with the bot on GroupMe.

Specific features of the bot:
  1. For any user: send `"hi bot"` or `"hello bot"` on GroupMe. The bot will reply back with message `"This is Anh's bot! How can I help you today?"`.
  2. For any user: send `"Good morning"` on GroupMe. The bot will reply back with message `"Good morning, <USERNAME>!"`, where `<USERNAME>` is your username.
  3. For any user: send `"Good night"` on GroupMe. The bot will reply back with message `"Good night, <USERNAME>!"`, where `<USERNAME>` is your username.
  4. For any user: for all other messages/cases, the bot will reply with a funny GIF with the message as the query to the GIPHY. For example, if you message "cats", there will be an GIF of cat returned.
  5. For only my GroupMe account: if I send `"shutdown"` on GroupMe. The bot will reply back with message `"Please use Ctrl+C to shut me down!"` If other user sends this message, the bot will return with a funny GIF.
