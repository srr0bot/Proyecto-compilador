import ply.lex as lex
import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
from AnalizadorJulia import AnalizadorJulia
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
        character_count = len(code) - 1  # Restar 1 para excluir el último carácter que es una nueva línea
        self.character_count_label.config(text=f"Número de caracteres: {character_count}")

        if 1 <= character_count <= 500:
            self.run_button.config(state=tk.NORMAL)
        else:
            self.run_button.config(state=tk.DISABLED)

    def execute_code(self):
        code = self.code_input.get("1.0", tk.END)
        print(code)
            
        
        character_count = len(code) - 1  # Restar 1 para excluir el último carácter que es una nueva línea
        self.console_output.config(state=tk.NORMAL)
        self.console_output.delete("1.0", tk.END)
        
        if self.identify_language == "julia":
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
            
            number = numbers[0]
            metodos = Metodos()

            if "rand" in code:
                array = metodos.crearArray(number)
                arreglo = f'\n{array}\n'
                self.console_output.insert(tk.END, arreglo)
            elif "mean" in code:
                media = metodos.media(array)
                mean = f'\nMedia: \n{media}'
                print(mean)
                self.console_output.insert(tk.END, mean)
            elif "mode" in code:
                moda = metodos.calcular_moda(array)
                mode = f'\nModa: \n{moda}'
                self.console_output.insert(tk.END, mode)
            elif "var" in code:
                varianza = metodos.calcular_varianza(array)
                variance = f'\nVarianza: \n{varianza}'
                self.console_output.insert(tk.END, variance)
            elif "std" in code:
                desviacion = metodos.calcular_desviacion_estandar(array)
                desv = f'\nDesviacion Estandar: \n{desviacion}'
                self.console_output.insert(tk.END, desv)
            elif "median" in code:
                mediana = metodos.calcular_mediana(array)
                med = f'\nMediana: \n{mediana}'
                self.console_output.insert(tk.END, med)
            else:
                self.console_output.insert(tk.END, "Método no reconocido")
        else:
            print("ruby")
        
        self.console_output.config(state=tk.DISABLED)

            # Después de analizar el código, actualiza el conteo de caracteres
        self.update_button_and_count()

    def identify_language(code):
        julia_keywords = ["rand", "mean", "mode", "var", "std", "median"]
        ruby_keywords = ["def", "end", "if", "else", "elsif", "puts", "print", "while", "for"]

        julia_matches = sum(keyword in code for keyword in julia_keywords)
        ruby_matches = sum(keyword in code for keyword in ruby_keywords)

        if julia_matches > ruby_matches:
            return "julia"
        elif ruby_matches > julia_matches:
            return "ruby"
        else:
            return "unknown"

    def open_file_julia(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos Julia", "*.jl")])
        if file_path:
            with open(file_path, "r") as file:
                code = file.read()
                self.code_input.delete("1.0", tk.END)
                self.code_input.insert(tk.END, code)
                # Después de abrir el archivo, actualiza el conteo de caracteres y el estado del botón
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