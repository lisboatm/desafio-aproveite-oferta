## README

### Descrição

Este script Python lê um número de casos de teste e, para cada caso, calcula o número total de garrafas (cheias e vazias) que um dado número de itens \( N \) pode encher, considerando que cada garrafa comporta \( K \) itens. 

### Funcionalidades

- Lê o número de casos de teste.
- Para cada caso de teste, lê dois valores \( N \) e \( K \).
- Calcula o número de garrafas cheias que podem ser preenchidas com \( N \) itens.
- Calcula o número de garrafas vazias necessárias para armazenar os itens restantes.
- Imprime o número total de garrafas (cheias e vazias).

### Requisitos

- Python 3.6 ou superior.

### Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Salve o código em um arquivo, por exemplo, `main.py`.
3. Execute o script usando o comando:

```bash
python main.py
```

4. Siga as instruções no terminal para inserir o número de casos de teste e os valores \( N \) e \( K \) para cada caso.

### Entrada

O programa solicita ao usuário que insira:

1. O número de casos de teste \( T \).
2. Para cada caso de teste, os valores \( N \) e \( K \) separados por espaço.

### Saída

Para cada caso de teste, o programa imprime o número total de garrafas (cheias e vazias).

### Exemplo de Execução

```plaintext
Digite o número de casos de teste: 2
Digite N e K separados por espaço: 6 3
2
Digite N e K separados por espaço: 7 3
3
```

### Explicação do Código

1. **Leitura do Número de Casos de Teste:**
    ```python
    T = int(input("Digite o número de casos de teste: "))
    ```

2. **Loop Através dos Casos de Teste:**
    ```python
    for _ in range(T):
        entrada = input("Digite N e K separados por espaço: ").strip()
    ```

3. **Verificação de Entrada Não Vazia:**
    ```python
    if entrada:
    ```

4. **Divisão da Entrada em Componentes \( N \) e \( K \):**
    ```python
    entrada = entrada.split()
    ```

5. **Verificação se a Entrada Contém Dois Valores:**
    ```python
    if len(entrada) >= 2:
    ```

6. **Conversão dos Valores para Inteiros:**
    ```python
    N = int(entrada[0])
    K = int(entrada[1])
    ```

7. **Cálculo das Garrafas Cheias e Vazias:**
    ```python
    garrafas_cheias = N // K
    garrafas_vazias = N % K
    ```

8. **Cálculo do Total de Garrafas:**
    ```python
    total = garrafas_cheias + (1 if garrafas_vazias > 0 else 0)
    ```

9. **Impressão do Resultado:**
    ```python
    print(total)
    ```

10. **Mensagens de Erro para Entradas Inválidas:**
    ```python
    else:
        print("Entrada inválida: menos de dois valores fornecidos.")
    else:
        print("Entrada vazia ou inválida.")
    ```

### Contribuição

Sinta-se à vontade para contribuir com melhorias no código ou na documentação, abrindo issues ou pull requests no repositório correspondente.
