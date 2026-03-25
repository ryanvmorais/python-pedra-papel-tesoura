![Jogo da Velha em Python - Lógica de Programação e Matrizes](https://github.com/ryanvmorais/python-pedra-papel-tesoura/blob/main/assets/pedra-papel-tesoura-python-logica-programacao.png?raw=true)

# 🪨📜✂️ Pedra, Papel e Tesoura em Python | Exercício de Lógica de Programação

Este repositório contém o clássico jogo **Pedra, Papel e Tesoura (Jokenpô)** desenvolvido em Python, projetado especificamente como um material de estudo para desenvolvedores iniciantes. O foco principal é a aplicação prática de **fundamentos da programação** e o uso de dicionários para mapear regras de negócio no terminal.

### 🎯 Objetivo do Projeto:
Demonstrar a aplicação de **estruturas de repetição**, **manipulação de coleções (listas e dicionários)** e **Programação Orientada a Objetos (POO)** em Python. É um projeto prático ideal para estudantes que desejam entender como transformar regras do mundo real em algoritmos eficientes.

---

### 📚 O que você vai aprender com este projeto?
Este exercício foi estruturado para consolidar conceitos essenciais de algoritmos:

*   **Estruturas de Repetição:** Controle do fluxo contínuo de rodadas (Loop `while`).
*   **Dicionários (Mapping):** Como substituir múltiplos `if/else` por um mapeamento lógico de vitória (`chave` vence `valor`).
*   **Tratamento de Erros:** Uso de blocos `try/except` para validar entradas numéricas do usuário.
*   **POO (Orientada a Objetos):** Organização de código modular através da classe `PedraPapelTesoura` e uso do `self`.
*   **Interação Multiplataforma com o SO:** Uso do módulo `subprocess` para detectar o sistema operacional (`cls` no Windows ou `clear` em Unix/Mac) e manter a interface do terminal limpa e profissional.

---
### 🧠 Guia de Implementação: A Lógica por trás do Código
Para quem está começando, o maior desafio não é a sintaxe, mas a **montagem do raciocínio**. Confira o passo a passo da construção deste jogo:
1. **Facilitando a Escolha (Listas e Índices):** Em vez de pedir para o usuário digitar "pedra" (e correr o risco dele errar uma letra e o código travar), nós usamos uma lista: `['pedra', 'papel', 'tesoura']`. O usuário só digita o número (0, 1 ou 2). O Python entende que o número 0 é a Pedra, o 1 é o Papel e o 2 é a Tesoura. Isso evita erros e deixa o jogo mais rápido.
2. **O "Truque" do Dicionário (Regras de Vitória):** Sabe aquele monte de `if` e `else` que a gente costuma fazer? Aqui nós usamos um **Dicionário**. É como uma tabela: a gente diz que a Pedra vence a Tesoura, o Papel vence a Pedra, e assim por diante. O código só precisa olhar essa "tabela" para saber quem ganhou. É muito mais limpo e fácil de ler!.
3. **Organizando a Casa (Classes e o tal do `self`):** Usamos uma **Classe** chamada `PedraPapelTesoura`. Pense nela como uma caixa que guarda tudo o que o jogo precisa: o placar, as regras e as jogadas. O `self` serve para o jogo saber que ele está mexendo no seu *próprio* placar e não em algo de fora. Isso evita aquela bagunça de variáveis espalhadas pelo código.
4. **O Coração do Jogo (Game Loop):** O jogo roda dentro de um "laço" (*loop*) que não para até você pedir. Ele segue sempre essa ordem: `Limpa a tela` -> `Pede sua jogada` -> `Sorteia a jogada do computador` -> `Mostra quem venceu` -> `Pergunta se quer jogar de novo`. É assim que quase todo jogo funciona!.
5. **Conversando com o seu Computador:** Usamos um comando especial (`subprocess`) para falar com o sistema operacional (`Windows`, `Mac` ou `Linux`). Ele descobre qual sistema você usa e limpa a tela do terminal automaticamente, deixando o jogo com uma aparência muito mais bonita e organizada.
6. **Proteção contra Erros (Try/Except):** E se o jogo pedir um número e o usuário digitar uma letra? Normalmente o programa fecharia com um erro feio. Aqui, usamos o `try/except`, que "tenta" fazer algo e, se der erro, ele avisa o usuário educadamente em vez de travar tudo.

---

### 🛠️ Tecnologias e Ferramentas:
Para garantir a melhor experiência de aprendizado e a execução correta de todos os recursos (como a limpeza de tela automática), o projeto utiliza as seguintes tecnologias:


| Ferramenta | Descrição | Badge |
| :--- | :--- | :--- |
| **Python 3** | Linguagem principal utilizada no desenvolvimento do algoritmo. | ![Linguagem Python](https://img.shields.io/badge/-Python-3776AB%3Fstyle%3Dflat%26logo%3Dpython?logo=python&logoColor=3776AB&logoSize=flat&color=F0F0F0) |
| **Terminal** | Interface onde o jogo é executado e processa as entradas do usuário. | ![Terminal](https://img.shields.io/badge/Terminal-241F31?style=flat&logo=gnometerminal&logoColor=241F31&color=F0F0F0) |
| **VS Code / PyCharm** | IDEs recomendadas para edição, depuração e refatoração do arquivo `main.py`. | ![PyCharm](https://img.shields.io/badge/PyCharm-pycharm?style=flat&logo=pycharm&logoColor=000000&color=F0F0F0) |

---

### ✅ Requisitos Mínimos:

Para garantir que o jogo funcione corretamente, certifique-se de ter os seguintes itens instalados:

- **Python 3.10 ou superior:** O código utiliza recursos modernos da linguagem.
- **VS Code / PyCharm (Opcional):** Recomendado para abrir e editar o arquivo `main.py` com suporte total a refatoração e depuração.

> **Dica:** Para verificar sua versão do Python, digite `python --version` no seu terminal.

---

### ⚙️ Como Executar o Projeto:
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/ryanvmorais/python-pedra-papel-tesoura.git
   ``` 
2. **Execute o script:**
- Navegue até a **pasta do projeto** e utilize o comando abaixo no seu terminal (CMD, PowerShell ou Terminal do VS Code/PyCharm):
   ```bash
   python main.py
   ```
> **Nota:** O jogo detectará automaticamente se você está no `Windows`, `Linux` ou `macOS` para gerenciar a limpeza da tela.
---
### ▶️ Execução Simplificada (Atalhos):
Para facilitar o acesso de quem está começando, adicionei scripts de inicialização automática. Basta baixar o projeto e:
   * **No Windows:** Dê dois cliques no arquivo `iniciar_jogo.bat`.
   * **No Linux/macOS:** Execute o arquivo `iniciar_jogo.sh` no terminal.

*Esses scripts verificam automaticamente se você tem o Python instalado antes de iniciar a partida.*

---
### 📋 Atividade para praticar:

Para exercitar o que aprendeu, tente modificar o código e implementar estas novas funcionalidades:

1. **🏆  Placar Acumulado (Gerenciamento de Estado):**

O desafio é criar um contador que não zere ao reiniciar uma partida.
   * **O Conceito:** Aprenda a diferenciar variáveis que controlam a **rodada atual** das que controlam o **histórico global do usuário**.
   * **A Lógica:**  Implemente variáveis de controle (ex: `pontos_usuario` e `pontos_computador`) dentro do método `__init__` da classe. Garanta que, ao reiniciar o loop de jogadas, essas variáveis persistam e sejam exibidas no placar a cada novo turno.
   * **O Aprendizado:** Você entenderá como manter dados consistentes e estados de memória em aplicações que possuem múltiplos ciclos de execução (Game Loops).

2. **🤖 Modo "Melhor de 3":** Tente fazer o jogo encerrar e declarar um Grande Campeão assim que o usuário ou o computador atingir 2 vitórias.
3. **⏲️ Efeito de Suspense:** Utilize o módulo `time` e a função `time.sleep(1)` para exibir "Pedra...", "Papel..." e "Tesoura!" com pausas antes de revelar a jogada da máquina.

---

### 💡 Ficou com alguma dúvida ou tem sugestões?

Aprender algo novo tem seus desafios, mas estou aqui para caminharmos juntos! Se você encontrou algum erro, teve dificuldade em rodar o jogo ou pensou em uma funcionalidade incrível para adicionar:

*   **Abra uma [Issue](https://github.com/ryanvmorais/python-pedra-papel-tesoura/issues):** Clique no link e descreva sua dúvida ou sugestão. É a melhor forma de trocarmos conhecimento e ajudarmos outras pessoas que tenham a mesma dúvida!
*   **Me mande um E-mail:** Se preferir algo mais privado, pode me escrever em [**contato@ryanmorais.com.br**](mailto:contato@ryanmorais.com.br).

Ficarei muito feliz em ver seu progresso e receber seu feedback para melhorar cada vez mais nossos materiais de estudo! 🤝

---

### ⚖️ Licença

Este projeto está sob a **Licença MIT**. Isso significa que você pode usar, copiar e modificar o código à vontade, inclusive para seus próprios projetos, desde que mantenha os créditos originais. Para mais detalhes, consulte o arquivo [LICENSE](LICENSE).
