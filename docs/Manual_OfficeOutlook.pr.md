# OfficeOutlook
  
Connect to Outlook Desktop application.  

*Read this in other languages: [English](Manual_OfficeOutlook.md), [Portugues](Manual_OfficeOutlook.pr.md), [Español](Manual_OfficeOutlook.es.md).*
  
![banner](/docs/imgs/Banner_OfficeOutlook.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  




## Como usar este módulo
Para usar este módulo, você deve adicionar uma conta ao Outlook e, em seguida, poderá se conectar com sucesso.


## Descrição do comando

### Conecte-se ao Outlook
  
Conectar-se a uma instância do aplicativo Outlook
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Variável para salvar o resultado da conexão|Salve o resultado da conexão|result|

### Criar pasta
  
Criar uma pasta no Outlook
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da pasta|Nome da pasta que você deseja criar.|Nova pasta|
|Pasta de destino|Pasta onde você deseja criar a nova pasta (opcional).|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEE4E12200|
|Atribuir à variável|Salve o resultado da criação da pasta.|Variável|

### Pesquisar e-mail por filtro
  
Pesquisar por filtro fornecido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Filtro|Filtro que deseja usar.|(domain 'rocketbot.com' or domain 'gmail.com') and subject 'Aviso de compra'|
|Procure em|Filtre por e-mails lidos e não lidos|Todos|
|Pasta|Pasta na qual deseja pesquisar.|Inbox|
|Atribuir a variável|Salve o resultado da pesquisa.|Variável|

### Ler e-mail por EntryID
  
Ler dados de e-mail por EntryID fornecido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja obter|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Atribuir a variável|Salve o e-mail lido.|Variável|
|Baixar anexos|Caminho para a pasta onde salvar os anexos.|C:\User\|

### Mover e-mail para pasta
  
Mover dados de e-mail por EntryID fornecido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja mover.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Pasta de destino|Pasta para onde você deseja mover.|0014182A9615CE201001B40B98EB45D6B4A70D3F4F050000D5955FDE0000|

### Mover e-mail para pasta por nome
  
Mova os dados de e-mail pelo nome fornecido. (Somente pasta na caixa de entrada)
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja mover.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Pasta de destino|Pasta para onde você deseja mover.|minha_pasta|

### Marcar e-mail como não lido
  
Marcar e-mail como não lido pelo EntryID fornecido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja marcar como não lido.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|

### Enviar email
  
Envie e-mail, antes de configurar o servidor
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|To|Emails dos destinatários.|to@mail.com, to2@mail.com|
|Cc|Emails dos destinatários.|cc@mail.com, cc2@mail.com|
|Assunto|Assunto do email|Novo mail|
|Body|Mensagem do e-mail|Esta é uma mensagem de teste|
|Arquivo anexo|Arquivo anexado que você deseja enviar.|C:\User\Desktop\test.txt|
|Pasta (vários arquivos)|Pasta que contém arquivos anexados que você deseja enviar.|C:\User\Desktop\Files|
|Confirmação de leitura||True|

### Responder email
  
Responder e-mail do Entry ID
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja responder.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Mensagem|Mensagem do e-mail.|Isto é um teste|
|Arquivo anexo|Arquivo anexado com o qual você deseja enviar.|C:\User\Desktop\test.txt|
|Pasta (vários arquivos)|Pasta que contém arquivos anexados com os quais você deseja enviar.|C:\User\Desktop\Files|

### Reenviar email
  
Reenviar e-mail usando o  Entry ID
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja reenviar.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Para|Email dos destinatários.|to@mail.com, to2@mail.com|

### Salvar email
  
Salva um e-mail usando o Entry ID
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do email que você deseja salvar.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Caminho para salvar o arquivo|Caminho no qual salvar o arquivo.|C:/Users/Documents/mail.msg|

### Extrair tabela do email por EntryID
  
Extraia o conteúdo de uma tabela por e-mail EntryID fornecido
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do email que você deseja extrair da tabela.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Atribuir a variável|Salve o resultado da leitura da tabela.|Variável|

### Baixar anexos por EntryID
  
Baixar anexos por EntryID em uma pasta
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|EntryID|ID do e-mail que você deseja obter.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Baixe os anexos|Caminho para a pasta onde salvar os anexos.|C:\User\|
