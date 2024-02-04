import asyncio
import os
from playwright.async_api import async_playwright
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

async def main():
 async with async_playwright() as p:
    print("""

    ░█████╗░░█████╗░███╗░░██╗░██████╗██╗░░░██╗██╗░░░░░████████╗░█████╗░██████╗░  ░░░░░░  ░█████╗░██████╗░███████╗
    ██╔══██╗██╔══██╗████╗░██║██╔════╝██║░░░██║██║░░░░░╚══██╔══╝██╔══██╗██╔══██╗  ░░░░░░  ██╔══██╗██╔══██╗██╔════╝
    ██║░░╚═╝██║░░██║██╔██╗██║╚█████╗░██║░░░██║██║░░░░░░░░██║░░░███████║██████╔╝  █████╗  ██║░░╚═╝██████╔╝█████╗░░
    ██║░░██╗██║░░██║██║╚████║░╚═══██╗██║░░░██║██║░░░░░░░░██║░░░██╔══██║██╔══██╗  ╚════╝  ██║░░██╗██╔═══╝░██╔══╝░░
    ╚█████╔╝╚█████╔╝██║░╚███║██████╔╝╚██████╔╝███████╗░░░██║░░░██║░░██║██║░░██║  ░░░░░░  ╚█████╔╝██║░░░░░██║░░░░░
    ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝  ░░░░░░  ░╚════╝░╚═╝░░░░░╚═╝░░░░░~Gabrielfry
    """)
    print('Carregando...')
    ua = UserAgent(software_names=[SoftwareName.FIREFOX.value], operating_systems=[OperatingSystem.WINDOWS.value], limit=100)
    user_agent = ua.get_random_user_agent()
    browser = await p.firefox.launch(headless=True)
    context = await browser.new_context(user_agent=user_agent)
    page = await context.new_page()
    await page.goto('https://www.situacao-cadastral.com/')
    os.system('cls')
    cpf = input('Insira o CPF a ser consultado!:')
    await page.fill('input#doc', cpf)
    await page.click('#consultar')
    texto = await page.inner_text('#resultado')
    os.system('cls')
    print("""

    ██████╗░███████╗░██████╗██╗░░░██╗██╗░░░░░████████╗░█████╗░██████╗░░█████╗░
    ██╔══██╗██╔════╝██╔════╝██║░░░██║██║░░░░░╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗
    ██████╔╝█████╗░░╚█████╗░██║░░░██║██║░░░░░░░░██║░░░███████║██║░░██║██║░░██║
    ██╔══██╗██╔══╝░░░╚═══██╗██║░░░██║██║░░░░░░░░██║░░░██╔══██║██║░░██║██║░░██║
    ██║░░██║███████╗██████╔╝╚██████╔╝███████╗░░░██║░░░██║░░██║██████╔╝╚█████╔╝
    ╚═╝░░╚═╝╚══════╝╚═════╝░░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░╚════╝░
    """)
    print(texto)
    final = input('Deseja consultar outro CPF?: (Sim) ou (Não):')
    if final == 'sim' or 'Sim' or 's':
         os.system('cls')
         await main()
    else:
         print('Finalizando Consulta...')

asyncio.run(main())
