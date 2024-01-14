# OSINT-Steam

Este script em Python foi desenvolvido para extrair informações detalhadas de perfis Steam, proporcionando uma visão rápida e personalizada. Utilizando web scraping com as bibliotecas `requests` e `BeautifulSoup`, o código permite a obtenção de dados como nome/nick, avatar, nome real, localização, atividade recente, nível e status do perfil.

### Utilização

1. **Substitua a URL do Perfil Steam:**
   - No início do script, substitua a variável `url` pelo URL do perfil Steam desejado.

```python
url = 'URL_DO_PERFIL_STEAM'  # Substitua pelo URL do perfil Steam desejado
```

2. **Execute o Script:**
   - Após substituir a URL, execute o script em um ambiente Python para visualizar as informações extraídas do perfil.

```bash
python nome_do_script.py
```

### Informações Extraídas

- **Nome/Nick:** Nome ou apelido do perfil Steam.
- **Avatar:** Link direto para a imagem do avatar.
- **Nome Real:** Nome real associado ao perfil (se disponível).
- **Localização:** Localização indicada no perfil Steam (se disponível).
- **Atividade Recente:** Tempo da atividade mais recente no perfil Steam.
- **Nível:** Nível do perfil Steam.
- **Status:** Status atual do perfil Steam.

### Observações

- Certifique-se de respeitar os Termos de Serviço do Steam ao usar este script para evitar violações.
- Em caso de erro ao acessar o perfil Steam, será exibido o código de status correspondente.

Esperamos que este script seja útil para obter informações específicas de perfis Steam de forma eficiente. Se tiver alguma dúvida ou sugestão de melhoria, sinta-se à vontade para contribuir ou entrar em contato.
