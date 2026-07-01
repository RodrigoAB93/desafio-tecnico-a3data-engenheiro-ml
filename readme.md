# Extrator de Incidentes - Desafio Técnico A3Data

API REST desenvolvida em **Python** com **FastAPI** que utiliza um **Modelo de Linguagem (LLM)** executado localmente por meio do **Ollama** para extrair informações estruturadas a partir de descrições textuais de incidentes.

A aplicação recebe um relato em linguagem natural e retorna um objeto JSON estruturado contendo informações relevantes para análise e automação de processos, simulando a integração de IA em um fluxo de software real sem dependência de serviços pagos em nuvem.

## ⚙️ Funcionalidades

- Extração automática de informações utilizando LLM local (Ollama);
- API REST de alto desempenho desenvolvida com FastAPI;
- **Resolução de Datas Relativas:** Injeção dinâmica do relógio do sistema no prompt para que a IA compreenda termos como "ontem", "hoje" e "amanhã";
- Flexibilidade de payload (suporta `application/json` e texto puro `text/plain`);
- Documentação interativa via Swagger/OpenAPI customizada;
- Pipeline de pré-processamento para otimização de tokens;
- Execução totalmente isolada e local utilizando Docker;
- Retorno estruturado em formato JSON rigorosamente validado.

## 📊 Informações Extraídas

De acordo com os requisitos do desafio, a API extrai as seguintes chaves:
- **`data_ocorrencia`**: Data e hora do incidente (formato `YYYY-MM-DD HH:MM` ou `null`).
- **`local`**: Local do incidente.
- **`tipo_incidente`**: Tipo ou categoria do incidente.
- **`impacto`**: Descrição breve do impacto gerado.

---

## 🏗️ Arquitetura e Fluxo de Dados



---

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **FastAPI** (Framework Web)
- **Pydantic** (Validação de Dados)
- **Ollama** (Motor de LLM Local)
- **Docker & Docker Compose** (Containerização)
- **Pytest** (Framework de Testes Automatizados)

---

## 🚀 Pré-requisitos

Para garantir a reprodutibilidade exata do ambiente, o projeto foi containerizado. Antes de executar, certifique-se de ter instalado em sua máquina:
- **Docker**
- **Docker Compose**



## 💻 Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone [https://github.com/RodrigoAB93/desafio-tecnico-a3data-engenheiro-ml.git](https://github.com/RodrigoAB93/desafio-tecnico-a3data-engenheiro-ml.git)
cd desafio-tecnico-a3data-engenheiro-ml

```

### 2. Inicie os containers

Suba os serviços definidos no `docker-compose.yml`:

```bash
docker-compose up -d

```

### 3. Inicie o Servidor (Uvicorn)

Como o servidor ASGI roda em um processo separado, após os containers estarem ativos, execute o **Uvicorn** para iniciar a API:

```bash
 uvicorn app.main:app --reload --port 8080 
```

### 4. Baixe o modelo

Em outro terminal, baixe o modelo (`llama3`) no serviço Ollama:

```bash
docker exec -it incident-extractor-ollama-1 ollama pull llama3

```

### 5. Executando os Testes

Para rodar a suíte de testes (`pytest`) dentro do container da API:

```bash
pytest

```


### 6. Executando os Testes Automatizados

Para rodar a suíte de testes (`pytest`) dentro do container da API e garantir que tudo está funcionando corretamente:

```bash
pytest

```
---

## 📚 Documentação Interativa

Após iniciar os containers, acesse a documentação gerada automaticamente:

* **Swagger UI:** `http://localhost:8000/docs`
* **OpenAPI JSON:** `http://localhost:8000/openapi.json`

---

## 📡 Exemplo de Uso (cURL)

**Requisição (POST):**

```bash
curl -X 'POST' \
  'http://localhost:8000/api/v1/extract' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "Ontem às 14h, no escritório de São Paulo, houve uma falha no servidor principal que afetou o sistema de faturamento por 2 horas."
}'

```

**Resposta Esperada:**

```json
{
  "data_ocorrencia": "2025-08-12 14:00",
  "local": "São Paulo",
  "tipo_incidente": "Falha no servidor",
  "impacto": "Sistema de faturamento indisponível por 2 horas"
}

```

---

## 📂 Estrutura do Projeto

```text
.
├── app/             # Código fonte da aplicação
├── tests/           # Testes automatizados com Pytest
├── Dockerfile       # Configuração da imagem da API
├── docker-compose.yml # Orquestração dos serviços (incluindo Uvicorn)
└── requirements.txt # Dependências do projeto

```

## 💡 Considerações e Boas Práticas

Esta implementação foi desenhada priorizando:

* **Engenharia de Dados Aplicada:** Uso de validação estrita (Pydantic), injeção de contexto temporal e limpeza de strings, mitigando alucinações comuns de LLMs menores.
* **Isolamento de Responsabilidades:** Separação clara entre infraestrutura (API), regras de negócio (Services) e dependências externas (LLM).
* **Reprodutibilidade Total:** Configuração agnóstica de sistema operacional através do Docker, garantindo que a aplicação execute de forma idêntica em qualquer máquina.

```

```