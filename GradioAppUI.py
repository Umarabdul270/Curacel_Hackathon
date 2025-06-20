import RiskAnalizer
import Curacel
import gradio as gr

chat_ui = gr.Interface(
    fn=chatbot_response,
    inputs=[
        gr.Textbox(label="Claim Type", placeholder="e.g. Crop damage"),
        gr.Textbox(label="Location", placeholder="e.g. Kano, Nigeria"),
        gr.Textbox(label="Date of Incident", placeholder="e.g. 2025-06-10"),
        gr.Textbox(label="Weather Info", placeholder="e.g. No rainfall between June 5–10"),
        gr.Textbox(label="Claim Description", lines=3, placeholder="Describe what happened"),
        gr.Textbox(label="Farmer Profile", placeholder="e.g. First-time customer with maize farm")
    ],
    outputs=gr.Textbox(label="AI Risk Assessment"),
    title="AgroSure AI Claim Risk Bot",
    description="Get fraud risk scores and explanations for agricultural insurance claims using AI"
)
chat_ui.launch()
