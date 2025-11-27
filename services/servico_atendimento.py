import pandas as pd
from data.repositorio_cliente import obter_cliente_por_id, salvar_cliente
from data.repositorio_produto import decrementar_estoque
from data.repositorio_compra import criar_compra, adicionar_item_compra
from views.interface_console import solicitar_id_cliente, solicitar_id_produto_e_quantidade, exibir_nota_fiscal

def processar_atendimento_loop():
    while True:
        try:
            abrir = input("Deseja iniciar um atendimento? [s/n]: ").strip().lower()
            if abrir != 's':
                break
        except KeyboardInterrupt:
            print('\n\nOperação cancelada pelo usuário.')
            break
        
        try:
            cid = solicitar_id_cliente()
            cliente = obter_cliente_por_id(int(cid))
            if not cliente:
                novo_id = salvar_cliente()
                cid = novo_id
                print(f'Cliente cadastrado com id {novo_id}')
                cliente = obter_cliente_por_id(novo_id)
            else:
                cid = int(cid)

            id_compra = criar_compra(cid)
            print(f'Compra {id_compra} iniciada.')

            carrinho = []
            while True:
                try:
                    item = solicitar_id_produto_e_quantidade()
                    if item is None:
                        break
                    carrinho.append(item)
                except KeyboardInterrupt:
                    print('\n\nOperação cancelada pelo usuário.')
                    break

            if not carrinho:
                print('Atendimento cancelado (nenhum item).')
                continue

            df = pd.DataFrame(carrinho)
            grouped = df.groupby(['id','nome','preco'], as_index=False).agg({'quantidade':'sum'})
            grouped['total'] = grouped['quantidade'] * grouped['preco']

            exibir_nota_fiscal(grouped, cliente)

            for _, row in grouped.iterrows():
                id_produto = int(row['id'])
                quantidade = int(row['quantidade'])
                preco = float(row['preco'])
                adicionar_item_compra(id_compra, id_produto, quantidade, preco)
                decrementar_estoque(id_produto, quantidade)

            print(f'Compra {id_compra} registrada. Estoque atualizado e atendimento finalizado.')
        except KeyboardInterrupt:
            print('\n\nOperação cancelada pelo usuário.')
            break
        except Exception as e:
            print(f'\nErro durante o atendimento: {e}')
            continue
