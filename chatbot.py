from openai import OpenAI
import sys

client = OpenAI(base_url="http://192.168.56.1:8000/v1", api_key="lm-studio")
history = [
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
]

while True:
    print('Enter your message (Press enter twice to send):')
    
    lines = []
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if line == '':
            break
        lines.append(line)
        
    user_message = " ".join(lines)
    
    if user_message != '':
        history.append({"role": "user", "content": user_message})
        
        completion = client.chat.completions.create(
            model="TheBloke/Mistral-7B-Instruct-v0.2-GGUF/mistral-7b-instruct-v0.2.Q4_K_S.gguf",
            messages=history,
            temperature=0.7,
            stream=True,
        )
        
        new_message = {"role": "assistant", "content": ""} 
        for chunk in completion:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="")
                new_message["content"] += chunk.choices[0].delta.content
                
        history.append(new_message)
