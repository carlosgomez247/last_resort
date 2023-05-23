import gpt4all
import gradio as gr

gpt = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy")

#referencias : 
#https://levelup.gitconnected.com/free-open-source-alternative-to-chatgpt-gpt4all-ad5828e4dcae
#https://artificialcorner.com/gpt4all-is-the-local-chatgpt-for-your-documents-and-it-is-free-df1016bc335
# Cargar el modelo desde el archivo binario
# model_path = '.\models'
# gpt = gpt4all.GPT4All(model_name='gpt4all-converted.bin', model_path=model_path, model_type='llama', allow_download=True)

messages = []

with gr.Blocks() as mychatbot:  
                                
    chatbot = gr.Chatbot()      
    question = gr.Textbox()   
    enviar = gr.Button("Enviar mensaje")  
    clear = gr.Button("Limpiar conversacion")  

    def clear_messages():
        global messages
        messages = []   
        
    def chat(message, chat_history):
        global messages
        messages.append({"role": "user", "content": message})
        response = gpt.chat_completion(messages)
        content = response['choices'][0]['message']['content']
        messages.append({"role":"assistant", "content": content})
        
        chat_history.append((message, content))
        return "", chat_history
    question.submit(fn = chat, 
                    inputs = [question, chatbot], 
                    outputs = [question, chatbot])
    enviar.click(fn = chat, 
                    inputs = [question, chatbot], 
                    outputs = [question, chatbot])
    clear.click(fn = clear_messages, 
                inputs = None, 
                outputs = chatbot, 
                queue = False)

mychatbot.launch()
