import requests
import json
import gradio as gr

URL = "http://localhost:11434/api/generate"
HEADERS = {'Content-Type': 'application/json'}
HISTORY = []

def generate_response(prompt):
    global HISTORY
    HISTORY.append(prompt)
    final_prompt = "\n".join(HISTORY)
    data = {
        "model": "procoder",
        "prompt": final_prompt,
        "stream": False
    }
    response = requests.post(URL, headers=HEADERS, data=json.dumps(data))

    if response.status_code == 200:
        response_data = json.loads(response.text)
        return response_data.get('response')
    else:
        print("Error:", response.text)

interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your Prompt"),
    outputs="text"
)
interface.launch()
