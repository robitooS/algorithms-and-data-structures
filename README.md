# Algorithms and Data Structures

Este repositório consolida uma série de implementações técnicas voltadas ao estudo aprofundado de fundamentos da ciência da computação, arquitetura de sistemas e otimização de algoritmos. O foco reside na soberania sobre conceitos de baixo nível e na aplicação de estruturas de dados eficientes para a resolução de problemas complexos.

---

## 🛠️ Escopo Técnico

O conteúdo deste repositório está segmentado em domínios críticos da engenharia de software:

### 1. Sistemas Operacionais e Interface de Baixo Nível
Desenvolvimento de ferramentas que interagem diretamente com as APIs do Kernel (como POSIX no Linux) para manipulação de sistemas de arquivos, gerenciamento de diretórios e leitura de metadados de **Inodes**.

### 2. Persistência de Dados e Segurança Binária
Implementação de fluxos de I/O (Input/Output) binários para gravação de dados em disco, integrando camadas de cifragem simétrica via operações bitwise (**XOR**) e validação de integridade por meio de algoritmos de **Checksum**.

### 3. Gerenciamento de Memória e Estratégias de Cache
Estudo de políticas de substituição de páginas e memória, com foco em **LRU (Least Recently Used)**. As implementações visam a eficiência temporal de $O(1)$ através da hibridização de estruturas como **Doubly Linked Lists** (para controle de recência) e **Hash Maps** (para acesso rápido).

### 4. Inteligência Artificial e Teoria dos Jogos
Aplicação de algoritmos de busca em espaço de estados e tomada de decisão, especificamente o algoritmo **Minimax** com otimização via **Poda Alpha-Beta**, garantindo a exploração eficiente de árvores de decisão em sistemas competitivos de soma zero.

### 5. Aritmética Computacional
Algoritmos voltados para o processamento de bases numéricas e representação de dados em nível de bit, fundamentais para a compreensão do gerenciamento de memória e protocolos de rede.

---

## 🚀 Tecnologias e Linguagens

* **C/C++**: Empregado em implementações que exigem controle determinístico de recursos, manipulação direta de ponteiros e alta performance.
* **Python**: Utilizado para modelagem de algoritmos de IA, benchmarking de performance e prototipagem rápida de estruturas de dados complexas.
