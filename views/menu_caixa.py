def menu_abrir_caixa():
    print("\n--- MENU CAIXA ---\n")
    while True:
        try:
            opc = input("Deseja abrir o caixa? [s/n]: ").strip().lower()
            if opc in ('s','n'):
                return opc == 's'
            print('Opção inválida. Digite s ou n.')
        except KeyboardInterrupt:
            print('\n\nOperação cancelada pelo usuário.')
            return False
