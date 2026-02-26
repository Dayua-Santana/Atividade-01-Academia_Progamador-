# 🔺 Sistema de Classificação de Triângulos

## 📝 Descrição do Projeto
Este software automatiza a validação e classificação de triângulos através de uma interface gráfica simples. O objetivo é garantir que as medidas fornecidas formem um objeto geométrico válido e identificar sua categoria de forma rápida e intuitiva.

---

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python 3.x
* **Biblioteca Principal:** `PyAutoGUI` (Interface e automação)
* **Conceitos Aplicados:** Lógica de programação, Tratamento de Erros (Try/Except) e Condicionais.

---

## ⚙️ Como Instalar e Rodar
1. Clone o repositório ou baixe o arquivo `.py`.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Instale a dependência necessária via terminal:
   pip install pyautogui
   
4. Execução: No terminal, navegue até a pasta do projeto e execute o script:

Bash
python nome_do_seu_arquivo.py

## 📐 Lógica de Validação

O sistema segue um fluxo de inspeção rigoroso para garantir a precisão geométrica:

1. **Condição de Existência:**
   Antes de classificar, o script valida se a soma de dois lados é maior que o terceiro. Matematicamente:
   - `x + y > z`
   - `x + z > y`
   - `y + z > x`

2. **Critérios de Classificação (Após Aprovação):**
   - **EQUILÁTERO:** `x == y == z` (Todos os lados iguais).
   - **ISÓSCELES:** `x == y` ou `x == z` ou `y == z` (Dois lados iguais).
   - **ESCALENO:** `x != y != z` (Todos os lados diferentes).
