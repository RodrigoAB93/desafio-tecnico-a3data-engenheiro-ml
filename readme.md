# Extrator de Incidentes (Incident Extractor)

API REST desenvolvida em **Python** com **FastAPI** que utiliza um **Modelo de Linguagem de Grande Escala (LLM)** executado localmente por meio do **Ollama** para extrair informações estruturadas a partir de descrições textuais de incidentes de TI.

A aplicação recebe um relatório em linguagem natural e retorna um objeto JSON contendo informações relevantes para análise e automação de processos.

## Funcionalidades

- Extração automática de informações utilizando LLM local;
- API REST desenvolvida com FastAPI;
- Documentação interativa via Swagger/OpenAPI;
- Execução totalmente local utilizando Docker e Ollama;
- Pipeline de pré-processamento para normalização da entrada;
- Retorno estruturado em formato JSON.

## Informações extraídas

- Tipo do incidente
- Gravidade
- Resumo
- Entidades envolvidas

---

# Arquitetura

```text
Cliente
    │
    ▼
FastAPI (API REST)
    │
    ▼
Pré-processamento
    │
    ▼
Construção do Prompt
    │
    ▼
Ollama (LLM Local)
    │
    ▼
Validação da Resposta
    │
    ▼
JSON Estruturado
```

---

# Pipeline de processamento

Antes do envio ao Modelo de Linguagem (LLM), o texto informado pelo usuário passa por um pipeline simples de pré-processamento para aumentar a consistência da entrada.

As etapas realizadas incluem:

- Remoção de espaços em branco excedentes;
- Normalização de quebras de linha;
- Limpeza de caracteres desnecessários;
- Preparação do texto para composição do prompt enviado ao modelo.

Após o pré-processamento, o texto é incorporado ao prompt e enviado ao LLM executado localmente pelo Ollama. A resposta retornada é validada e convertida para o formato JSON esperado pela API.

---

# Tecnologias

- Python 3.12
- FastAPI
- Ollama
- Docker
- Docker Compose
- Pydantic

---

# Pré-requisitos

Antes de executar o projeto é necessário possuir instalado:

- Docker
- Docker Compose

---

# Como executar

## 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/desafio-tecnico-a3data-engenheiro-ml.git

cd desafio-tecnico-a3data-engenheiro-ml
```

## 2. Inicie os containers

```bash
docker-compose up -d
```

## 3. Baixe o modelo utilizado

O Ollama inicia sem modelos instalados. Para baixar o modelo padrão execute:

```bash
docker exec -it incident-extractor-ollama-1 ollama pull llama3
```

> Aguarde a conclusão do download antes de utilizar a API.

Caso deseje, outro modelo compatível com o Ollama pode ser utilizado mediante alteração da configuração da aplicação.

---

# Documentação

Após iniciar a aplicação, acesse:

### Swagger UI

```
http://localhost:8000/docs
```

### OpenAPI

```
http://localhost:8000/openapi.json
```

---

# Exemplo de requisição

```bash
curl -X POST "http://localhost:8000/api/v1/extract" \
-H "Content-Type: application/json" \
-d '{
  "text": "Às 3h45 da manhã, o servidor de banco de dados primário (192.168.1.50) sofreu um pico massivo no uso de CPU, fazendo com que o serviço de gateway de pagamento ficasse offline por 45 minutos."
}'
```

---

# Exemplo de resposta

```json
{
  "incident_type": "Falha de infraestrutura",
  "severity": "Alta",
  "summary": "Servidor de banco de dados apresentou pico de CPU, causando indisponibilidade do gateway de pagamento por 45 minutos.",
  "entities": [
    "Servidor de banco de dados primário",
    "192.168.1.50",
    "Gateway de pagamento"
  ]
}
```

---

# Estrutura do projeto

```text
.
├── app
├── api
├── llm
├── services
├── models
├── utils
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Organização da aplicação

A solução foi organizada em módulos independentes, cada um responsável por uma etapa do processamento.

| Módulo | Responsabilidade |
|---------|------------------|
| `api` | Endpoints da API REST e tratamento das requisições HTTP. |
| `services` | Orquestração do fluxo de processamento da aplicação. |
| `llm` | Comunicação com o modelo local executado pelo Ollama e construção dos prompts. |
| `models` | Definição e validação dos modelos de entrada e saída da API. |
| `utils` | Funções auxiliares, incluindo o pipeline de pré-processamento do texto. |

Essa organização facilita a manutenção do código, a realização de testes e a evolução da aplicação.

---

# Considerações

Esta implementação foi desenvolvida com foco nos critérios propostos para o desafio técnico, priorizando:

- Boas práticas de desenvolvimento em Python;
- Organização e separação de responsabilidades;
- Utilização de um LLM executado localmente, sem dependências de serviços em nuvem;
- Pipeline simples de pré-processamento para melhoria da consistência das entradas;
- Facilidade de reprodução do ambiente por meio do Docker;
- Código modular, legível e de fácil manutenção.

---

# Possíveis melhorias

Como evolução da solução, podem ser adicionadas funcionalidades como:

- Suporte a múltiplos modelos do Ollama;
- Monitoramento e observabilidade da aplicação;
- Cache de respostas do modelo;
- Autenticação e autorização da API;
- Testes automatizados;
- Pipeline de Integração Contínua (CI/CD);
- Estratégias de recuperação para respostas inválidas do LLM.