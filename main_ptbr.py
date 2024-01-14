import requests
from bs4 import BeautifulSoup

# ASCII Art
ascii_art = """
 ___  ____ ___ _   _ _____    
/ _ \/ ___|_ _| \ | |_   _|   
| | | \___ \| ||  \| | | |     
| |_| |___) | || |\  | | |     
 \___/|____/___|_| \_| |_|     
/ ___|| |_ ___  __ _ _ __ ___  
\___ \| __/ _ \/ _` | '_ ` _ \ 
 ___) | ||  __/ (_| | | | | | |
|____/ \__\___|\__,_|_| |_| |_|
Criado por Kensdy
"""

print(ascii_art)

# Solicita a URL do perfil Steam
url = input("Digite o URL do perfil Steam: ")

# Realiza a requisição HTTP
response = requests.get(url)

if response.status_code == 200:
    # Cria um objeto BeautifulSoup para facilitar a extração de informações do HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extrai informações específicas
    nome_nick_raw = soup.find('meta', property='og:title')
    nome_nick = nome_nick_raw['content'].replace('Steam Community :: ', '') if nome_nick_raw else None

    # Modificação para extrair o link da imagem diretamente
    img_player_avatar_link = soup.find('link', rel='image_src')['href'] if soup.find('link', rel='image_src') else None

    # Modificação para corrigir a extração da localização
    header_real_name = soup.find('div', class_='header_real_name')
    nome_real = header_real_name.find('bdi').text.strip() if header_real_name else None
    localizacao = header_real_name.contents[-1].strip() if header_real_name else None

    # Modificação para corrigir a extração do tempo da atividade recente
    atividade_recente = soup.find('div', class_='recentgame_quicklinks')
    tempo_recente_tag = atividade_recente.find('h2') if atividade_recente else None
    tempo_recente = tempo_recente_tag.text.strip() if tempo_recente_tag else None

    nivel = soup.find('div', class_='persona_level').text.strip() if soup.find('div', class_='persona_level') else None

    status = soup.find('div', class_='profile_in_game_header').text.strip() if soup.find('div', class_='profile_in_game_header') else None

    # Exibe as informações
    print(f'Nome/Nick: {nome_nick}')
    print(f'Avatar: {img_player_avatar_link}')
    print(f'Nome Real: {nome_real}')
    print(f'Localização: {localizacao}')
    print(f'Atividade Recente: {tempo_recente}')
    print(f'Nível: {nivel}')
    print(f'Status: {status}')

else:
    print(f'Erro ao acessar o perfil Steam. Código de status: {response.status_code}')
