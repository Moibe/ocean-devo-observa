import gradio as gr
import globales

if globales.mensajes == "en":
    import sulkuMessages
else:
    import sulkuMessages_es as sulkuMessages

# Diccionario para mapear los sets a sus respectivas configuraciones
configuraciones = {
    "image-blend": {
        "input1": gr.Image(label="Source", type="filepath"),
        "input2": gr.Image(label="Destination", type="filepath"),
        "result": gr.Image(label="Result"),
    },
    "observa": {
        "input1": gr.Image(label = sulkuMessages.label_input1, type="filepath"),
        "input2": gr.Textbox(label= sulkuMessages.label_input2, value="Describe this image.", scale=4),
        "result": gr.Textbox(label= sulkuMessages.label_resultado) 
    },
    "video-blend": {
        "input1": gr.Image(label="Source", type="filepath"),
        "input2": gr.Video(),
        "result": gr.Video(label="Result") 
    },
    "sampler": {
        "input1": gr.Audio(),
        "input2": gr.Audio(),
        "result": gr.Audio(label="Result") 
    },
    "splashmix": {
        "input1": gr.Image(label="Source", type="filepath"),
        "result": gr.Image(label="Destination", type="filepath"),
    },
    "txt2image": {
        "input1": gr.Textbox(),
        "result": gr.Image(label="Source", type="filepath"),
    },
    "txt2video": {
        "input1": gr.Textbox(),
        "result": gr.Video(),
    },
    "zhi": {
        "input1": gr.Image(label="Source", type="filepath"),
        "input2": gr.Textbox(label="Prompt"),
        "result": gr.Image(label="Result"),
    },
}