# RESTful API com Django Rest Framework

Este é um projeto em Python desenvolvido com o Django Rest Framework, que implementa uma API RESTful para gerenciamento de brinquedos e drones. O projeto inclui autenticação via token, documentação com Swagger UI e oferece rotas para interação com dados de brinquedos, drones, pilotos e competições. Além disso, inclui uma interface gráfica para o front-end, onde os drones podem ser exibidos, além de um painel administrativo configurado para facilitar a gestão dos dados.

## 📝 Visão Geral do Projeto

 ### 💻 **Tecnologias Utilizadas**: 
   -  **Django:** Framework principal para desenvolvimento do back-end.
   - **Django REST Framework:** Usado para criar a API RESTful.
   - **drf-spectacular:** Para geração automática do esquema  OpenAPI e integração com o Swagger UI.
   - **SQLite:** Banco de dados utilizado para armazenar informações de drones, pilotos e competições.
   - **HTML/CSS:** Para criar a interface gráfica simples.

### 🚀 **Funcionalidades**:
   #### 1. **API RESTful para Gerenciamento de Drones**
A aplicação fornece uma API para gerenciar drones, suas categorias, pilotos e competições. A API foi criada usando Django REST Framework e inclui funcionalidades como:
- **Autenticação por token**: Endpoints para obter tokens de autenticação e segurança da API.
- **Esquema OpenAPI**: Documentação da API gerada automaticamente.
- **Swagger UI**: Interface gráfica para testar e visualizar os endpoints da API de maneira interativa.

#### 2. **Painel Administrativo Personalizado**
O painel administrativo do Django foi configurado para facilitar a gestão dos dados sobre drones, pilotos e competições. As principais funcionalidades incluem:
- **Listagem e Edição de Drones**: Através do painel de administração, é possível visualizar, editar e filtrar drones. A imagem do drone pode ser visualizada diretamente na interface.
- **Categorias de Drones**: Permite gerenciar as categorias dos drones.
- **Pilotos e Competições**: Gestão de pilotos, incluindo informações sobre gênero e contagem de corridas, além de detalhes das competições, como distância percorrida e datas.

#### 3. **Interface Gráfica (Front-End)**
A aplicação possui uma interface web simples que exibe os drones publicados. A página inicial foi configurada para exibir uma lista de drones filtrados por sua propriedade e status de publicação. A interface foi feita com templates do Django e serve como o front-end para os usuários interagirem com a plataforma.

## 🔗 Endpoints da API

### **Autenticação**
- `POST /api-token-auth/` - Gera um token de autenticação para usuários autenticados.

### **Drones**
- `GET /api/drones/`: Retorna uma lista de drones.
- `POST /api/drones/`: Cria um novo drone.
- `GET /api/drones/{id}/`: Retorna os detalhes de um drone específico.
- `PUT /api/drones/{id}/`: Atualiza as informações de um drone.
- `DELETE /api/drones/{id}/`: Exclui um drone.

### **Pilotos**
- `GET /api/pilots/`: Retorna uma lista de pilotos.
- `POST /api/pilots/`: Cria um novo piloto.
- `GET /api/pilots/{id}/`: Retorna os detalhes de um piloto específico.

### **Competições**
- `GET /api/competitions/`: Retorna uma lista de competições.
- `POST /api/competitions/`: Cria uma nova competição.
- `GET /api/competitions/{id}/`: Retorna os detalhes de uma competição específica.


### **Documentação da API**
- **Esquema OpenAPI**: `/api/schema/`
- **Swagger UI**: `/api/docs/` - Interface gráfica para explorar a documentação da API

## 📂 Estrutura do Projeto

```
restful01/
├── drones/
│   ├── migrations/          # Arquivos de migração do banco de dados
│   ├── drones_images/       # Pasta para uploads de imagens de drones
│   ├── admin.py             # Configurações do Django Admin para a app drones
│   ├── apps.py              # Configurações gerais da app drones
│   ├── models.py            # Definição de modelos (tabelas do banco de dados)
│   ├── views.py             # Lógica de negócio e endpoints
│   ├── serializers.py       # Serialização de dados para JSON
│   ├── urls.py              # Rotas/endpoints
│   ├── filters.py           # Configurações para filtrar dados da API
│   ├── pagination.py        # Configurações de paginação
│   └── tests.py             # Testes automatizados
├── home/
│   ├── templates/home/      # Arquivos HTML da interface web
│   │   └── index.html       # Página inicial do projeto
│   ├── models.py            # Modelos relacionados à página inicial (se aplicável)
│   ├── urls.py              # Rotas para a interface web
│   └── views.py             # Lógica para renderização da página inicial
├── toys/                    # Aplicação para gerenciamento de brinquedos
├── media/                   # Pasta para armazenamento de arquivos de mídia
├── db.sqlite3               # Banco de dados SQLite (padrão do Django)
├── manage.py                # Arquivo principal para gerenciar o projeto Django
├── pytest.ini               # Configurações para testes automatizados
├── requirements.txt         # Arquivo com as dependências do projeto
```

## 🛠️ Instalação e Configuração

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/alan-nunes/restful01.git
   cd restful01
   ```

2. **Crie e ative o ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados**:
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário** para acessar o painel administrativo:
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

Acesse a API localmente em [http://127.0.0.1:8000](http://127.0.0.1:8000).



## 💬 Contato

Para mais informações, você pode me encontrar no LinkedIn:

- [Alan Nunes](https://www.linkedin.com/in/alan-sn/)

---

Sinta-se à vontade para contribuir com sugestões, melhorias e relatórios de problemas!
