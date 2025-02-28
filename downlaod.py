import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


nome_do_filme = input("Digite o nome do filme que deseja buscar: ")

driver = webdriver.Firefox()

driver.get("https://redecanais.fi/")

sleep(2)


fechar = pyautogui.locateCenterOnScreen('/home/kk/Documentos/projetos/automação/filmes/X.png')

if fechar:
    pyautogui.click(fechar[0], fechar[1])
    print("Botão de fechar clicado.")
else:
    print("Botão de fechar não encontrado.")

sleep(1)


pesquisar = pyautogui.locateCenterOnScreen('/home/kk/Documentos/projetos/automação/filmes/pesquisar.png')

if pesquisar:
    pyautogui.click(pesquisar[0], pesquisar[1])
    print("Botão de pesquisa clicado.")
else:
    print("Botão de pesquisa não encontrado.")


try:
    barra_pesquisa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pm-search"))
    )


    barra_pesquisa.send_keys(nome_do_filme)
    barra_pesquisa.send_keys(Keys.RETURN)
    print("Pesquisa realizada com sucesso!")

except Exception as e:
    print(f"Erro ao encontrar a barra de pesquisa: {e}")

search_results = driver.find_elements(By.CSS_SELECTOR, "div.tF2Cxc a")

# Lista os links com números
links = []
for i, result in enumerate(search_results):
    href = result.get_attribute("href")
    if href:
        links.append(href)
        print(f"[{i+1}] {href}")

# Pergunta ao usuário qual link abrir
choice = int(input("\nDigite o número do link para abrir: ")) - 1

# Abre o link escolhido
if 0 <= choice < len(links):
    driver.get(links[choice])
else:
    print("Número inválido!")


# driver.quit()

