🌾 AgroSure AI – LLM-Powered Risk Assessment for Agricultural Insurance Claims

AgroSure AI is a Generative AI solution built to help insurers assess agricultural insurance claims quickly and intelligently. It uses Large Language Models (LLMs) to classify risk, detect potential fraud, and explain claim decisions in natural language — all integrated with Curacel's Grow API.


---

❓ Problem Statement

Agricultural insurance providers face growing challenges with:

🚨 High fraud rates due to unverifiable or inconsistent claim data

🐌 Slow manual claim reviews leading to delays in payouts

💬 Lack of transparency in how decisions are made or communicated to farmers

🌍 Underwriting challenges in regions with poor data access or irregular reporting


These issues hinder trust between farmers and insurers, reduce operational efficiency, and lead to financial losses.


---

💡 Solution Overview

AgroSure AI solves these challenges by introducing:

> ✅ A scalable, LLM-powered assistant that triages agricultural insurance claims, detects fraud risks, and explains claim decisions using natural language generation.



👇 Key Features

Feature	Description

🧠 AI Risk Scoring	Uses GPT-4 to evaluate claims and score their fraud risk
🗂 Claim Summarization	Transforms farmer input and attachments into structured insights
🔍 Context-Aware Detection	Combines weather, location, and metadata to catch red flags
📡 Curacel Integration	Pulls and updates claims from Curacel Grow API
🌍 Farmer-Friendly Feedback	Supports simple, explainable decisions in local languages



---

🧱 How It Works

🧠 AI Pipeline

1. Input: Claim details from Curacel or manual form (type, location, date, weather, description, etc.)


2. Prompt Construction: Build a context-rich prompt for GPT-4


3. LLM Inference: Send to OpenAI to generate a fraud score and reasoning


4. Output: JSON with { "score": 85, "reason": "No rain despite flood claim" }



🔗 API Integration

Read claim: GET /v1/claims/{claim_id}

Create claim: POST /v1/claims

Update status (optional): PUT /v1/claims/{id}/discharge-voucher



---

🧪 Demo Instructions (Colab)

Try the chatbot version in Google Colab:

1. Open Colab
2. Install dependencies:
   !pip install openai gradio
3. Replace your OpenAI API key
4. Run `chat_ui.launch()` to start chatting with the bot


---

⚙️ Technologies Used

🧠 OpenAI GPT-4o (LLM for reasoning and explanation)

🐍 Python 

🧪 Gradio (interactive chatbot interface in Colab)

🔌 Curacel Grow API (insurance backend integration)



---

📦 Future Enhancements

🖼️ Image analysis for crop damage verification

📱 Mobile app for field agents and farmers

🗣️ Multi-language support (Hausa, Pidgin)

📈 Model fine-tuning on local insurance data



---

🤝 Contributing

Contributions are welcome. You can:

Improve the AI prompts

Add support for image attachments

Expand integrations with other Curacel endpoints

---

