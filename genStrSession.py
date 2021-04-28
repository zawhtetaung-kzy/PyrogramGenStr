import os
import asyncio

from pyrogram import Client
from dotenv import load_dotenv

if os.path.isfile("config.env"):
    load_dotenv("config.env")


async def genStrSession() -> None:  # pylint: disable=missing-function-docstring
    async with Client(
            "codexbotz",
            api_id=int(os.environ.get("APP_ID") or input("Enter Telegram APP ID: ")),
            api_hash=os.environ.get("API_HASH") or input("Enter Telegram API HASH: "),
            device_model="CodeXBotz Ver 1.0.1"
    ) as codexbotz:
        print("\nprocessing...")
        await codexbotz.send_message(
            "me", f"<b>@CodeXBotz User Session</b>\n\n<code>{await antikozhi.export_session_string()}</code>\n\n<i>Keep this Safe and Not share anyone</i>")
        print("Done!, Check your Saved Message for String Session!")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(genStrSession())
