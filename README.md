# Code Generation with Ollama and Codelamma

This repository demonstrates how to use Ollama for running an open-source model locally and Codelamma for generating code in multiple languages based on user prompts.

## Prerequisites 

- Ollama should be installed on your local machine
- Codellama model should be downloaded 

## Requirements

- Python 3.11 
- Requests library (`pip install requests`)
- Gradio library (`pip install gradio`)

## Setup

1. Clone this repository:

   ```bash
   git clone <repository-url>
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the `app.py` script:

   ```bash
   python main.py
   ```

2. Once the application is launched, a Gradio interface will appear in your browser.

3. Enter your prompt in the textbox provided.

4. The model will generate code based on your prompt and display it as output.

## About the Code

- `app.py`: This script contains the code to interact with the Ollama and Codelamma models. It utilizes the `requests` library to communicate with the Ollama model running locally and the `gradio` library to create a user interface for generating code.

- `requirements.txt`: This file lists all the dependencies required by the project. You can install them using `pip`.

## Additional Notes
 - This example uses the "procoder" model name within the script. Ensure this matches the model name configured in Ollama.
The HISTORY list is currently not used to build context but can be incorporated for more advanced generation based on previous prompts.

 - For more information like how to add/edit modelfile, create model in ollama and run the model, please refer to ollama documentation 

## Contributors

- [Lokesh Darne](https://github.com/lokeshdarne)
