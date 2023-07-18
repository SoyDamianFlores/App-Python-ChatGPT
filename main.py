import openai
import config
import typer
from rich import print
from rich.table import Table



# Creamos una funcion Main para llamarla luego con la libreria Typer
def main():
    
    openai.api_key = config.api_key # Importo la api desde el archivo congig
    
    print("📢 [bold green]ChatGPT API con Python[/bold green]") #Comenzamos a usar las herramientas que ofrece print (Bold).

    table = Table("Comando", "Descripción") #Cabezera de la tabla con Rich :D
    table.add_row("exit", "Salir de la aplicación") #Add una fila a la tabla.
    table.add_row("new", "Crear una nueva conversación")

    print(table) #Mostramos la tabla en la terminal.

    #Contexto del asistente
    context = {"role":"system", #Cambiamos su rol
                "content": "Eres un asistente muy útil."} # condisionamos su rol para tener respuesta mas precisas.
    messages = [context]

    while True:
        content = __prompt()

        if content == "new":
            print("🆕 Nueva conversación creada")
            messages = [context]
            content = __prompt()

        messages.append({"role":"user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages) #Estructura del mensaje


        response_content = response.choices[0].message.content #Variable que almacena las respuestas.
        
        messages.append({"role":"assistant", "content": response_content}) #Add un rol asistente y guardamos los mensajes para que tenga historial de la conversacion


        print(f"[bold green]> [/bold green][green]{response_content}[/green]")

#Funcion con Typer para controlar la conversacion (New y Exit)
def __prompt():
    prompt = typer.prompt("\n¿Sobre qué quieres hablar? ")

    if prompt == "exit":
        exit = typer.confirm("🤚 ¿Estas seguro?")
        if exit:
            print("👋¡Hasta Luego!")
            raise typer.Abort()
        
        return __prompt()

    return prompt

# Forma para correr el programa con la libreria Typer
if __name__ == "__main__":
    typer.run(main)