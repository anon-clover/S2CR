import openai
import time
import asyncio
import aiohttp
import tqdm
import json
from config import *

class Reader:
    def __init__(self,temperature:float=0.8, max_tokens:int=2048):
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.model=OPENAI_API_MODEL
        openai.base_url=OPENAI_API_BASE_URL
        openai.api_key=OPENAI_API_KEY


    def generate_response(self, prompt:str):
        # 调用OpenAI API生成响应
        response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        # 提取生成的文本
        generated_text = response.choices[0].message.content
        return generated_text


class aReader:
    def __init__(self,temperature:float=0.8, max_tokens:int=2048, time_window:float=1.0, rate_limit:int=3):
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.model=OPENAI_API_MODEL
        openai.base_url=OPENAI_API_BASE_URL
        openai.api_key=OPENAI_API_KEY

        self.time_window=time_window
        self.rate_limit=rate_limit
        self.request_times=[]
        
        
    def generate_response(self, prompt:str):
        # 调用OpenAI API生成响应
        response = openai.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        # 提取生成的文本
        generated_text = response.choices[0].message.content
        return generated_text
        
    
    
    def generate_list_responses(self, prompts:list, progress_bar=False):
        if progress_bar:
            return [self.generate_response(prompt) for prompt in tqdm.tqdm(prompts)]
        else:
            return [self.generate_response(prompt) for prompt in prompts]
