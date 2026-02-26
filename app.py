import pyautogui as pg

while True:
    # --- O MENU VISUAL ---
    # Criamos uma janelinha com botões
    escolha = pg.confirm(text='O que deseja fazer?', title='Sistema de Triângulos', buttons=['Verificar um Novo Triângulo', 'Sair'])

    if escolha == 'Sair' or escolha is None:
        pg.alert(text='Encerrando o progama.', title='Fim')
        break

    if escolha == 'Verificar um novo triângulo':
        # --- ENTRADA DE DADOS ---
        # O prompt abre uma caixa para digitar. Precisamos converter para float.
        try:
            x = float(pg.prompt(text='Digite o valor do lado X:', title='Entrada de Dados'))
            y = float(pg.prompt(text='Digite o valor do lado Y:', title='Entrada de Dados'))
            z = float(pg.prompt(text='Digite o valor do lado Z:', title='Entrada de Dados'))
        except ValueError:
            pg.alert(text='Erro! Você precisa digitar números.', title='Entrada Inválida')
            continue

        # --- ESTAÇÃO 3 e 4: LOGÍSTICA DE VALIDAÇÃO E CLASSIFICAÇÃO ---
        if (x + y > z) and (x + z > y) and (y + z > x):
            
            if x == y == z:
                resultado = "EQUILÁTERO (Tudo igual!)"
            elif x == y or x == z or y == z:
                resultado = "ISÓSCELES (Dois iguais!)"
            else:
                resultado = "ESCALENO (Tudo diferente!)"
            
            # Exibe o resultado final numa caixa de alerta
            pg.alert(text=f'Resultado: Triângulo {resultado}', title='Classificação Concluída')
        
        else:
            pg.alert(text='Erro: Triângulo INVÁLIDO! As peças não fecham.', title='Atenção')
