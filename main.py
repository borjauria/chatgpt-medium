import openai
import functions

# Load config parameters from a config file
config = functions.read_config()

api_key = str(config['open_ai']['api_key'])
lang = str(config['languages']['git'])

# API key from Open AI
openai.api_key = api_key

# Context of assistant
language = lang.split('/')[-1].split('_')[-1].split('.')[0]

with open(lang) as file:
    content = file.read()

messages_to = [{"role": 'system', "content": f'{content}'}]

while True:
    question = input(f"Ask to chatGPT about {language}, please: ")
    
    if question == 'quit':
        break
    
    messages_to.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages_to)
    print(response.choices[0].message.content)