# RESTful API com Django Rest Framework

Este é um projeto em Python desenvolvido com o Django Rest Framework, que implementa uma API RESTful para gerenciamento de brinquedos e drones. O projeto inclui autenticação via token, documentação com Swagger UI e oferece rotas para interação com dados de brinquedos, drones, pilotos e competições.

## Visão Geral do Projeto

- **Tecnologias Utilizadas**: Python, Django, Django Rest Framework
- **Funcionalidades**:
  - CRUD de brinquedos e drones
  - Autenticação via token
  - Documentação da API com Swagger
  - Organização modular para diferentes entidades como brinquedos, drones, pilotos e competições

### Repositório

O código fonte deste projeto está disponível no GitHub:
[Alan Nunes - Projeto RESTful01](https://github.com/alan-nunes/restful01)

## Funcionalidades

### Autenticação
- **Rota**: `/api-token-auth/` - Gera um token de autenticação para usuários autenticados.

### Endpoints para Brinquedos
- `GET /toys/` - Lista todos os brinquedos
- `GET /toys/<int:pk>/` - Detalhes de um brinquedo específico
- `POST /toys/` - Cria um novo brinquedo
- `PUT /toys/<int:pk>/` - Atualiza um brinquedo específico
- `DELETE /toys/<int:pk>/` - Deleta um brinquedo específico

### Endpoints para Drones e Pilotos
- `GET /drones/` - Lista todos os drones
- `GET /drones/<int:pk>/` - Detalhes de um drone específico
- `GET /pilots/` - Lista todos os pilotos
- `GET /pilots/<int:pk>/` - Detalhes de um piloto específico
- `GET /competition/` - Lista todas as competições
- `GET /competition/<int:pk>/` - Detalhes de uma competição específica

### Documentação da API
- **Esquema OpenAPI**: `/api/schema/`
- **Swagger UI**: `/api/docs/` - Interface gráfica para explorar a documentação da API

## Instalação e Configuração

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

## Rotas Principais

O arquivo `urls.py` do projeto principal contém as rotas gerais, incluindo autenticação e documentação da API:

```python
urlpatterns = [
    path("api-token-auth/", views.obtain_auth_token, name="api-token-auth"),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path('admin/', admin.site.urls),
    path('', include('toys.urls')),
    path("api/", include("drones.urls")),
    path("auth/", include("rest_framework.urls")),
]
```

### Rotas do Aplicativo Drones

```python
urlpatterns = [
    path("", include(router.urls)),
    path("", views.ApiRoot.as_view(), name=views.ApiRoot.name),  
    path("drones/", views.DroneList.as_view(), name=views.DroneList.name),
    path("drones/<int:pk>/", views.DroneDetail.as_view(), name=views.DroneDetail.name),
    path("pilots/", views.PilotList.as_view(), name=views.PilotList.name),
    path("pilots/<int:pk>/", views.PilotDetail.as_view(), name=views.PilotDetail.name),
    path("competition/", views.CompetitionList.as_view(), name= views.CompetitionList.name),
    path("competition/<int:pk>/", views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),  
]
```

### Rotas do Aplicativo Toys

```python
urlpatterns = [
    path('toys/', views.toy_list),
    path('toys/<int:pk>', views.toy_detail),
]
```

## Contato

Para mais informações, você pode me encontrar no LinkedIn:

- [Alan Nunes](https://www.linkedin.com/in/alan-sn/)

---

Sinta-se à vontade para contribuir com sugestões, melhorias e relatórios de problemas!
