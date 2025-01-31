<h1 align="center">Telegram Gemini AI Bot</h1>
<p align="center">A Telegram bot that uses Google's Gemini AI to respond to text and voice messages. The bot transcribes voice messages to text using Google's Speech-to-Text API and generates responses using the Gemini AI model.</p>

### Features:
- Text Message Handling: Responds to text messages using Google's Gemini AI.
- Voice Message Handling: Converts voice messages to text and generates AI-powered responses.

### Technologies Used:
- Python: The core programming language.
- python-telegram-bot: Library for interacting with the Telegram Bot API.
- Google Generative AI: For generating AI-powered responses.
- SpeechRecognition: For converting voice messages to text.
- pydub: For converting .ogg audio files to .wav.
- python-dotenv: For managing environment variables.

### Prerequisites
Before running the bot, ensure you have the following:
1. Python 3.8 or higher;
2. Telegram Bot Token;
3. Google Gemini API Key;
4. FFmpeg: Required for pydub to handle audio conversion;

### Setup Instructions:
Clone the repository:
```bash
https://github.com/RafaelPil/TelegramAIVoiceAssistant
cd TelegramAIVoiceAssistant
```

### Set Up Environment Variables:
Create a .env file in the root directory and add your API keys:
```bash
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### Install Dependencies:
Run the following command to install the required Python packages:
```bash
pip install -r requirements.txt
```
Alternatively, use the provided install_dependencies.bat file (for Windows):
```bash
install_dependencies.bat
```

### Run the Bot:
```bash
python main.py
```

### Usage:
1. Start the Bot: Send /start to your bot on Telegram.
2. Send a Text Message: The bot will respond using Google's Gemini AI.
3. Send a Voice Message: The bot will transcribe the voice message to text and generate a response.

### License
- This project is licensed under the MIT License. 
