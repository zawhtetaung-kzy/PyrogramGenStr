import os
import asyncio

from pyrogram import Client


async def genStrSession() -> None:  # pylint: disable=missing-function-docstring
    async with Client(
            "codexbotz",
            api_id=int(input("Enter Telegram APP ID: ")),
            api_hash=input("Enter Telegram API HASH: "),
            device_model="CodeXBotz Ver 1.0.1"
    ) as codexbotz:
        print("\nprocessing...")
        codexbotz.storage.SESSION_STRING_FORMAT=">B?256sQ?"
        await codexbotz.send_message(
            "me", f"<b>@CodeXBotz User Session</b>\n\n<code>{await codexbotz.export_session_string()}</code>\n\n<i>Keep this Safe and Not share anyone</i>")
        print("Done!, Check your Saved Message for String Session!")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(genStrSession())
