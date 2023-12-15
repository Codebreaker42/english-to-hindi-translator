from flask import Flask,request,jsonify
import json
import os
import sys
import transformers
import tensorflow as tf
from datasets import load_dataset
from transformers import AutoTokenizer
from transformers import TFAutoModelForSeq2SeqLM, DataCollatorForSeq2Seq
from transformers import AdamWeightDecay
from transformers import AutoTokenizer, TFAutoModelForSeq2SeqLM

# model
model_checkpoint="Helsinki-NLP/opus-mt-en-hi"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = TFAutoModelForSeq2SeqLM.from_pretrained("tf_model/")
def english_to_hindi(input_text):
    tokenized=tokenizer([input_text],return_tensors='np')
    out=model.generate(**tokenized,max_length=128)
    print(out)
    with tokenizer.as_target_tokenizer():
        return(tokenizer.decode(out[0],skip_special_tokens=True))
    
# flask app
app=Flask(__name__)
@app.route('/')
def home():
    return "Welcome to our API"
  
@app.route('/response/',methods=['GET'])
def response():
    input_text=str(request.args.get('document'))
    translated=english_to_hindi(input_text)
    ans={'translation':translated}
    return json.dumps(ans)

if __name__=='__main__':
    app.run(debug=True)
    