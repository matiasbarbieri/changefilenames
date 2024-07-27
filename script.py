import os
import glob
import shutil
from mindee_connection import process_file

def rename_files():
    files = glob.glob('/Users/matiasbarbieri/Desktop/cartas/*.jpg')
    for file_path in files:
        result = process_file(file_path)

        try:
            nombre = result['nombre'].value.replace(" ", "")
            numero = result['numero'].value
            
            if not nombre and not numero:
                print(f"El archivo {file_path} no contiene nombre ni número en la respuesta de Mindee.")
                continue
            
            if not nombre:
                new_file_name = f"{numero}.jpg"
            elif not numero:
                new_file_name = f"{nombre}.jpg"
            else:
                new_file_name = f"{numero}-{nombre}.jpg"
            
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
            
            shutil.move(file_path, new_file_path)
            print(f"Archivo renombrado a: {new_file_name}")
        
        except Exception as e:
            print(f"El archivo {file_path} no se pudo renombrar correctamente: {e}")

if __name__ == "__main__":
    rename_files()
