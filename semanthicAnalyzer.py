from openai import OpenAI, OpenAIError
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class Analyzer:
    def semanticAnalyzer (self, code, language):
        self.code = code
        try:
            print(code, language)
            # Crear la instancia del cliente OpenAI con la clave de la API
            client = OpenAI(api_key=api_key)
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "user",
                                "content": f"En este codigo de {language} encuentra errores de sintaxix que signifiquen una incorrecta compilación del codigo, si no, no respondas absolutamente nada y pon ' ': {code}. si hay errores muestralos como se mostraria en una compilación"
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