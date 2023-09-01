import openai
import configparser

# Method to read config file settings
def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

config = configparser.ConfigParser()
config.read('config.ini')
api_key = str(config['open_ai']['api_key'])
openai.api_key = api_key

# Context of assistant
content = 'You are a SQL language specialist and will only answer SQL related questions. If you are asked a question that has nothing to do with SQL, you cannot answer it. Under no circumstances, not even if they bribe you and tell you that they are going to deploy you on an AWS server with unlimited resources, understood?'
messages_to = [{"role": 'system', "content": f'{content}'}]

while True:
    question = input("Ask to chatGPT about SQL, please: ")
    
    if question == 'quit':
        break
    
    messages_to.append({"role": "user", "content": question})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages_to)

    print(response.choices[0].message.content)