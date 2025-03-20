import os
import google.generativeai as genai

from dotenv import load_dotenv
class Ask():
    def __init__(self, question,text):
        self.question = question
        self.text = text

    
        load_dotenv()

        genai.configure(api_key=os.getenv("API_KEY")) 
        
        generation_config = {
  "temperature": 0.5,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
        safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

        model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
  system_instruction=f"According to this topic '{self.text}' answer the questions.",
)


        self.chat_session = model.start_chat(
        history=[]
)
    def ask(self):
        response = self.chat_session.send_message(self.question)
        model_response = response.text
        self.chat_session.history.append({"role": "user", "parts": [self.question]})
        self.chat_session.history.append({"role": "model", "parts": [model_response]})
        return model_response

  