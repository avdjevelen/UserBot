from pyrogram import Client, filters
from config import api_id, api_hash

# Create a Pyrogram client
app = Client("userbot", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.channel)
async def comment_on_post(client, message):
    try:
        print(f"Channel ID: {message.chat.id}")
        # Ensure the channel has a linked discussion group
        if message.chat:
            # Fetch the thread starter message ID in the discussion group
            linked_message = await client.get_discussion_message(message.chat.id, message.id)

            # Log the linked discussion group and message ID
            print(f"Discussion thread message ID: {linked_message.id}")

            # Compose your comment
            comment_text = "This is my automated comment in the discussion thread!"

            # Post the comment in the discussion group
            await client.send_message(
                chat_id=linked_message.chat.id,
                text=comment_text,
                reply_to_message_id=linked_message.id  # Reply to the discussion thread
            )
            print("Comment posted in discussion thread!")
    except Exception as e:
        print(f"Error: {e}")

@app.on_message(filters.channel)
async def log_channel_id(client, message):
    print(f"ChannelID: {message.chat.id}")

@app.on_message(filters.private)
async def connection_test(client, message):
    print(f"Received message from {message.from_user.username or message.from_user.id}")

if __name__ == "__main__":
    print("Starting userbot...")
    app.run()
