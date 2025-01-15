import gradio as gr

#MAIN
version = "4.0.2"
env = "dev"
aplicacion = "observa-dev"

seleccion_api = "eligeQuotaOCosto" #eligeQuotaOCosto , eligeAOB o eligeGratisOCosto
max_size = 20 #queue size

#Quota o Costo
api_cost = ("Moibe/comprension-imagenes", "quota")
api_zero = ("vikhyatk/moondream2", "gratis") #Éste es un caso raro pq después de acabarte la quota viene el gratis.
#A o B
api_a = ("Moibe/image-blend", "gratis")
api_b = ("Moibe/image-blend", "gratis")
#Gratis o Costo
api_gratis = ("Moibe/image-blend", "gratis")
api_costo = ("Moibe/image-blend", "costo")

interface_api_name = "/answer_question" #El endpoint al que llamará client.

process_cost = 0
seto = "observa"
work = "picswap"
app_path = "/observa-dev"
server_port=7830
#tema = tools.theme_selector()
tema = gr.themes.Default()
flag = "auto" #never, auto o manual.

#Future: Put age to cookies.

neural_wait = 3
mensajes_lang = "es"