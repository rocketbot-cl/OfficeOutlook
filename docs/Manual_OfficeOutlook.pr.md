



# OfficeOutlook
  
Módulo para conectar-se ao aplicativo de desktop do Outlook.  

*Read this in other languages: [English](Manual_OfficeOutlook.md), [Português](Manual_OfficeOutlook.pr.md), [Español](Manual_OfficeOutlook.es.md)*
  
![banner](imgs/Banner_OfficeOutlook.png)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  



## Como usar este módulo
Para usar este módulo, você deve adicionar uma conta ao Outlook e, em seguida, poderá se conectar com sucesso.


## Descrição do comando

### Conecte-se ao Outlook
  
Conectar-se a uma instância do aplicativo Outlook
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Email|Opcional. Email da conta do Outlook. Deve ser um e-mail que esteja vinculado no aplicativo Outlook.|rocketbot@outlook.com|
|Variável para salvar o resultado da conexão|Salve o resultado da conexão|result|
|Mostrar aplicativo|Esta caixa de seleção permite que você mostre o aplicativo Outlook. Se não estiver marcado, o aplicativo será executado em segundo plano.|True|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|

### Criar pasta
  
Criar uma pasta no Outlook
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da pasta|Nome da pasta que você deseja criar.|Nova pasta|
|Pasta de destino|Pasta onde você deseja criar a nova pasta (opcional).|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEE4E12200|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|
|Atribuir à variável|Salve o resultado da criação da pasta.|Variável|

### Listar Pastas
  
Devolve todas as pastas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|
|Salve o resultado da pesquisa||Variable|

### Pesquisar e-mail por filtro
  
Pesquisar por filtro fornecido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Filtro|Filtro que deseja usar.|(domain 'rocketbot.com' or domain 'gmail.com') and subject 'Aviso de compra'|
|Procure em|Filtrar por e-mails lidos, não lidos e todos.|Todos|
|Pasta|Pasta na qual deseja pesquisar.|Inbox|
|Subpasta|Caminho para a subpasta que deseja pesquisar. Para obter o caminho para a subpasta, você deve usar o módulo 'Listar pastas'.|rocketbot@outlook.com/RocketFolder|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|
|Atribuir a variável|Salve o resultado da pesquisa.|Variável|

### Ler e-mail por EntryID
  
Ler dados de e-mail por EntryID fornecido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja obter|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Atribuir a variável|Salve o e-mail lido.|Variável|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|
|Incluir HTML|Inclua o HTML do e-mail no resultado.|True|
|Baixar anexos|Caminho para a pasta onde salvar os anexos.|C:\User\|

### Mover e-mail para pasta
  
Mover dados de e-mail por EntryID fornecido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja mover.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Pasta de destino|Pasta para onde você deseja mover.|0014182A9615CE201001B40B98EB45D6B4A70D3F4F050000D5955FDE0000|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|

### Mover e-mail para pasta por nome
  
Mova os dados de e-mail pelo nome fornecido. (Somente pasta na caixa de entrada)
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja mover.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Pasta de destino|Pasta para onde você deseja mover.|minha_pasta|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|

### Marcar e-mail como não lido
  
Marcar e-mail como não lido pelo EntryID fornecido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja marcar como não lido.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|

### Enviar email
  
Envie e-mail, antes de configurar o servidor
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|To|Emails dos destinatários.|to@mail.com, to2@mail.com|
|Cc|Emails dos destinatários.|cc@mail.com, cc2@mail.com|
|Assunto|Assunto do email|Novo mail|
|Body|Você pode usar html para estilizar seu e-mail. Exemplo <b>Texto em negrito</b>. Para imagens locais, use <img src='caminho da imagem png'>|Esta é uma mensagem de teste|
|Arquivo anexo|Arquivo anexado que você deseja enviar.|C:\User\Desktop\test.txt|
|Pasta (vários arquivos)|Pasta que contém arquivos anexados que você deseja enviar.|C:\User\Desktop\Files|
|Confirmação de leitura||True|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|

### Responder email
  
Responder e-mail do Entry ID
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja responder.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Mensagem|Mensagem do e-mail.|Isto é um teste|
|Arquivo anexo|Arquivo anexado com o qual você deseja enviar.|C:\User\Desktop\test.txt|
|Pasta (vários arquivos)|Pasta que contém arquivos anexados com os quais você deseja enviar.|C:\User\Desktop\Files|
|Incluir arquivos anexados recebidos|Inclua os anexos recebidos no e-mail na resposta.|True|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|

### Reenviar email
  
Reenviar e-mail usando o  Entry ID
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja reenviar.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Para|Email dos destinatários.|to@mail.com, to2@mail.com|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|

### Salvar email
  
Salva um e-mail usando o Entry ID
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do email que você deseja salvar.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Caminho para salvar o arquivo|Caminho no qual salvar o arquivo.|C:/Users/Documents/mail.msg|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|

### Extrair tabela do email por EntryID
  
Extraia o conteúdo de uma tabela por e-mail EntryID fornecido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do email que você deseja extrair da tabela.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|
|Atribuir a variável|Salve o resultado da leitura da tabela.|Variável|

### Baixar anexos por EntryID
  
Baixar anexos por EntryID em uma pasta
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja obter.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Baixe os anexos|Caminho para a pasta onde salvar os anexos.|C:\User\|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|

### Leia o arquivo .msg
  
Leia o arquivo .msg e armazene as informações em uma variável
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho para o arquivo .msg|Caminho do arquivo .msg que você deseja ler.|C:/Users/User/Desktop/file.msg|
|Sessão do Outlook|Atribua uma sessão à conexão do Outlook|session|
|Atribuir resultado à variável|Nome da variável onde as informações do arquivo .msg serão armazenadas.|Variável|
