
Requisitos do Front-end para a sua Plataforma de Agendamento de Posts (Com Endpoints Backend)
O objetivo é criar uma interface funcional, intuitiva e eficiente para o uso interno, com foco na flexibilidade e automação de escala, detalhando os pontos de conexão com o backend Flask.
1. Autenticação e Autorização
Login de Usuário:
Campos para nome de usuário (ou e-mail) e senha.
Validação de credenciais no lado do cliente (básica) e no backend.
Exibição clara de mensagens de erro (ex: "Usuário ou senha inválido").
Mecanismo para persistência da sessão (tokens JWT, cookies, etc.).
Controle de Acesso:
Verificação se o usuário logado tem permissão para acessar as funcionalidades de agendamento e visualização. (Isso será mais no backend, mas o front-end deve reagir a respostas de permissão negada).
Endpoints Necessários:
POST /api/auth/login: Para autenticar o usuário. Envia credenciais (username/email, password). Recebe token de autenticação (JWT) ou cookie de sessão.
POST /api/auth/logout: Para encerrar a sessão do usuário. Invalida o token/cookie.
GET /api/auth/me: (Opcional, para verificar status da sessão) Retorna informações básicas do usuário logado.
2. Dashboard / Visão Geral
Visão Rápida:
Número de posts agendados para o dia, semana e mês.
Contagem de posts em rascunho, agendados, publicados e com erro.
Links rápidos para as principais funcionalidades (agendar novo post, agendamento em massa, ver calendário).
Endpoints Necessários:
GET /api/dashboard/summary: Retorna dados agregados para o dashboard (contagens de posts por status, agendamentos próximos).
3. Agendamento de Novo Post (Individual)
Esta funcionalidade permanece para controle granular.
Seleção de Conteúdo (Mídia):
Campo de Upload de Arquivo: Botão para selecionar um único arquivo (vídeo/imagem).
Pré-visualização: Exibição da miniatura da imagem ou do primeiro frame do vídeo após o upload.
Limitações: Indicação de tamanhos/formatos de arquivo suportados (validação final no backend).
Detalhes do Post:
Título: Campo de texto para o título do post (YouTube).
Descrição/Legenda: Campo de texto para o corpo do post, com suporte a múltiplas linhas.
Tags: Campo para inserção de tags, talvez com sugestões ou autocompletar.
Redes Sociais:
Lista de redes sociais disponíveis (YouTube, Instagram, etc.), com caixas de seleção (checkboxes).
Para cada rede selecionada, talvez campos específicos (ex: para YouTube, visibilidade Público/Privado/Não Listado).
Agendamento:
Seletor de Data: Um componente de calendário interativo para escolher a data de publicação.
Seletor de Hora: Um seletor para a hora e minuto exatos.
Fuso Horário: (Opcional, mas recomendado) Indicação clara do fuso horário usado para o agendamento.
Ações:
Botão "Agendar Post".
Botão "Salvar Rascunho" (se aplicável).
Botão "Cancelar".
Validação:
Validação em tempo real dos campos obrigatórios.
Mensagens de feedback claras sobre o sucesso ou falha do agendamento.
Endpoints Necessários:
POST /api/posts/single: Para agendar um único post.
Corpo da Requisição (FormData):
file: O arquivo de mídia (vídeo/imagem).
title: Título do post.
description: Descrição/legenda.
tags: Tags (string separada por vírgulas ou array JSON).
scheduled_at: Data e hora de agendamento (formato ISO 8601, ex: 2025-07-28T10:00:00-03:00).
social_networks: Array JSON das redes sociais (["youtube", "instagram"]).
visibility: (Opcional, para YouTube) public, private, unlisted.
Resposta: Status 201 (Created) e os detalhes do post agendado.
POST /api/posts/draft: (Opcional) Para salvar um post como rascunho. Recebe os mesmos dados, mas com status draft.
4. Agendamento de Posts em Massa
Esta é a nova e crucial funcionalidade para otimizar o processo.
Tipo de Agendamento:
Opção clara para escolher entre "Agendamento Individual" e "Agendamento em Massa".
Upload de Mídia em Massa:
Campo de Upload de Pasta/Múltiplos Arquivos: Um mecanismo para selecionar múltiplos arquivos de vídeo/imagem de uma vez (ou simular uma "pasta"). O front-end precisará lidar com o upload de vários arquivos simultaneamente ou em lote.
Lista de Arquivos Carregados: Exibição do nome e, idealmente, uma miniatura de cada arquivo carregado, para que o usuário possa ver o que foi selecionado.
Upload de Horários e Metadados:
Campo de Upload de Arquivo JSON: Botão para selecionar um arquivo .json contendo os detalhes do agendamento para cada vídeo/post.
Formato Esperado do JSON: Informar claramente o formato esperado do JSON (ex: lista de objetos, onde cada objeto tem filename, title, description, tags, schedule_time, social_networks).
JSON

[
  {
    "filename": "video1.mp4",
    "title": "Título do Vídeo 1",
    "description": "Descrição detalhada do vídeo 1.",
    "tags": "tag1, tag2",
    "schedule_time": "2025-07-28T10:00:00-03:00",
    "social_networks": ["youtube", "instagram"]
  },
  {
    "filename": "video2.mp4",
    "title": "Título do Vídeo 2",
    "description": "Descrição detalhada do vídeo 2.",
    "tags": "tag3, tag4",
    "schedule_time": "2025-07-28T14:30:00-03:00",
    "social_networks": ["youtube"]
  }
]
Validação do JSON: Realizar uma validação preliminar do JSON no front-end para garantir que o formato básico está correto antes de enviar ao backend.
Mapeamento e Pré-visualização:
Após o upload dos arquivos de mídia e do JSON, a interface deve mostrar uma pré-visualização da "fila" de agendamentos.
Tabela de Mapeamento: Uma tabela onde cada linha representa um post a ser agendado, mostrando:
Nome do Arquivo de Mídia (do upload da pasta)
Título (puxado do JSON, ou "Não definido" se não houver)
Descrição (puxado do JSON)
Data/Hora de Agendamento (puxado do JSON)
Redes Sociais (puxado do JSON)
Opção de Título Individual: Permitir que o usuário edite o título, descrição, tags e redes sociais de posts individuais diretamente nesta tabela de pré-visualização antes de finalizar o agendamento em massa. Isso oferece a flexibilidade que você mencionou.
Alertas para Mídia/JSON Não Correspondentes: Se houver arquivos de mídia sem correspondência no JSON ou entradas no JSON sem o arquivo de mídia correspondente, o sistema deve alertar o usuário.
Ações:
Botão "Processar Agendamentos em Massa".
Botão "Limpar Tudo" / "Cancelar".
Feedback de Processamento:
Mostrar o progresso do processamento dos agendamentos em massa (ex: "Processando 3/10 vídeos", "Agendamento X de Y concluído").
Exibir um resumo dos agendamentos bem-sucedidos e falhos ao final.
Endpoints Necessários:
POST /api/posts/bulk-upload-initiate: Para iniciar o processo de upload em massa.
Corpo da Requisição (FormData):
files[]: Array de arquivos de mídia (vídeos/imagens).
metadata_json: O arquivo JSON (ou o conteúdo JSON como string).
Resposta: Status 202 (Accepted) e um ID de processo/lote, ou uma lista de posts pré-validados para que o front-end possa exibir a tabela de mapeamento.
POST /api/posts/bulk-schedule: Para confirmar e agendar o lote após a pré-visualização e possíveis edições no front-end.
Corpo da Requisição (JSON):
batch_id: ID do lote retornado pela chamada bulk-upload-initiate (se houver).
posts_data: Array de objetos, cada um com os detalhes finais de um post (título, descrição, tags, scheduled_at, social_networks, e um file_id ou filename para o backend vincular ao arquivo de mídia já carregado).
Resposta: Status 200 (OK) ou 201 (Created) e um resumo dos agendamentos (sucesso/erro para cada item).
GET /api/bulk-operations/{id}/status: (Opcional, para monitorar o progresso se o agendamento for assíncrono e demorado). Retorna o status de um processo de agendamento em massa específico.
5. Calendário de Posts Agendados
Componente de Calendário:
Exibição mensal padrão, com navegação para meses anteriores e futuros.
Capacidade de alternar para visão semanal ou diária.
Marcação de Dias: Os dias com posts agendados devem ser visualmente marcados.
Eventos no Calendário:
Cada post agendado deve aparecer como um "evento" no calendário, exibindo pelo menos o título e a hora.
Cores/Ícones: Diferenciar posts por status (agendado, publicado, erro) ou por rede social (ex: ícone do YouTube ao lado do evento).
Clique no Evento: Ao clicar em um evento, exibir um pop-up ou redirecionar para uma página de detalhes/edição do post.
Filtragem e Pesquisa:
Filtros por rede social, status do post, ou campo de busca por título/descrição.
Endpoints Necessários:
GET /api/posts/calendar?start_date={YYYY-MM-DD}&end_date={YYYY-MM-DD}: Retorna uma lista de posts agendados dentro de um período específico para preencher o calendário.
Parâmetros de Query: start_date, end_date, (Opcional) social_network, status.
Resposta: Array de objetos de post, contendo id, title, scheduled_at, status, social_networks e outros dados relevantes para a exibição no calendário.
6. Lista de Posts (Tabela)
Tabela Interativa:
Colunas: Título, Redes, Data/Hora de Agendamento, Status (Agendado, Publicado, Erro, Rascunho), Data de Criação, Ações.
Ordenação: Capacidade de ordenar por qualquer coluna.
Paginação: Para grandes volumes de posts.
Pesquisa: Campo de busca global para filtrar a tabela.
Ações por Post:
Botões de "Editar", "Visualizar", "Duplicar", "Excluir" (com confirmação).
Link direto para o post no YouTube (após publicado).
Status Visual:
Indicação clara do status com cores ou ícones (ex: verde para publicado, amarelo para agendado, vermelho para erro).
Endpoints Necessários:
GET /api/posts: Retorna uma lista paginada de todos os posts.
Parâmetros de Query: page, limit, sort_by, sort_order, search_query, status, social_network.
Resposta: Objeto contendo total_posts, current_page, total_pages, e um items (array de objetos de post).
7. Detalhes e Edição do Post
Visualização Completa: Exibir todos os detalhes do post (mídia, título, descrição, tags, agendamento, status).
Histórico de Publicação: (Opcional) Data e hora exatas da publicação, URL do post, e qualquer erro ocorrido.
Edição: Capacidade de modificar título, descrição, tags, redes e, principalmente, a data/hora de agendamento (se ainda não publicado).
Salvar alterações e receber feedback de sucesso.
Endpoints Necessários:
GET /api/posts/{id}: Retorna os detalhes de um post específico.
Parâmetros de URL: id do post.
Resposta: Objeto detalhado do post.
PUT /api/posts/{id}: Para atualizar os detalhes de um post.
Parâmetros de URL: id do post.
Corpo da Requisição (JSON): Campos a serem atualizados (ex: title, description, tags, scheduled_at, social_networks, visibility).
Resposta: Status 200 (OK) e o objeto do post atualizado.
DELETE /api/posts/{id}: Para excluir um post.
Parâmetros de URL: id do post.
Resposta: Status 204 (No Content) para sucesso.
8. Interface do Usuário (UI) / Experiência do Usuário (UX)
Design Responsivo: A interface deve ser utilizável em diferentes tamanhos de tela (desktop, tablet).
Navegação Clara: Um menu lateral ou superior com links para Dashboard, Agendar Novo Post (Individual), Agendamento em Massa, Calendário, Lista de Posts, Configurações.
Feedback Visual: Carregadores (spinners) e barras de progresso para operações demoradas (especialmente no agendamento em massa), mensagens de sucesso/erro pop-up.
Consistência: Elementos de UI padronizados para botões, campos de formulário, mensagens.
Usabilidade: Fluxos de trabalho lógicos e mínimos cliques para as tarefas mais comuns.
Com esses endpoints definidos, o time de front-end terá um guia claro sobre como interagir com o seu backend Flask/Celery, garantindo uma comunicação fluida e a construção da ferramenta que você precisa.
