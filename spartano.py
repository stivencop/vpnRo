#!/usr/bin/python
import base64

BRANCO='\033[1;29m'
NADA='\033[0m'
CINZA='\033[02;37m'
DESTACAR='\033[01;37m'
RED='\033[1;31m'
AZUL='\033[36m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
AMARELO='\033[33m'
SCOLOR='\033[0m'
SEMCOR='\033[8m'
BrancoAll='\033[03;37;47m'
LETRAPRETA='\033[02;30;47m'
PURPULA='\033[35m'

OLAMAE =f"ㅤﾠㅤ⣿⣿⣿⣿⣿⠁⢰⠂⠐⠋⠊⠄⠂⢰⣆⠄⠂⠤⠄⡨⡀⠄⠄⠄⠄⠄⠠⠠\nﾠㅤㅤ⣿⣿⣿⣿⣿⠇⠄⠈⠄⠄⠄⠄⠄⠄⢸⣿⠄⠄⠄⠄⠄⠁⠄⠄⠄⠄⠄⠠\nㅤㅤﾠ⣿⣿⣿⣿⡟⠄⠄⠄⠄⡀⡄⠠⢀⣤⣿⣿⠄⠄⠄⠄⠄⢐⠄⠄⠄⠄⠄⠠\nㅤㅤﾠ⣿⣿⣿⣿⠁⠄⠸⠄⠄⢿⣷⣬⣿⣿⣿⣿⣀⣹⡤⡀⠄⢰⠄⠄⠄⠄⠄⠠\nㅤㅤﾠ⣿⣿⣿⠇⠄⠄⠄⠄⠄⠘⣿⣿⣿⡿⢼⣿⣿⣿⠁⠄⠄⢸⠄⠄⠄⠄⠄⠠\nㅤㅤﾠ⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠈⠻⣿⣆⣾⡿⠛⠁⠄⠄⠄⠄⡄⠄⠄⠄⠄⠠\nㅤㅤﾠ⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠛⠁⠄⠄⠄⠄⠄⠄⠄⢃⠄⠄⠄⠄⠄ \nㅤㅤﾠ⡟⠄⣀⣤⣤⣄⠄⣠⣀⣀⣀⣀⠄⠄⠄⠄⠄⠄⡀⠄⣀⣀⣘⠄⠄⠄⠄⠄ \nㅤㅤﾠ⠄⣾⣿⣿⣿⡟⢰⣿⣿⣿⣿⣷⣷⣶⣿⣾⣿⣿⡇⢻⣿⣿⣿⣿⡄⠄⠄⠄ \nㅤㅤﾠ⠄⣿⣿⣿⡏⠃⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣌⢟⡯⡟⣿⣷⠄⠄⠄ \nㅤㅤﾠ⠄⢹⣿⣿⢁⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣜⠿⠂⠄⠄ \nㅤㅤﾠ⠄⠄⢿⠇⣼⣿⣿⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⡷⡀⠄⠄ \nㅤㅤﾠ⠄⠄⠘⢐⣿⣿⠄⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⢰⠘⡀ \nㅤㅤﾠ⠄⠄⠄⢸⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⢻⣟⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⠄⠄ \nㅤㅤﾠ⠄⠄⠄⠄⠻⣿⣿⣿⣿⣿⣿⣿⡿⣻⣿⣟⣾⠿⣿⣿⣿⣿⣿⣿⡿⠃⠠⠄ \nㅤㅤﾠ⢀⢐⡀⣤⣤⣬⣝⣛⣻⣟⣿⢭⣿⣿⡿⣿⣿⣿⣮⣼⣟⠻⣿⡝⠄⠄⠄⠠"
def linha():
    print('🐝'*26)


def ssl():
    ssl = nm+"!!!!"+tp+"!!!!GET / HTTP/1.1[crlf]Host: "+dm+"[crlf]Upgrade: ws[crlf][crlf]!!!!"+pxy+"!!!!"+dnP+"!!!!"+dnS+"!!!!!!!!"+pt+"!!!!0!!!!0!!!!"+tg+"!!!!1!!!!1!!!!!!!!!!!!"+si+"!!!!127.0.0.1:"+udp+"(((((("
    return(ssl)


def web():
    web = nm+"!!!!"+tp+"!!!!GET / HTTP/1.1[crlf]Host:"+dm+"[crlf]Upgrade: ws[crlf][crlf]!!!!"+pxy+"!!!!"+dnP+"!!!!"+dnS+"!!!!!!!!"+pt+"!!!!0!!!!0!!!!"+tg+"!!!!1!!!!1!!!!!!!!!!!!"+si+"!!!!127.0.0.1:"+udp+"(((((("
    return(web)


def pay():
    pay = nm+"!!!!"+tp+"!!!!GET wss//"+si+" HTTP/1.1[crlf]Host: "+dm+"[crlf]Upgrade: ws[crlf][crlf]!!!!"+pxy+"!!!!"+dnP+"!!!!"+dnS+"!!!!!!!!"+pt+"!!!!0!!!!0!!!!"+tg+"!!!!1!!!!1!!!!!!!!!!!!"+si+"!!!!127.0.0.1:"+udp+"(((((("
    return(pay)


def custom():
    custom =  nm+"!!!!"+tp+"!!!!"+csm+"!!!!"+pxy+"!!!!"+dnP+"!!!!"+dnS+"!!!!!!!!"+pt+"!!!!0!!!!0!!!!"+tg+"!!!!1!!!!1!!!!!!!!!!!!"+si+"!!!!127.0.0.1:"+udp+"(((((("
    return(custom)
    
print(f"{OLAMAE}")
while True:
    csm = str(input(f"{GREEN}Coloque Su Payload Personalizado:{YELLOW} "))
    nm = str(input(f"{GREEN}Coloque El Nombre De Su Operadora:{YELLOW} "))
    linha()
    dm = str(input(f"{GREEN}Coloque Su Dominio:{YELLOW} "))
    linha()
    si = str(input(f"{GREEN}Coloque un SNI / Bughost:{YELLOW} "))
    linha()
    udp = str(input(f"{GREEN}Digite un puerto UDP, juegos, streaming:{YELLOW} "))
    linha()
    pt = str(input(f"{GREEN}Digite Un Puerto Proxy{YELLOW}: "))
    linha()
    pxy = str(input(f"{GREEN}Coleque El Proxy:{YELLOW} "))
    linha()
    dnP = str(input(f"{GREEN}Digite un DNS Primário válido:{YELLOW} "))
    linha()
    dnS = str(input(f"{GREEN}Digite un DNS Secundário válido:{YELLOW} "))
    linha()
    tp = str(input(f"{GREEN}Dê un nombre pro Tipo de Payload:{YELLOW} "))
    linha()
    tg = str(input(f"{GREEN}Digite una bandera, ejemplo: br, usa :{YELLOW} "))
    

    key = "((((((######0######0######--------AtlantusFree@@@@@@@@@@@@"

    gerar = int(input(f"""
   {DESTACAR}[ 1 ]{AZUL} {AZUL}Generar Payload Mod Spartano{AZUL}

   {DESTACAR}[ 2 ]{AZUL} {PURPULA}Generar Payload Normal, varia{AZUL}

    """))
    if gerar == 1:
        while True:                                                                                 
            menu = int(input(f"""
{DESTACAR}[ 𝟙 ]{AZUL} {PURPULA}Generar Con Su Payload Personalizado{AZUL}
{DESTACAR}[ 𝟚 ]{AZUL} {RED}generar SSL normal{AZUL}
{DESTACAR}[ 𝟛 ]{AZUL} {AZUL}Generar WebSocket Direct{AMARELO} 
{DESTACAR}[ 𝟜 ]{AZUL} {AMARELO}Generar SSL + Payload{PURPULA} 
{DESTACAR}[ 𝟝 ]{AZUL} {GREEN}Cuando Tengas Texto Generado Colocalo Aqui{YELLOW}
{DESTACAR}[ 𝟞 ]{AZUL} {CINZA}Volver{AZUL}
"""))
            if menu == 1:
                q = int(input('Cuantas Quieres Generar? '))
                m = q * custom()
                chave = "######"+nm+"!!!!1"
                print(m+chave+key, sep='')
            if menu == 2:
                q = int(input('Cuantas Quieres Generar? '))
                m = q * ssl()
                chave = "######"+nm+"!!!!1"
                print(m+chave+key)
            elif menu == 3:
                q = int(input('Cuantas Quieres Generar? '))
                m = q * web()
                chave = "######"+nm+"!!!!1"
                print(m+chave+key)
            elif menu == 4:
                q = int(input('Cuantas Quieres Generar? '))
                m = q * pay()
                chave = "######"+nm+"!!!!1"
                print(m+chave+key)
            elif menu == 5:
                dados = str(input(f'{AMARELO}Coloque aqui su texto generado para encriptarlo y subir al arquivo al sitio de atualizacion{GREEN}:{DESTACAR}{AZUL}'))
                valor = base64.b64encode(dados.encode('utf-8'))
                print(valor[::-1])
            elif menu == 6:
                break