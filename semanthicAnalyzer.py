from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class Analyzer:
    def semanticAnalyzer (self, code):
        self.code = code
        try:
            # Crear la instancia del cliente OpenAI con la clave de la API
            client = OpenAI(api_key=api_key)
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                                "content": f"Analiza cual  lenguaje de programacion es (Julia o Ruby)  y encuentre errores que signifiquen una incorrecta compilación del codigo, si no, no los muestres y compila: {code}. En la respuesta no muestres el nombre del lenguaje. Los errores muestralos como los mostraria un compilador. si es correcto el codigo muestra la ejecucion de la siguiente forma: Ejecución:(Aqui va el resultado del codigo), si no, muestra: (aqui el error de compilacion)",
                    }
                ]
            )
            completion1 = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                                "content": f"Hola",
                    }
                ]
            )
            response = completion.choices[0].message.content
            response1 = completion1.choices[0].message.content
            print(response1)
            return response

        except OpenAIError as e:
            print(f"Error al inicializar la instancia de OpenAI: {e}")