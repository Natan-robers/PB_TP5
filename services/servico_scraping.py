import requests, re, pandas as pd
from bs4 import BeautifulSoup
from utils.arquivos import caminho_produtos_csv, caminho_produtos_url

def extrair_produtos_flexivel(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    
    # Tenta encontrar produtos em diferentes estruturas HTML
    produtos = []
    next_id = 1
    
    # Método 1: Busca por elementos que contêm preços
    elementos_com_preco = soup.find_all(string=re.compile(r'R\$\s*[\d\.,]+'))
    
    for elemento_preco in elementos_com_preco:
        # Pega o elemento pai que contém o preço
        parent = elemento_preco.parent
        if parent:
            # Busca o texto completo do elemento pai e seus irmãos
            texto_completo = parent.get_text(separator=" ", strip=True)
            
            # Extrai preço
            preco_match = re.search(r"R\$\s*([\d\.,]+)", texto_completo)
            if not preco_match:
                continue
            
            preco = float(preco_match.group(1).replace('.', '').replace(',', '.'))
            
            # Extrai quantidade
            quantidade = 0
            qtd_match = re.search(r"(\d+)\s*(?:un|unidade|disponível|disponivel)", texto_completo, re.IGNORECASE)
            if qtd_match:
                quantidade = int(qtd_match.group(1))
            
            # Extrai nome do produto (procura texto antes do preço)
            # Remove o preço e quantidade do texto
            texto_sem_preco = re.sub(r'R\$\s*[\d\.,]+', '', texto_completo)
            texto_sem_preco = re.sub(r'\d+\s*(?:un|unidade|disponível|disponivel)', '', texto_sem_preco, flags=re.IGNORECASE)
            
            # Encontra palavras que podem ser o nome do produto
            palavras = re.findall(r'[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ\s\-]{2,}', texto_sem_preco)
            nomes_validos = [p.strip() for p in palavras 
                           if p.strip().lower() not in ['disponível', 'disponivel', 'produto', 'un', 'unidade', 'r$'] 
                           and len(p.strip()) > 2]
            
            if nomes_validos:
                nome_produto = nomes_validos[0]
                if preco > 0:
                    produtos.append({ "id": next_id, "nome": nome_produto, "quantidade": quantidade, "preco": preco })
                    next_id += 1
    
    # Método 2: Se não encontrou nada, tenta método alternativo baseado em linhas
    if not produtos:
        textos = soup.get_text(separator="\n")
        linhas = [l.strip() for l in textos.split("\n") if l.strip()]
        
        bloco = []
        for linha in linhas:
            lower = linha.lower()
            
            # Se a linha contém preço, processa o bloco anterior
            if "r$" in lower:
                if bloco:
                    texto = " ".join(bloco)
                    # Extrai preço
                    preco_match = re.search(r"R\$\s*([\d\.,]+)", texto)
                    if preco_match:
                        preco = float(preco_match.group(1).replace('.', '').replace(',', '.'))
                        
                        # Extrai quantidade
                        quantidade = 0
                        qtd_match = re.search(r"(\d+)\s*un", texto, re.IGNORECASE)
                        if qtd_match:
                            quantidade = int(qtd_match.group(1))
                        
                        # Extrai nome
                        texto_sem_preco = re.sub(r'R\$\s*[\d\.,]+', '', texto)
                        texto_sem_preco = re.sub(r'\d+\s*un', '', texto_sem_preco, flags=re.IGNORECASE)
                        nome_match = re.findall(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ\s\-]{2,}", texto_sem_preco)
                        nomes_validos = [n.strip() for n in nome_match 
                                       if n.strip().lower() not in ['disponível', 'disponivel', 'produto', 'un', 'unidade'] 
                                       and len(n.strip()) > 2]
                        
                        if nomes_validos and preco > 0:
                            produtos.append({ "id": next_id, "nome": nomes_validos[0], "quantidade": quantidade, "preco": preco })
                            next_id += 1
                    
                    bloco = []
            else:
                # Adiciona linhas que podem conter informações do produto
                if len(linha) > 2:
                    bloco.append(linha)
    
    # Remove duplicatas baseado no nome e preço
    produtos_unicos = []
    vistos = set()
    for p in produtos:
        chave = (p['nome'].lower(), p['preco'])
        if chave not in vistos:
            vistos.add(chave)
            produtos_unicos.append(p)
    
    return produtos_unicos

def executar_scraping_e_gerar_csv():
    url = caminho_produtos_url()
    print(f"Buscando produtos em: {url}")
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        print(f"Página acessada com sucesso (status: {resp.status_code})")
    except Exception as e:
        print(f"Erro ao acessar a página: {e}")
        return pd.DataFrame()
    
    lista = extrair_produtos_flexivel(resp.text)
    print(f"Produtos extraídos: {len(lista)}")
    
    if not lista:
        print("AVISO: Nenhum produto foi extraído da página!")
        print("Tentando método alternativo de extração...")
        # Cria um CSV vazio para evitar erro na importação
        df_vazio = pd.DataFrame(columns=['id', 'nome', 'quantidade', 'preco'])
        df_vazio.to_csv(caminho_produtos_csv(), index=False)
        print("CSV vazio criado. Verifique a estrutura da página HTML.")
        return pd.DataFrame()
    
    df = pd.DataFrame(lista)
    
    # Mostra uma amostra dos produtos extraídos
    print("\nAmostra dos produtos extraídos (primeiros 3):")
    for i, produto in enumerate(lista[:3], 1):
        print(f"  {i}. ID: {produto['id']}, Nome: {produto['nome']}, "
              f"Qtd: {produto['quantidade']}, Preço: R$ {produto['preco']:.2f}")
    
    df.to_csv(caminho_produtos_csv(), index=False)
    print(f"\n{len(df)} produtos escritos em {caminho_produtos_csv()}")
    return df
