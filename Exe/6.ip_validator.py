import sys
import re

# Receber um IP - Formato IPv4
# O Ip não pode iniciar com nenhum 0. E.g: 012.034.05.06
# O número máximo de cada intervalo é 255

# formato 192.168.82.22

def main():
    get_ip()    

def get_ip():
    ip_addr = sys.argv[1]
    treat_ip(ip_addr)

def treat_ip(IPv4):
    split_ip = re.split(r"\.", IPv4)
    count = 0
    for ip_peace in split_ip:
        ip_peace = int(ip_peace)
        if ip_peace > 1 or ip_peace.startswith("0"):
            continue
        elif ip_peace < 1:
            print("[ERRO] Nosso protocolo não aceita IPs começando em 0")
        else:
            if count == 0 or count == 1:
                if ip_peace > 255:
                    print("[ERRO: As 2 primeiras partes do ip devem estar entre 1 e 255]")
                else:
                    print("Primeira metade do IP válida")
            if count == 2 or count == 3:
                if ip_peace > 100:
                    print("[ERRO] as duas últimas partes do IP precisam estar entre 1 e 99") 
                else:
                    print("Segunda metade do ip válida") 
        count = count + 1
        print(IPv4)
        
if __name__ == "__main__":
    main()