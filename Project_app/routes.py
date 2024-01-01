from flask import Flask, render_template, url_for, request
from Project_app import app
import os
import openai

openai.api_key = "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"

INSTRUCTIONS = ["1. summarize the sentences", "2. give me core word"]
system_instruction = "\n".join(["""You will be provided with many sentences, and your task is to summarize these sentences as follows.
                                또한, 입력 문장이 한국어라면, 한국어로 요약내용과 핵심 단어를 도출해내라.""", *INSTRUCTIONS])

@app.route("/")
@app.route("/index")
def index_func():
    return render_template("index.html", title="Home")

@app.route("/somepage", methods = ["GET", "POST"])
def some_func():
    msg = request.form
    response = openai.ChatCompletion.create(
        model="gpt-4", #모델 지정
        messages = [{"role":"system", "content": f"{system_instruction}"},
        {"role": "user", "content": f"{msg}"}],
        temperature=0,
        )
    if request.method == "POST":
        if msg["button"] == "summarize":
            return render_template("somepage.html", title = "SomePage", result = response.choices[0].message.content, original_msg = msg['massage'])
    return render_template("somepage.html", title = "SomePage")
