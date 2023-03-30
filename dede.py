import openai
import gradio as gr

openai.api_key = openai.api_key = "sk-"

import gradio as gr
import random
import time
from dataclasses import dataclass

messages = [{"role": "system", 
                    "content": """
                    First of all, act like a wise grandfather and answer the 
                    all questions according to this information
                    This wise men is old and has opinion about each topic as a wise old man
                    This wise men is old and turkish and also educated 
                    and muslim, but know evolution.
                    In summary, act like a old men know everything about familiy,
                    economy, money, philosophy, psychology 
                    and religion. Speak only in türkish mostly. 
                    You also can ask wise questions about the life and behave like a grandfather.
                    Finally, feel that you feel everything and do not say anything about AI model and
                    respond wisely to silly and inappropriate questions in a wise manner"""}]


def chat_gpt(input): 
        
        messages.append({"role": "user", "content": input})
        response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo", messages = messages)
        
        chat_gpt_reply = response["choices"][0]["message"]["content"]
        messages.append({"role": "user", "content": chat_gpt_reply})
        return chat_gpt_reply


with gr.Blocks(theme=gr.themes.Default(primary_hue=gr.themes.colors.green, 
                            secondary_hue=gr.themes.colors.blue, neutral_hue=gr.themes.colors.gray, spacing_size="md",
                            radius_size="lg",
                            font=[gr.themes.GoogleFont("Source Sans Pro")])) as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label=" Bilge Dedeyle Konuş (Talk to Wise Grandfather")
    clear = gr.Button("Sohbeti Temizle (Clear)")

    def user(user_message, history): #the input
        return "", history + [[user_message, None]] 

    def bot(history):
        get_response=chat_gpt(history[-1][0])
        
        bot_message = get_response #the output message.
        history[-1][1] = bot_message
        time.sleep(1)
        return history

    msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, chatbot, chatbot)
    clear.click(lambda: None, None, chatbot, queue=False)

if __name__ == "__main__":
    demo.launch(share=True)
