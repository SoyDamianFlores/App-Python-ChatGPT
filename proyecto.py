import openai

openai.api_key = "API-KEY" #API KEY


while True: # Add un ciclo While para que la interaccion se repita.


    prompt = input("\nIntroduce una pregunta: ") #Add una varible para hacer la pregunta por terminal.
    
    if prompt == "exit": # Condicion para  detener el programa.
        break

    completion = openai.Completion.create(engine="text-davinci-003", # Modelo entrenado que usaremos
                            prompt=prompt, #Realizamos la pregunta (Esta en la variable PROMPT)
                            n=1, #Numero de respuestas por defecto (1)
                            max_tokens=2048) # Longitud de respuesta

    print(completion.choices[0].text)
