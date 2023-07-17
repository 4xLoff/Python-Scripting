import requests

# Abre el archivo 'output.txt' en modo de lectura
with open('output.txt', 'r') as file:
    # Itera sobre cada línea del archivo
    for line in file:
        # Elimina los espacios en blanco al principio y al final de la línea
        line = line.strip()
        
        # Realiza una solicitud GET a una URL específica
        # La URL es la concatenación de 'http://192.168.100.45/shehatesme' y el contenido de la línea actual
        response = requests.get('http://192.168.100.45/shehatesme' + line)
        
        # Abre el archivo 'curl.txt' en modo de escritura (si no existe, lo crea)
        # y agrega la respuesta de la solicitud HTTP al archivo
        with open('curl.txt', 'a') as output_file:
            output_file.write(response.text)
