import gradio as gr
import globales
import tools

mensajes, sulkuMessages = tools.get_mensajes(globales.mensajes_lang)

# Diccionario para mapear los sets a sus respectivas configuraciones
configuraciones = {
    "image-blend": {
        "input1": gr.Image(label=mensajes.label_input1, type="filepath"),
        "input2": gr.Image(label=mensajes.label_input2, type="filepath"),
        "result": gr.Image(label=mensajes.label_resultado),
    },
    "observa": {
        "input1": gr.Image(label = mensajes.label_input1, type="filepath"),
        "input2": gr.Textbox(label= mensajes.label_input2, value=mensajes.value_input2, scale=4),
        "result": gr.Textbox(label= mensajes.label_resultado) 
    },
    "video-blend": {
        "input1": gr.Image(label=mensajes.label_input1, type="filepath"),
        "input2": gr.Video(),
        "result": gr.Video(label=mensajes.label_resultado) 
    },
    "sampler": {
        "input1": gr.Audio(label = mensajes.label_input1),
        "input2": gr.Audio(label= mensajes.label_input2),
        "result": gr.Audio(label=mensajes.label_resultado) 
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