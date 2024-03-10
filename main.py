import ply.lex as lex
import tkinter as tk
import re
import json
from tkinter import scrolledtext, filedialog, messagebox
from AnalizadorJulia import AnalizadorJulia
from analizadorRuby import analizadorRuby
from metodos import Metodos

#from rubyAnalyzer import RubyAnalyzer
#from semanthicAnalyzer import Analyzer

class CodeInputApp:
        
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Código")
        self.root.geometry("730x430")

        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="Abrir Julia", command=self.open_file_julia)
        self.file_menu.add_command(label="Abrir Ruby", command=self.open_file_ruby)
        self.file_menu.add_command(label="Guardar Como", command=self.save_as)

        self.code_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20, fg="#CDCCCD")
                
        self.code_input.configure(bg="#111")       
                
        self.code_input.grid(row=0, column=0, padx=10, pady=10)
        self.code_input.bind("<KeyRelease>", self.update_button_and_count)

        self.run_button = tk.Button(root, text="Ejecutar Código", command=self.execute_code, state=tk.DISABLED)
        self.run_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W + tk.E)

        self.console_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=20, fg="#CDCCCD")
        self.console_output.grid(row=0, column=1, padx=10, pady=10)
        self.console_output.config(state=tk.DISABLED)
        
        self.console_output.configure(bg="#1A1A1A")

        self.character_count_label = tk.Label(root, text="Número de caracteres: 0")
        self.character_count_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        #self.update_button_and_count()
    
    def update_button_and_count(self, event=None):
        code = self.code_input.get("1.0", tk.END)
        character_count = len(code) - 1  
        self.character_count_label.config(text=f"Número de caracteres: {character_count}")

        if 1 <= character_count <= 500:
            self.run_button.config(state=tk.NORMAL)
        else:
            self.run_button.config(state=tk.DISABLED)
            
    # Función para cargar el diccionario desde el archivo JSON
    def cargar_array(self):
        try:
            with open('arrays.json', 'r') as json_file:
              arrays = json.load(json_file)
            return arrays
        except FileNotFoundError:
            print("El archivo JSON no existe.")
            return {}
    
    # Función para guardar un array en el diccionario y en el archivo JSON
    def guardar_array(self, nombre_variable, array):
        arrays = self.cargar_array()
        if nombre_variable in arrays:
            print(f"Ya existe un array con el nombre de variable '{nombre_variable}'.")
        else:
            arrays[nombre_variable] = array
            with open('arrays.json', 'w') as json_file:
                json.dump(arrays, json_file)
            print(f"El array para la variable '{nombre_variable}' se ha guardado correctamente.")
            
    # Función para extraer un array por nombre de variable
    def extraer_array_por_nombre(self, nombre_variable):
        arrays = self.cargar_array()
        if nombre_variable in arrays:
            return arrays[nombre_variable]
        else:
            print(f"No se encontró el array para la variable {nombre_variable}")
            return None
    
    def match(self, ultima_linea):
        nombre_variable_match = re.match(r'^mean\((\w+)\)$', ultima_linea)
        if nombre_variable_match:
            nombre_variable = nombre_variable_match.group(1)
            array_extraido = self.extraer_array_por_nombre(nombre_variable)
            return array_extraido
        else:
            self.console_output.insert(tk.END, "No se encontró el nombre de la variable para calcular la media")

    def execute_code(self):
        code = self.code_input.get("1.0", tk.END)
        
        lineas = code.splitlines()
        
        for linea in reversed(lineas):
            if linea.strip():
                ultima_linea = linea
                break
        print(ultima_linea)            
        
        character_count = len(code) - 1 
        self.console_output.config(state=tk.NORMAL)
        self.console_output.delete("1.0", tk.END)
        
        if self.identify_language(ultima_linea) == "julia":
            julia_analyzer = AnalizadorJulia()
            analyzed_tokens = julia_analyzer.analyze_code(code)
            result = f"Tokens reconocidos:\n{analyzed_tokens}"
            numbers = []
            self.console_output.insert(tk.END, result)
            #self.console_output.config(state=tk.DISABLED)

            for cont in analyzed_tokens:
                try:
                    number = int(cont[1])  
                    numbers.append(number)  
                except ValueError:
                    pass  
            
            
            metodos = Metodos()
            arrays = {}
            
            if "rand" in ultima_linea:
                number = numbers[0]
                array = metodos.crearArray(number)
                nombre_variable = re.match(r'^\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=', ultima_linea)
                if nombre_variable:
                    nombre_variable = nombre_variable.group(1)
                    print("Nombre de la variable:", nombre_variable)
                    self.guardar_array(nombre_variable, array)
                    for nombre_variable, array in arrays.items():
                        print(f"Nombre de la variable: {nombre_variable}, Array: {array}")
                    arreglo = f'\n{array}\n'
                    self.console_output.insert(tk.END, arreglo)                   
                else:
                    print("No se encontró el nombre de la variable")
            elif "mean" in ultima_linea:
                array_extraido = self.match(ultima_linea)
                if array_extraido is not None:
                    media = metodos.media(array_extraido)
                    mean = f'\nMedia: \n{media}'
                    self.console_output.insert(tk.END, mean)
                else:
                    print("No se pudo extraer el array.")
            elif "mode" in ultima_linea:
                moda = metodos.calcular_moda(array)
                mode = f'\nModa: \n{moda}'
                self.console_output.insert(tk.END, mode)
            elif "var" in ultima_linea:
                varianza = metodos.calcular_varianza(array)
                variance = f'\nVarianza: \n{varianza}'
                self.console_output.insert(tk.END, variance)
            elif "std" in ultima_linea:
                desviacion = metodos.calcular_desviacion_estandar(array)
                desv = f'\nDesviacion Estandar: \n{desviacion}'
                self.console_output.insert(tk.END, desv)
            elif "median" in ultima_linea:
                mediana = metodos.calcular_mediana(array)
                med = f'\nMediana: \n{mediana}'
                self.console_output.insert(tk.END, med)
            else:
                self.console_output.insert(tk.END, "Método no reconocido")
                
        elif self.identify_language(ultima_linea) == "ruby":
            ruby_analyzer = analizadorRuby()
            analyzed_tokens = ruby_analyzer.analyze_code(ultima_linea)
            result = f"Tokens reconocidos:\n{analyzed_tokens}"
            numbers = []
            self.console_output.insert(tk.END, result)
            #self.console_output.config(state=tk.DISABLED)

            for cont in analyzed_tokens:
                try:
                    number = int(cont[1])  
                    numbers.append(number)  
                except ValueError:
                    pass  
            
            number = numbers[0]
            metodos = Metodos()

            if "rand" in ultima_linea:
                array = metodos.crearArray(number)
                arreglo = f'\n{array}\n'
                self.console_output.insert(tk.END, arreglo)
            elif "mean" in ultima_linea:
                media = metodos.media(array)
                mean = f'\nMedia: \n{media}'
                self.console_output.insert(tk.END, mean)
            elif "mode" in ultima_linea:
                moda = metodos.calcular_moda(array)
                mode = f'\nModa: \n{moda}'
                self.console_output.insert(tk.END, mode)
            elif "var" in ultima_linea:
                varianza = metodos.calcular_varianza(array)
                variance = f'\nVarianza: \n{varianza}'
                self.console_output.insert(tk.END, variance)
            elif "std" in ultima_linea:
                desviacion = metodos.calcular_desviacion_estandar(array)
                desv = f'\nDesviacion Estandar: \n{desviacion}'
                self.console_output.insert(tk.END, desv)
            elif "median" in ultima_linea:
                mediana = metodos.calcular_mediana(array)
                med = f'\nMediana: \n{mediana}'
                self.console_output.insert(tk.END, med)
            else:
                self.console_output.insert(tk.END, "Método no reconocido")
        else:
            print(self.identify_language(ultima_linea))

        
        self.console_output.config(state=tk.DISABLED)
        self.update_button_and_count()

    def identify_language(self, code):
        
        expresionJulia = r'[a-zA-Z]+\s*=\s*[a-z]+\(\d+\)$|\b([a-z]+)\(([a-zA-Z]+)\)$'
        expresionRuby = r'[a-zA-Z]+\s*=\s*[a-zA-Z]+\.[a-z]+$|[a-zA-Z]+\s*=\s*Array\.new\(\d+\)\s*\{\s*rand\s*\}$'

        if re.match(expresionJulia, code):
            return "julia"
        elif re.match(expresionRuby, code):
            return "ruby"
        else:
            return "Lenguaje no encontrado"

    def open_file_julia(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos Julia", "*.jl")])
        if file_path:
            with open(file_path, "r") as file:
                code = file.read()
                self.code_input.delete("1.0", tk.END)
                self.code_input.insert(tk.END, code)
                self.update_button_and_count()

    def open_file_ruby(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos Ruby", "*.rb")])
        if file_path:
            with open(file_path, "r") as file:
                code = file.read()
                self.code_input.delete("1.0", tk.END)
                self.code_input.insert(tk.END, code)
                # Después de abrir el archivo, actualiza el conteo de caracteres y el estado del botón
                self.update_button_and_count()

    def save_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de Texto", "*.txt"),
                                                                                      ("Archivos Julia", "*.jl"),
                                                                                      ("Archivos Ruby", "*.rb")])
        if file_path:
            with open(file_path, "w") as file:
                code = self.code_input.get("1.0", tk.END)
                file.write(code)

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeInputApp(root)
    root.mainloop()