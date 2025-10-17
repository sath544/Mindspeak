# Mindspeak AI Assistant

**Mindspeak** is a student-built AI assistant designed to be a stress-buster, English improvement companion, and daily productivity assistant. It combines human-like conversational AI with helpful features to support users in their daily routine.

## Features

* **Conversational AI**: Chat with Mindspeak like a human, powered by AI.
* **English Assistant**: Correct your sentences and improve grammar.
* **StressBuster Mode**: Get quick stress-relief prompts, motivational tips, and guided exercises.
* **Daily 15-Min Reminder**: Schedule personal check-ins or tasks to help you stay productive.
* **Voice Interaction**: Talk to Mindspeak using microphone input (prototype).

## Quick Start (Local Run)

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```
2. Activate the environment:

   * Windows: `venv\Scripts\activate`
   * Mac/Linux: `source venv/bin/activate`
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Set your OpenAI API key in environment variables or `.env` file:

   ```bash
   export OPENAI_API_KEY="sk-..."  # Mac/Linux
   setx OPENAI_API_KEY "sk-..."   # Windows
   ```
5. Run the app:

   ```bash
   streamlit run app.py
   ```

## Deploying to Streamlit Cloud

1. Push this folder to a GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io) and connect your GitHub account.
3. Create a new app → select the repository and `app.py` as main file.
4. Add your `OPENAI_API_KEY` in Streamlit Secrets.
5. Deploy → your app will be live at `https://<your-app-name>.streamlit.app`

## Future Enhancements

* SMS or voice reminders using Twilio (free trial).
* Browser-based voice interaction using Web Speech API.
* User accounts and preference storage using Firebase.
* Custom domain for branding (free via Freenom/Cloudflare).

## Credits

Built as a student project by Sathwik Nandimalla. Open-source prototype for learning and experimentation.
