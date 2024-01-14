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
Created by Kensdy
"""

print(ascii_art)

# Request Steam profile URL
url = input("Enter the Steam profile URL: ")

# Perform HTTP request
response = requests.get(url)

if response.status_code == 200:
    # Create a BeautifulSoup object for easy HTML information extraction
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract specific information
    name_nick_raw = soup.find('meta', property='og:title')
    name_nick = name_nick_raw['content'].replace('Steam Community :: ', '') if name_nick_raw else None

    # Modification to extract the image link directly
    img_player_avatar_link = soup.find('link', rel='image_src')['href'] if soup.find('link', rel='image_src') else None

    # Modification to fix the extraction of location
    header_real_name = soup.find('div', class_='header_real_name')
    name_real = header_real_name.find('bdi').text.strip() if header_real_name else None
    location = header_real_name.contents[-1].strip() if header_real_name else None

    # Modification to fix the extraction of recent activity time
    recent_activity = soup.find('div', class_='recentgame_quicklinks')
    recent_time_tag = recent_activity.find('h2') if recent_activity else None
    recent_time = recent_time_tag.text.strip() if recent_time_tag else None

    level = soup.find('div', class_='persona_level').text.strip() if soup.find('div', class_='persona_level') else None

    status = soup.find('div', class_='profile_in_game_header').text.strip() if soup.find('div', class_='profile_in_game_header') else None

    # Display the information
    print(f'Name/Nick: {name_nick}')
    print(f'Avatar: {img_player_avatar_link}')
    print(f'Real Name: {name_real}')
    print(f'Location: {location}')
    print(f'Recent Activity: {recent_time}')
    print(f'Level: {level}')
    print(f'Status: {status}')

else:
    print(f'Error accessing the Steam profile. Status code: {response.status_code}')
