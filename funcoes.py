def html_para_string(caminho_do_arquivo):
  """
  Lê o conteúdo de um arquivo HTML, faz tratativas e retorna como uma string.

  Args:
    caminho_do_arquivo (str): O caminho para o arquivo HTML.

  Returns:
    str: O conteúdo do arquivo HTML como uma string.
  """
  try:
    with open(caminho_do_arquivo, 'r', encoding='utf-8') as arquivo:
      conteudo = arquivo.read()

      # Remove entidades HTML (ex.: &nbsp;)
      conteudo = html.unescape(conteudo)

      # Remove caracteres e trechos de texto desnecessários
      conteudo = conteudo.replace('\n', '')\
                         .replace('\t', '')\
                         .replace('<span style="color: #0000ff;">', '')\
                         .replace('</span>', '')

      return conteudo
  except FileNotFoundError:
    return f'Erro: Arquivo não encontrado em {caminho_do_arquivo}'
  except Exception as e:
    return f'Erro ao ler o arquivo: {e}'
