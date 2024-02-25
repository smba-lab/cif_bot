# -*- coding: utf-8 -*-
"""
Telegram-bot - cif file Descriptor!
Send the cif file and it render it and tell about crystall structure.

"""

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
from telegram.ext.dispatcher import run_async

import wikipedia
import os
import re
import time
import toolboxer

# get telegram token
with open('bron.txt', 'r') as file:
    TOKEN = file.read()


# Define the start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the cif file Descriptor!\
 Send me the cif file and i render it and tell\
 about it.')

# Define the wikipedia option
def get_wikipedia_info(update: Update, context: CallbackContext) -> None:
    topic = ' '.join(context.args)
    try:
        summary = wikipedia.summary(topic, sentences=3)
        update.message.reply_text(summary)
    except wikipedia.exceptions.PageError:
        update.message.reply_text('Sorry, I could not find any \
                                  information about that topic.')
    except wikipedia.exceptions.DisambiguationError as e:
        update.message.reply_text(f"Sorry, I found multiple results.\
                                  Try to be more specific: \
                                      {', '.join(e.options)}")

# Define the file command handler
def request_file(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Please upload the file.')

# Define the file processing handler
@run_async
def receive_file(update: Update, context: CallbackContext) -> None:
    # get cif file
    file_id = update.message.document.file_id
    new_file = context.bot.get_file(file_id)
    new_file.download('received_file.cif')
    
    # get metadata from cif file
    chat_id = update.message.chat_id
    cif_infos= toolboxer.cif_info()
    context.bot.send_message(chat_id=chat_id, text=cif_infos)
    
    # generate info, xyz format and rendered image of crystal
    toolboxer.session_cleaner()
    toolboxer.get_infos()
    toolboxer.cif_to_xyz('received_file.cif')
    toolboxer.render_xyz()
    
    # send rendered crystal    
    photo_path = 'output_file.xyz.png'
    if os.path.exists(photo_path):
        with open(photo_path, 'rb') as photo_file:
            update.message.reply_photo(photo=photo_file)
    else:
        update.message.reply_text('Sorry, the photo file was not found.')
    
    # send desctiption about crystal structure
    time.sleep(2)
    with open('info.txt', 'r', encoding="utf-8") as file:
        content = file.read()
        context.bot.send_message(chat_id=chat_id, text=content)


# Define the video command handler
def send_video(update: Update, context: CallbackContext) -> None:
    video_path = 'animation.mp4'
    if os.path.exists(video_path):
        with open(video_path, 'rb') as video_file:
            update.message.reply_video(video=video_file, 
                                       caption='Here is the video!')
        
    else:
        update.message.reply_text('Sorry, render is not completed')

   
def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("info", get_wikipedia_info))
    dispatcher.add_handler(CommandHandler("file", request_file))
    dispatcher.add_handler(MessageHandler(Filters.document, receive_file))
    dispatcher.add_handler(CommandHandler("video", send_video))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

