import json
import gpt4all
 
gptj = gpt4all.GPT4All("ggml-gpt4all-j-v1.3-groovy")
messages = [{"role": "user", "content": "En que año empezo la primera guerra mundial?"}]
ret = gptj.chat_completion(messages)
print(json.dumps(ret, indent=4))