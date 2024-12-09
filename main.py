import os
os.system("cls")


# Importando as bibliotecas necessarias
try:
    
    # Verificando se a biblioteca para a barra de progresso esta em condições
    try:
        from rich.progress import Progress
    except ImportError:
        print("\n033[1;31mExecute: pip install rich")
        
    with Progress() as progress:
        
        # Criando uma barra de progresso para as importações necessarias
        task = progress.add_task("   [blue]Importando Bibliotecas:", total=100)
            
            
        while not progress.finished:
            
            import mysql.connector
            progress.update(task, advance=1)
            
            import random
            progress.update(task, advance=1)
            
            import os
            progress.update(task, advance=1)
                
            import sys
            progress.update(task, advance=1)
                
            import time
            progress.update(task, advance=1)
                
            import pyfiglet
            progress.update(task, advance=1)
                
            import inquirer
            progress.update(task, advance=1)
                
            from colorama import Fore, Back, Style
            progress.update(task, advance=1)
            
            from tqdm import tqdm
            progress.update(task, advance=1)
                
            import random
            progress.update(task, advance=1)
                
            import getpass
            progress.update(task, advance=1)
            

# Caso alguma biblioteca não esteja instalada ou atualizada
except ImportError:
    print("\n\033[1;31mAlgumas bibliotecas estão em falta\n\033[0;32mExecute \033[1;34m'pip install -r requirements.txt'\033[0;32m para instalar/atualizar as bibliotecas necessarias\033[0;0m")



