import os
import google.generativeai as genai
import speech_recognition as sr
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from pydub import AudioSegment  # For converting .ogg to .wav
from dotenv import load_dotenv

load_dotenv()

load_dotenv()
telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
print(f"Telegram Token: {telegram_token}")  # Debugging line
# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Function to convert voice to text
def voice_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)  # Use Google's Speech-to-Text API
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Sorry, there was an issue with the speech-to-text service."

# Function to convert .ogg to .wav
def convert_ogg_to_wav(ogg_file, wav_file):
    audio = AudioSegment.from_ogg(ogg_file)
    audio.export(wav_file, format="wav")

# Handle text messages
async def handle_text(update: Update, context):
    user_input = update.message.text
    response = model.generate_content(user_input)
    await update.message.reply_text(response.text)

# Handle voice messages
async def handle_voice(update: Update, context):
    # Download the voice message
    voice_file = await update.message.voice.get_file()
    await voice_file.download_to_drive("voice_message.ogg")
    
    # Convert .ogg to .wav
    convert_ogg_to_wav("voice_message.ogg", "voice_message.wav")
    
    # Convert the voice message to text
    text = voice_to_text("voice_message.wav")
    
    # Generate a response using Gemini
    response = model.generate_content(text)
    await update.message.reply_text(f"Voice message transcribed: {text}\n\nResponse: {response.text}")
    
    # Clean up the downloaded files
    os.remove("voice_message.ogg")
    os.remove("voice_message.wav")

# Start command
async def start(update: Update, context):
    await update.message.reply_text("Hello! Send me a text or voice message, and I'll respond using Google's Gemini AI.")

# Main function to run the bot
if __name__ == "__main__":
    # Replace with your Telegram bot token
    application = ApplicationBuilder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    application.add_handler(MessageHandler(filters.VOICE, handle_voice))
    
    # Start polling
    print("Bot is running...")
    application.run_polling()