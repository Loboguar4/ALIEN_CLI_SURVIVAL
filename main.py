#!/usr/bin/env python3
# ============================================================
# Alien: Terminal Survival
# Versão: 1.0.0
#
# Copyright (C) 2025 Bandeirinha
#
# Este programa é software livre: você pode redistribuí-lo
# e/ou modificá-lo sob os termos da Licença Pública Geral GNU
# conforme publicada pela Free Software Foundation, na versão 3
# da Licença, ou (a seu critério) qualquer versão posterior.
#
# Este programa é distribuído na esperança de que seja útil,
# mas SEM QUALQUER GARANTIA; sem sequer a garantia implícita de
# COMERCIALIZAÇÃO ou ADEQUAÇÃO A UM DETERMINADO PROPÓSITO.
# Veja a Licença Pública Geral GNU para mais detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa. Caso contrário, veja:
# https://www.gnu.org/licenses/
#
# ------------------------------------------------------------
# AVISO LEGAL:
# Este é um projeto feito por fã, sem fins comerciais.
# Não é afiliado, endossado ou associado à franquia Alien
# ou a seus detentores de direitos.
#
# Todo o código é original. Conceitos narrativos são usados
# apenas como inspiração artística.
# ============================================================


import random
import time
import math
import sys


# codigos ANSI para efeitos de texto
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
LIGHT_GREEN = "\033[92m"
RED = "\033[31m"
LIGHT_RED = "\033[91m"  # Vermelho claro
INVISIBLE = "\033[8m"  # Tornar o texto invisível
BRIGHT_YELLOW = "\033[93m"  # Amarelo brilhante (mais claro)
YELLOW = "\033[33m"      

# Funcao para imprimir textos dos terminais
def terminal_text(text):
    for char in text:
        sys.stdout.write(CYAN + BOLD + char + RESET) # Usando verde e um pouco de brilho
        sys.stdout.flush()
        time.sleep(0.001) # Tempo de espera entre cada caractere
    print() # Nova linha no terminal   
    
def terminal_slow(text):
    for char in text:
        sys.stdout.write(LIGHT_GREEN + char + RESET) # Usando verde e um pouco de brilho
        sys.stdout.flush()
        time.sleep(0.02) # Tempo de espera entre cada caractere
    print() # Nova linha no terminal


def blink_effect(text, blink_delay=0.5, total_blinks=5):
    for _ in range(total_blinks):  # Define quantas vezes o texto vai "piscar"
        sys.stdout.write(INVISIBLE + text + RESET)  # Texto invisível
        sys.stdout.flush()
        time.sleep(blink_delay)  # Espera entre as piscadas
        sys.stdout.write(RED + text + RESET)  # Texto visível em vermelho claro
        sys.stdout.flush()
        time.sleep(blink_delay)  # Espera entre as piscadas
    print()  # Nova linha no terminal

def typewriter_effect_b(text, delay = 0.1):
    for char in text:
        sys.stdout.write(YELLOW + char + RESET) # Usando amarelo e um pouco de brilho
        sys.stdout.flush()
        time.sleep(0.02) # Tempo de espera entre cada caractere
    print() # Nova linha no terminal

# Controla a exibição gráfica com exceção do mapa
from scenarios import corridor1, open_door, corridor_a, dark_corridor, tight_corridor, new_corridor, asteroid, asteroid1, asteroid2, med, living, living_alt, communications, engine, cargo, control_room, control_room2, get_flamethrower
from organisms import xenomorph_face, xenomorph_face2, xenomorph, xenomorph_attack, xenomorph_is_near, xenomorph_far, facehugger_is_near, facehugger_attack, facehugger_alt_attack, facehugger_last_attack, body
 
def alien_is_near(corridor1, open_door, corridor_a, dark_corridor, tight_corridor, new_corridor, xenomorph_is_near, xenomorph_far):
    return random.choice([corridor1, open_door, corridor_a, dark_corridor, tight_corridor, new_corridor, xenomorph_is_near, xenomorph_far])

def facehugger_approaches(corridor1, open_door, corridor_a, dark_corridor, tight_corridor, new_corridor, facehugger_is_near):
    return random.choice([corridor1, open_door, corridor_a, dark_corridor, tight_corridor, new_corridor, facehugger_is_near])

def rand_corridor(corridor1, open_door, corridor_a, dark_corridor, tight_corridor, new_corridor):
	return random.choice([corridor1, open_door, corridor_a, dark_corridor, tight_corridor, new_corridor])
	
def rand_dark_corridor(dark_corridor, tight_corridor):
	return random.choice([dark_corridor, tight_corridor])

def rand_systems(control_room, control_room2):
	return random.choice([control_room, control_room2])
	
def rand_living(living, living_alt, communications):
	return random.choice([living, living_alt, communications])
	
def rand_alien_combat(xenomorph, xenomorph_attack, xenomorph_is_near):
	return random.choice([xenomorph, xenomorph_attack, xenomorph_is_near])

def rand_alien_face(xenomorph_face, xenomorph_face2, xenomorph, xenomorph_attack, xenomorph_is_near):
	return random.choice([xenomorph_face, xenomorph_face2, xenomorph, xenomorph_attack, xenomorph_is_near])
	
def facehugger_jumpscare(facehugger_is_near, facehugger_attack, facehugger_alt_atack, facehugger_last_attack):
	return random.choice([facehugger_is_near, facehugger_attack, facehugger_alt_atack, facehugger_last_attack])

def facehugger_kissing(facehugger_attack, facehugger_alt_attack, facehugger_last_attack):
	return random.choice([facehugger_attack, facehugger_alt_attack, facehugger_last_attack])
	

# Configurações básicas
timer = 526  # tempo em minutos para o resgate
energy_level = 72  # Energia da nave em %
integridade_nave = 96  # Integridade da nave e suporte à vida em %
player_position = (0, 0)  # Posição inicial do jogador
map_size = (7, 7)  # Tamanho reduzido do mapa (7x7)
map_grid = [[' ' for _ in range(map_size[0])] for _ in range(map_size[1])]  # Mapa em grade

# Salas e terminais com posições únicas
available_positions = [(x, y) for x in range(map_size[0]) for y in range(map_size[1])]
random.shuffle(available_positions)

rooms = {}
room_names = ["Engine Room", "Control Room", "Cargo Bay", "Living Quarters", "Med Bay"]

for room in room_names:
    rooms[room] = available_positions.pop()


terminais = list(rooms.keys())  # Nomes dos terminais da nave
alien_positions = [(random.randint(0, map_size[0] - 1), random.randint(0, map_size[1] - 1))]
facehuggers = []
pending_events = {}
energy_redirected = False  # Flag para controle do redirecionamento de energia


# Estrutura do inventário
inventory = {
    "Flamethrower": None	
}

# Variáveis de status para itens
flamethrower_fuel = 0  
  

# Função para coletar itens (pode ser chamada após o comando 'p' de procurar)
def collect_item(item_name):
    global flamethrower_fuel  

    if item_name == "Flamethrower":
        if inventory["Flamethrower"] is None:
            flamethrower_fuel = random.randint(0, 99)
            inventory["Flamethrower"] = True
            print(get_flamethrower)            
            print(f"\nVocê encontrou um {item_name} com {flamethrower_fuel}% de combustível."), time.sleep(2)
        else:
            flamethrower_fuel = flamethrower_fuel + random.randint(15, 20) 
            print("\nVocê encontrou combustível.")
            time.sleep(2)

# Função para procurar       
def search():
    found_item = False
    
    # Probabilidade de encontrar um item (50% de chance, por exemplo)
    if random.random() < 0.07:
        # Sorteia qual item será encontrado
        item = random.choice(["Flamethrower"])
        collect_item(item)
        found_item = True
    
    if not found_item:
        # Verifica se o jogador está em uma sala com terminal
        current_room = None
        for room, pos in rooms.items():
            if player_position == pos:
                current_room = room
                break

        if current_room:
            if current_room == "Engine Room":
                print(engine)
                if random.random() < 0.1:
                    print("\nNada, além de manchas de sangue.\n"), time.sleep(2)
                else:    
                    print("\nNada útil encontrado.\n"), time.sleep(2)
            elif current_room == "Control Room":
                print(rand_systems(control_room, control_room2))
                if random.random() < 0.1:
                    print("\nNada, além de manchas de sangue.\n"), time.sleep(2)
                else: 
                    print("\nNada útil encontrado.\n"), time.sleep(2)
            elif current_room == "Cargo Bay":
                print(cargo)
                if random.random() < 0.1:
                    print(body)	
                    print("\nNunca vi algo tão brutal.\n"), time.sleep(2)
                else: 
                    print("\nVocê procurou, mas não encontrou nada útil.\n"), time.sleep(2)
            elif current_room == "Living Quarters":
                print(rand_living(living, living_alt, communications))
                if random.random() < 0.1:
                    print("\nNada, além de manchas de sangue.\n"), time.sleep(2)
                else: 
                    print("\nVocê procurou, mas não encontrou nada útil.\n"), time.sleep(2)
            elif current_room == "Med Bay":
                print(med)
                if random.random() < 0.1:
                    print("\nNada, além de manchas de sangue.\n"), time.sleep(2),
                else:  
                    print("\nVocê procurou, mas não encontrou nada útil.\n"), time.sleep(2)      
    
        else:
            print(rand_dark_corridor(dark_corridor, tight_corridor))
            if random.random() < 0.1:
                print("\nMuito escuro em alguns lugares.\n"), time.sleep(2)
            else: 
                print("\nNada útil encontrado.\n"), time.sleep(2)


# Função para interagir com inimigos
def encounter_enemy(enemy_type):
    global flamethrower_fuel 
    
    if enemy_type == "Alien":
        if inventory["Flamethrower"] and flamethrower_fuel > 0:
            fuel_usage = random.randint(25, 50)
            if flamethrower_fuel >= fuel_usage:
                flamethrower_fuel -= fuel_usage
                print(rand_alien_combat(xenomorph, xenomorph_attack, xenomorph_is_near))
                print("\n\n\tVocê usou o Flamethrower no Alien!"), time.sleep(3)
                print(f"\n\n\tCombustível restante: {flamethrower_fuel}%.\n\n"), time.sleep(3)
                draw_map()
                # O Alien continua se movimentando, mas a morte foi evitada
            else:
                print(rand_alien_face(xenomorph_face, xenomorph_face2, xenomorph, xenomorph_attack, xenomorph_is_near))             
                terminal_slow("\n\n\tCombustível insuficiente!"), time.sleep(3)
                terminal_slow("\n\n\tO Alien te capturou."), time.sleep(2)
                terminal_slow("\n\n\tFim de jogo.\n\n"), time.sleep(3)
                # O jogo pode acabar aqui ou aplicar alguma penalidade
                exit()
        else:
            print(rand_alien_face(xenomorph_face, xenomorph_face2, xenomorph, xenomorph_attack, xenomorph_is_near))
            terminal_slow("\n\n\tVocê não tem como se defender!"), time.sleep(3)
            terminal_slow("\n\n\tO Alien te capturou."), time.sleep(2)
            terminal_slow("\n\n\tFim de jogo.\n\n"), time.sleep(2)
            # O jogo pode acabar aqui ou aplicar alguma penalidade
            exit()
	
  
    if enemy_type == "Facehugger":
        if inventory["Flamethrower"] and flamethrower_fuel > 0:
            fuel_usage = random.randint(20, 30)
            if flamethrower_fuel >= fuel_usage:
                flamethrower_fuel -= fuel_usage
                print(facehugger_jumpscare(facehugger_is_near, facehugger_attack, facehugger_alt_attack, facehugger_last_attack))
                print("\n\n\tVocê queimou o Facehugger com o Flamethrower!"), time.sleep(3)
                print(f"\n\n\tCombustível restante: {flamethrower_fuel}%.\n\n"), time.sleep(3)
                # O Facehugger desaparece do mapa
                facehuggers.remove(player_position)
                draw_map()
            else:
                print(facehugger_kissing(facehugger_attack, facehugger_alt_attack, facehugger_last_attack))            
                terminal_slow("\n\n\tCombustível insuficiente!"), time.sleep(3)
                terminal_slow("\n\n\tO Facehugger te atacou..."), time.sleep(2)
                terminal_slow("\n\n\tE não há mais o que fazer sendo um hospedeiro."), time.sleep(2)
                terminal_slow("\n\n\tFim de jogo.\n\n"), time.sleep(3)
                # O jogo pode acabar aqui ou aplicar alguma penalidade
                exit()
        else:
            print(facehugger_kissing(facehugger_attack, facehugger_alt_attack, facehugger_last_attack))    
            terminal_slow("\n\n\tVocê não tem como se defender!"), time.sleep(3) 
            terminal_slow("\n\n\tO Facehugger te atacou..."), time.sleep(2)
            terminal_slow("\n\n\tE não há mais o que fazer sendo um hospedeiro."), time.sleep(2)
            terminal_slow("\n\n\tFim de jogo.\n\n"), time.sleep(3)
            exit()
 

# Funções para desenhar o mapa e o terminal
def draw_map():
    terminal_text("\n\n\tSENSOR DE MOVIMENTO:\n")
    padding = " " * 10
    for y in range(map_size[1]):
        print(padding, end=' ')
        for x in range(map_size[0]):
            if (x, y) == player_position:
                print('┼', end=' ')
            elif (x, y) in alien_positions:
                print('■', end=' ')
            elif (x, y) in facehuggers:
                print('*', end=' ')
            elif (x, y) in rooms.values():
                print('█', end=' ')  # Indica uma sala
            else:
                print(map_grid[y][x], end=' ')
        print()
    print('\n')

def terminal_interface(terminal_name):
    global energy_level
    terminal_text(f"\n\tBEM-VINDO AO TERMINAL {terminal_name}.\n")
    
    if terminal_name == "Engine Room":
        terminal_text("[1] Sistema de Energia")
    elif terminal_name == "Control Room":
        terminal_text(f"\n\n\tIntegridade geral da nave: {integridade_nave}%\n\n[1] Sistema de Pilotagem")    
    elif terminal_name == "Cargo Bay":
        terminal_text("[1] Verificar Cargas")
    elif terminal_name == "Living Quarters":
        terminal_text("[1] Verificar Comunicações")
    elif terminal_name == "Med Bay":
        terminal_text("[1] Verificar Sistema de Saúde")
    
    terminal_text("[2] Logs e Mensagens")
    terminal_text("[3] Sair do Terminal")
    
    while True:
        choice = input("\nSelecione uma opção (ou pressione Enter para pular): ").strip()

        # Se o usuário pressionar Enter sem digitar nada, consideramos um "comando nulo"
        if choice == "":
            print("\nComando nulo - passagem de turno.\n")
            return None
        
        # Verifica se a escolha é um número válido entre 1 e 3
        if choice.isdigit() and 1 <= int(choice) <= 3:
            return int(choice)
        else:
            print("\nOpção inválida. Tente novamente.\n") 

	
# Funções para os sistemas específicos de cada terminal
def sistema_energia():
    global energy_level, energy_redirected, pending_events
    terminal_text("\n\n\t=== Sistema de Energia ===\n\n")
    print(engine)
    terminal_text(f"\tNível de Energia: {energy_level}%\n")

    if energy_level <= 15:
        terminal_text("\n\n\tAlerta! Baixo nível de energia detectado."), time.sleep(3)
        terminal_text("\n\n\tRedirecione a energia do reator ou configure o consumo de energia da nave.\n\n")

    if "Vazamento de Ar" in pending_events:
        action = input("\nDeseja redirecionar energia para resolver o vazamento de ar? [s/n]: ")
        if action == 's':
            del pending_events["Vazamento de Ar"]
            energy_level = max(0, energy_level - random.randint(1, 3))
            print(engine)
            time.sleep(3)
            print("\n\n\tVazamento de ar resolvido.\n"), time.sleep(2)
        else:
            print(engine)
            print("\n\tNenhuma ação foi tomada."), time.sleep(2)
    elif not energy_redirected:
        action = input("\nDeseja redirecionar energia? [s/n]: ")
        if action == 's':
            #recovery = min(26, 100 - energy_level)  # Recupera até 26% da energia faltante
            recovery = max(0, energy_level - random.randint(15, 35)) # anteriormente: 15, 25 ... 10, 30
            energy_level += recovery
            print(engine)
            terminal_text(f"\n\n\tRecuperação de energia: {recovery}%.\n"), time.sleep(2) 
            terminal_text(f"\n\tNovo nível de energia: {energy_level}%.\n"), time.sleep(2)
            energy_redirected = True  # Marca que o redirecionamento foi realizado
            # if energy_level > 100: time.sleep(2) print("""
            # Sobrecarga nos módulos de enrgia da nave... Instabiliade crítica detectada!""")
             
            if energy_level >= 100:
                blink_effect("\n\n\tALERTA!"), time.sleep(3)
                blink_effect("\n\n\tSOBRECARGA DE ENERGIA NO REATOR DETECTADA!"), time.sleep(3)
                terminal_slow("\n\n\tUma explosão ocorreu devido a instabilidade no reator, destruindo a nave."), time.sleep(2)
                terminal_slow("\n\n\tFim de jogo.\n\n"), time.sleep(3)
                exit()
        else:
            print(engine)
            print("\nNenhuma ação foi tomada.\n"), time.sleep(2)
    else:
        print("\n\tO redirecionamento de energia já foi realizado.\n"), time.sleep(2)

def sistema_pilotagem():
    global pending_events, energy_level
    terminal_text("\n\n\t=== Sistema de Pilotagem ===\n\n")
    if "Colisão Iminente" in pending_events:
        print(asteroid)
        print("\n\tDesviando curso para evitar colisão iminente...\n"), time.sleep(3)
        energy_level = max(0, energy_level - random.randint(1, 3))
        del pending_events["Colisão Iminente"]
        print(asteroid2)
        print("\n\tColisão evitada com sucesso.\n"), time.sleep(2)
    else:
        print(rand_systems(control_room, control_room2))
        print("\n\tNenhuma ação de pilotagem necessária no momento.\n"), time.sleep(2)

def resolver_curto_circuito():
    global pending_events, energy_level
    terminal_text("\n\n\t=== Assistente de Reparo ===\n\n")
    if "Curto-circuito" in pending_events:
        print(rand_systems(control_room, control_room2))
        terminal_text("\n\tCurto-circuito detectado! Iniciando modo de reparo...\n"), time.sleep(3)
        energy_level = max(0, energy_level - random.randint(1, 3))
        del pending_events["Curto-circuito"]
        terminal_text("\n\tCurto-circuito resolvido com sucesso.\n"), time.sleep(2)
    else:
        print(rand_systems(control_room, control_room2))
        terminal_text("\n\tNenhum problema detectado.\n"), time.sleep(2)

def verificar_cargas():
    global pending_events, energy_level
    terminal_text("\n\n\t=== Verificação de Cargas ===\n\n")
    if "Anomalia na Carga" in pending_events:
        print(cargo)
        print("\n\tResolvendo anomalia na carga...\n"), time.sleep(3)
        energy_level = max(0, energy_level - 1)
        del pending_events["Anomalia na Carga"]
        print("\n\tAnomalia resolvida com sucesso.\n"), time.sleep(2)
    else:
        print(cargo)
        print("\n\tNenhuma anomalia detectada nas cargas.\n"), time.sleep(2)

def verificar_comunicacoes():
    global pending_events, energy_level
  
    terminal_text("\n\n\t=== Verificação de Comunicações ===\n\n")
    terminal_text(f"\n\tTempo estimado para o resgate: {timer} minutos.\n"), time.sleep(3)
    if "Comunicações Interrompidas" in pending_events:
        print(communications)
        terminal_text("\n\tRestaurando comunicações...\n"), time.sleep(3)
        energy_level = max(0, energy_level - random.randint(1, 2))
        del pending_events["Comunicações Interrompidas"]
        print("\n\tComunicações restauradas com sucesso.\n"), time.sleep(2)
    else:
        print(communications)
        print("\n\tSinal fraco, mas estável. Nenhum problema detectado.\n"), time.sleep(2)

def verificar_saude():
    global pending_events, energy_level
    terminal_text("\n\n\t=== Verificação do Sistema de Saúde ===\n\n")
    if "Problema de Saúde" in pending_events:
        print(med)
        print("\n\tResolvendo problema de saúde...\n"), time.sleep(3)
        energy_level = max(0, energy_level - 1)
        del pending_events["Problema de Saúde"]
        print("\n\tProblema de saúde resolvido com sucesso.\n"), time.sleep(2)
    else:
        print(med)
        print("\n\tTodos os sistemas de saúde e suporte à vida estão operando dentro dos parâmetros normais.\n"), time.sleep(3)

def logs_mensagens(terminal_name):
    terminal_text("\n\n\t=== Logs e Mensagens ===\n\n")
    if terminal_name == "Engine Room":
        logs = [
            "\nLog 001: Relatório de manutenção do reator. Operando a 95% de capacidade.",
            "Log 002: Anomalia detectada no sistema de refrigeração. Necessita reparo.\nAté lá os propulsores primários estarão inoperantes.\n",
            "Log 003: Atenção! Enquanto o reator e o sistema de refrigeração estiverem sob manutenção, por favor não sobrecarregar o reator usando a chave de redirecionamento automática.\n\nAté o reparo for concluído, a tripulação manterá a nave em IDLE pelo tempo que for necessário.'\n"
        ]
    elif terminal_name == "Control Room":
        logs = [
            "\nLog 001: Desvio de asteroide concluído com sucesso.",
            "Log 002: Relatório do piloto: 'Algo estranho no radar. Movimentação irregular.'\n"
        ]
    elif terminal_name == "Cargo Bay":
        logs = [
            "\nLog 001: Carga 23A: Conteúdo biológico intacto. Observação: alto risco.",
            "Log 002: Sensor detectou movimento na área de carga. Verificação necessária.\n"
        ]
    elif terminal_name == "Living Quarters":
        logs = [
            "\nLog 001: Relatório de descanso da tripulação: Todos a bordo.",
            "Log 002: Transmissão da Terra: 'Nenhuma atividade anormal.'",
            "Log 003: SOS PEDIDO DE SOCORRO SOS: 'O conteúdo biológico saiu de controle.\nAs criaturas parecem apresentar um ciclo de vida parasitário e são extremamente letais.\n\nForte supeita de sabotagem.\n\nConforme sugerem os logs da central, o módulo de fuga foi ejetado da nave-mãe sem nenhum tripulante a bordo. O nosso sintético ficou inoperante pouco antes das anomalias começarem...\nSeus módulos de memória e de backup foram comprometidos por razão ainda desconhecida, e os propulsores primários também estão inoperantes devido à uma anomalia no reator.\n\nNo momento restam dois sobreviventes.'\n\n",
            "Log 004: Transmissão da Colônia Wayland: Resgate qualificado a caminho. \n" 
	    ]		
    elif terminal_name == "Med Bay":
        logs = [
            "\nLog 001: Análise biológica: Organismos desconhecidos. Monitoramento contínuo.\n",
            "Log 002: Nota: Um dos tripulantes relatou dificuldade para respirar.\n",
            '''Log 003: Análise biológica: Escaneamento concluído.            
   ..................................................................                           
.................................^...........~...........                            
.................................~:..........7:..........                            
.................................~:::.......!!^.........                             
.................................:^::.......!J^.......                              
..................................:7:^:.....^7^^...                                  
...................................!^7^.....!!7^.                               
...................................~^!:    .J7~.             .:.                     
...................................^:!:    ^J7:           .!!~:                     
.................:::::.............:^!:.. .77!.         .:!7!.                       
...................::::~^..........:^!:...:7!^        .:~!7!.                         
.....................:!7!!^........^:~!..:?!7:     ..:!?7^..                
........................^!77^.....:~^7^.~?!!^.  ...^!77^.                            
..........................^!?7~:..!^~^.77~~:..::^~7!~:.      ..:^^^.                   
............................^~!?^!^^!~?7~~!~!~~~^~^.   ...:^!7JY7^.                  
..............::^:^:.:^:.....:^??!:~?!^^7!!!~^::...::^~~7?JJ?7~.                      
.................:^:^!????7~~~^~!7?!7^:~7!~~^7!^^:^!7!~^^:...                        
.......................::^~!77?7!7?!:.^7~~^::^^:::::..                               
............................~^^^!J7^..~?!~^:::::::::.............                    
............................^??!7J7:..^?!~~!!~:::^!7!!!!!77?7?YY?!~:                  
..........................:^7JY?7??^..~YJ!7~^:.............:::::....                 
.....................:^~^~!7J?~::~7^:.!5!^~!JYJ7:.                                   
  ......................:^^^^:::^!!7^:!J^^~!7J5PP^                                   
    ...................^^:..::^~!?J7^:?!7?77?Y5GG7                                   
     .......................:^~7JY!^::7^.!PJJYPGG!.                                  
    ....................::::^!7YY^.::.^!..?G555J^.                                   
    ....................^7?JJJY7:..:^^^?...:~^.......                                
     .....................:^~^.....^^~~J................                             
  .................................^:^7?...................                          
  .................................:::7?......................                       
 ..................................:.:!?.........................                    

	Organismo parasitóide: 98% de chance. 

	Multicelular: Sim. 
	
    Análise toxicológica: Nenhuma toxina conhecida detectada.

	Origem: Desconhecida.  
	
	Taxonomia: Desconhecida, embora apresente um sistema nervoso.   
	
	
	NOTA DE PERICULOSIDADE: Os "ovos" coletados eclodiram e duas das criaturas se espalharam pela da nave, 
	apresentando um sério risco não somente para a nossa missão, mas também para o restante da tripulação.
	 
	Um tripulante foi atacado e está dominado por uma dessas criaturas. Segundo os exames radiológicos,
	 ela está realizando um processo de inseminacão. Todas as tentativas de removê-la foram ineficazes. E seu
	sistema vascular coagula uma substância EXTREMAMENTE ácida.

	Ciclo de vida ainda desconhecido.	  
		
	Somos especializados em exogeologia e missões de exploração de curto prazo... 
	
	Devíamos considerar maior apoio científico, e quem sabe... militar... Mas por algum motivo, o pedido de ajuda foi atrasado.	
            '''
        ]
        
    for log in logs:
        terminal_text(log)
    input("Pressione Enter para sair."), time.sleep(1) 
    
    
# Função para gerar eventos aleatórios
def alert_event():
    global pending_events
    event = random.choice([
        "Vazamento de Ar", 
        "Curto-circuito", 
        "Anomalia na Carga", 
        "Comunicações Interrompidas", 
        "Problema de Saúde", 
        "Colisão Iminente"
    ])
    if event == "Vazamento de Ar":
        pending_events[event] = (22, "Engine Room")
        typewriter_effect_b("\nAlerta: Vazamento de Ar detectado! Resolva o problema na Engine Room.\n")
    elif event == "Curto-circuito":
        pending_events[event] = (22, "Control Room")
        typewriter_effect_b("\nAlerta: Curto-circuito detectado! Resolva o problema na Control Room. Acesse o Sistema de Pilotagem\n da nave para acessar o assistente de reparos.\n")
    elif event == "Anomalia na Carga":
        pending_events[event] = (22, "Cargo Bay")
        typewriter_effect_b("\nAlerta: Anomalia na carga detectada! Resolva o problema na Cargo Bay.\n")
    elif event == "Comunicações Interrompidas":
        pending_events[event] = (22, "Living Quarters")
        typewriter_effect_b("\nAlerta: Comunicações interrompidas! Resolva o problema na Living Quarters.\n")
    elif event == "Problema de Saúde":
        pending_events[event] = (22, "Med Bay")
        typewriter_effect_b("\nAlerta: Problema de saúde detectado! Resolva o problema na Med Bay.\n")
    elif event == "Colisão Iminente":
        pending_events[event] = (10, "Control Room")
        blink_effect("\n\n\tALERTA!"), time.sleep(3)
        typewriter_effect_b("\nColisão iminente! Resolva o problema na Control Room.\n")        

    time.sleep(2)  # Simulação de um pequeno delay para emergência

# Função para processar eventos pendentes
def process_pending_events():
    global pending_events, timer, energy_level, integridade_nave

    for event, (time_left, location) in list(pending_events.items()):
        if time_left <= 0:
            if event == "Colisão Iminente":
                time.sleep(3)
                print(asteroid1)
                terminal_slow("\n\n\tA colisão da nave com um asteroide ocorreu!"), time.sleep(3)
                terminal_slow("\n\n\tEla foi destruída."), time.sleep(2)
                terminal_slow("\n\n\tFim de jogo.\n\n"), time.sleep(3)
                exit()
            else:
                print(f"\nFalha em resolver o evento: {event}!\n"), time.sleep(3)
                integridade_nave = max(0, integridade_nave - random.randint(10, 30)) # dano de integridade 
                del pending_events[event]
        else:
            pending_events[event] = (time_left - 1, location)


# Função para calcular a distância entre duas posições no mapa
def calcular_distancia(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Função para verificar se o jogador está perto do alien ou facehugger
def verificar_proximidade():
    global player_position, alien_positions, facehuggers

    for alien_pos in alien_positions:
        distancia = calcular_distancia(player_position, alien_pos)
        if distancia <= 2 and random.random() < 0.5:  # chance de um evento aleatório ocorrer

            # TASK: Incorporar verificacao de salas
            print(alien_is_near(corridor1, open_door, corridor_a, dark_corridor, tight_corridor, new_corridor, xenomorph_is_near, xenomorph_far))
            terminal_slow("\n\n\tVocê ouve ruídos metálicos..."), time.sleep(2)
            terminal_slow("\n\te passos pesados.\n")
            time.sleep(2)  # Pausa para aumentar a tensão

    for facehugger_pos in facehuggers:
        distancia = calcular_distancia(player_position, facehugger_pos)
        if distancia <= 2 and random.random() < 0.5:  # chance de um evento aleatório ocorrer      
        
            # TASK: Incorporar verificacao de salas 
            print(facehugger_approaches(corridor1, open_door, corridor_a, dark_corridor, tight_corridor, new_corridor, facehugger_is_near))
            terminal_slow("\n\n\t...  ")
            time.sleep(2)  # Pausa para aumentar a tensão



# Loop principal
while timer > 0 and integridade_nave > 0:

    print("\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n")
    draw_map()
    print(f"\n\tCombustível: {flamethrower_fuel}%\n") 

	
    # Movimentação dos Aliens
    for i in range(len(alien_positions)):
        move_direction = random.choice(["W", "A", "S", "D"])
        if move_direction == 'W' and alien_positions[i][1] > 0:
            alien_positions[i] = (alien_positions[i][0], alien_positions[i][1] - 1)
        elif move_direction == 'S' and alien_positions[i][1] < map_size[1] - 1:
            alien_positions[i] = (alien_positions[i][0], alien_positions[i][1] + 1)
        elif move_direction == 'A' and alien_positions[i][0] > 0:
            alien_positions[i] = (alien_positions[i][0] - 1, alien_positions[i][1])
        elif move_direction == 'D' and alien_positions[i][0] < map_size[0] - 1:
            alien_positions[i] = (alien_positions[i][0] + 1, alien_positions[i][1])

        if random.random() <= 0.25:  # 25% de chance de saltar casas.
            if move_direction == 'W' and alien_positions[i][1] > 1:
                alien_positions[i] = (alien_positions[i][0], alien_positions[i][1] - 2)
            elif move_direction == 'S' and alien_positions[i][1] < map_size[1] - 2:
                alien_positions[i] = (alien_positions[i][0], alien_positions[i][1] + 2)
            elif move_direction == 'A' and alien_positions[i][0] > 1:
                alien_positions[i] = (alien_positions[i][0] - 2, alien_positions[i][1])
            elif move_direction == 'D' and alien_positions[i][0] < map_size[0] - 2:
                alien_positions[i] = (alien_positions[i][0] + 2, alien_positions[i][1])

    # Movimentação dos facehuggers
    new_facehuggers = []
    for (fx, fy) in facehuggers:
        move_direction = random.choice(["W", "A", "S", "D"])
        if move_direction == 'W' and fy > 0:
            new_facehuggers.append((fx, fy - 1))
        elif move_direction == 'S' and fy < map_size[1] - 1:
            new_facehuggers.append((fx, fy + 1))
        elif move_direction == 'A' and fx > 0:
            new_facehuggers.append((fx - 1, fy))
        elif move_direction == 'D' and fx < map_size[0] - 1:
            new_facehuggers.append((fx + 1, fy))
    facehuggers = new_facehuggers  

    if timer % 80 == 0:
        facehuggers.append((random.randint(0, map_size[0] - 1), random.randint(0, map_size[1] - 1)))
        typewriter_effect_b("Alerta: Um novo organismo foi detectado na nave.\n"), time.sleep(2)
    
    # Surge um novo Alien
    if timer <= 153 and len(alien_positions) < 2:
        alien_positions.append((random.randint(0, map_size[0] - 1), random.randint(0, map_size[1] - 1)))
        typewriter_effect_b("Alerta: Um novo Alien foi detectado na nave.\n"), time.sleep(2)
    if player_position in alien_positions:
        encounter_enemy("Alien") 
    elif player_position in facehuggers:
        encounter_enemy("Facehugger")
    
    

    action = input("mover-[w/a/s/d] terminal-[e] procurar-[p] sair-[q]\n").lower()

    if action in ['w', 'a', 's', 'd']:
        x, y = player_position
        if action == 'w' and y > 0:
            player_position = (x, y - 1)
        elif action == 's' and y < map_size[1] - 1:
            player_position = (x, y + 1)
        elif action == 'a' and x > 0:
            player_position = (x - 1, y)
        elif action == 'd' and x < map_size[0] - 1:
            player_position = (x + 1, y)        
        verificar_proximidade()

    elif action == 'e':
        # Verifica se o jogador está em uma sala com terminal
        current_room = None
        for room, pos in rooms.items():
            if player_position == pos:
                current_room = room
                break

        if current_room:
            choice = terminal_interface(current_room)
            if choice == 1:
                if current_room == "Engine Room":
                    sistema_energia()
                elif current_room == "Control Room":
                    sistema_pilotagem()
                    resolver_curto_circuito()		    
                elif current_room == "Cargo Bay":
                    verificar_cargas()
                elif current_room == "Living Quarters":
                    verificar_comunicacoes()
                elif current_room == "Med Bay":
                    verificar_saude()
            elif choice == 2:
                logs_mensagens(current_room)
    
        else:
            print("\nVocê não está em uma sala com terminal.\n"), time.sleep(2)

    elif action == 'p':
        print("\nProcurando...\n")
        time.sleep(1)  # Simula uma pequena espera
        search()
 
    elif action == 'q':
        print("\nSaindo do jogo...\n"), time.sleep(2)
        break


    energy_level = max(0, energy_level - 0.1213)  # A energia diminui progressivamente ao longo do tempo

    if energy_level <= 0:
        terminal_slow("\n\n\tNível de energia em estado crítico."), time.sleep(3)
        terminal_slow("\n\n\tA nave se desativou.\n\n"), time.sleep(3)
        break
    

    # Processa eventos pendentes e gera novos eventos aleatórios
    process_pending_events()
    if random.random() < 0.03:  # chance de um evento aleatório ocorrer
        alert_event()

    timer -= 1

if integridade_nave <= 0:
    terminal_slow("\n\n\tDiversos sistemas da nave foram comprometidos."), time.sleep(3)
    terminal_slow("\n\n\tFim de jogo.\n\n"), time.sleep(3)
    
elif timer <= 0:
    terminal_slow("\n\n\tO resgate finalmente chegou!"), time.sleep(3)
    terminal_slow("\n\n\tFim de jogo.\n\n"), time.sleep(3)
