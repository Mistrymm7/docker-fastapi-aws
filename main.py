from fastapi import FastAPI
import gradio as gr

app = FastAPI()

# Gradio
CUSTOM_PATH = "/gradio"
io = gr.Interface(lambda x: "Hello, " + x + "!", "textbox", "textbox")
app = gr.mount_gradio_app(app, io, path=CUSTOM_PATH)

#Welcome
@app.get("/")
async def root():
    return {"message": "Hello World Lets Go"}

#Additonal
@app.get("/{name}")
async def welcome(name: str):
    return {"Welcome": name}



