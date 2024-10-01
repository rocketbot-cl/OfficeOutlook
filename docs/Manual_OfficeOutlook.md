



# OfficeOutlook
  
Módulo para conectarse a la aplicación de escritorio de Outlook.  

*Read this in other languages: [English](Manual_OfficeOutlook.md), [Português](Manual_OfficeOutlook.pr.md), [Español](Manual_OfficeOutlook.es.md)*
  
![banner](imgs/Banner_OfficeOutlook.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este módulo
Para usar este módulo, tienes que agregar una cuenta a Outlook y luego podras conectarte correctamente.


## Descripción de los comandos

### Conectar a Outlook
  
Conectar a una instancia de la aplicación de Outlook
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Email|Opcional. Email de la cuenta de Outlook. Debe ser un correo que esté enlazado en la Aplicación de Outlook.|rocketbot@outlook.com|
|Variable donde guardar el resultado|Guardar el resultado de la conexión.|result|
|Mostrar aplicación|Este casilla permite mostrar la aplicación de Outlook. Si no está marcado, la aplicación se ejecutará en segundo plano.|True|
|Sesión de Outlook|Asigna una sesión a la conexión de Outlook.|session|

### Crear carpeta
  
Crea una carpeta en Outlook
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre carpeta|Nombre de la carpeta que se desea crear.|Nueva carpeta|
|Carpeta destino|Carpeta donde se quiere crear la nueva (opcional).|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEE4E12200|
|Asignar a variable|Guardar el resultado de la creación de la carpeta.|Variable|

### Listar Carpetas
  
Devuelve todas las carpetas
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Sesión de Outlook|Asigna una sesión a la conexión de Outlook.|session|
|Asignar resultado a variable||Variable|

### Buscar por filtro
  
Buscar correos por filtros
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro|Filtro que se desea utilizar.|(domain 'rocketbot.com' or domain 'gmail.com') and subject 'Aviso de compra'|
|Buscar en|Filtro para emails leidos, no leidos y Todos.|Todos|
|Carpeta|Carpeta en la que se desea buscar.|Inbox|
|Subcarpeta|Ruta a la subcarpeta en la que desea buscar. Para obtener la ruta a la subcarpeta, debe utilizar el módulo 'Listar carpetas'.|rocketbot@outlook.com/RocketFolder|
|Sesión de Outlook|Asigna una sesión a la conexión de Outlook.|session|
|Asignar a variable|Guardar el resultado de la búsqueda.|Variable|

### Leer email por EntryID
  
Lea la información del correo electrónico por EntryID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|EntryID|ID del email que se desea obtener.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Asignar a variable|Guardar la lectura del email.|Variable|
|Sesión de Outlook|Asigna una sesión a la conexión de Outlook.|session|
|Incluir HTML|Incluye al resultado el HTML del correo|True|
|Descargar adjuntos|Carpeta donde guardar los documentos adjuntos.|C:\User\|

### Mover email a una carpeta
  
Mueve un email hacia una carpeta por EntryID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|EntryID|ID del email que se desea mover.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Carpeta de destino|Carpeta donde se desea mover.|0014182A9615CE201001B40B98EB45D6B4A70D3F4F050000D5955FDE0000|

### Mover email a una carpeta por nombre
  
Mueve un email hacia una carpeta por Nombre (Solo carpetas dentro de la bandeja de entrada)
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|EntryID|ID del email que se desea mover.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Carpeta de destino|Carpeta donde se desea mover.|mi_carpeta|

### Marcar email como no leído
  
Marca un email como no leído por EntryID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|EntryID|ID del email que se desea marker como no leído.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|

### Enviar Email
  
Envia un email, previamente debe configurar el servidor
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Para|Email de los destinatarios.|to@mail.com, to2@mail.com|
|Copia|Email de los destinatarios.|cc@mail.com, cc2@mail.com|
|Asunto|Asunto que se desea dar.|Nuevo mail|
|Mensaje|Puedes usar html para dar estilos a tu correo. Ejemplo <b>Texto en negrita</b>. Para imagenes locales, usar <img src='ruta imagen en png'>|Esto es un mensaje de prueba|
|Archivo Adjunto|Archivo adjunto que se desea enviar.|C:\User\Desktop\test.txt|
|Carpeta (Varios archivos)|Carpeta que contiene archivos adjuntos que se desea enviar.|C:\User\Desktop\Files|
|Confirmación de lectura||True|

### Responder Email
  
Responde un email usando el Entry ID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|EntryID|ID del email que se desea responder.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Mensaje|Mesaje del mail.|Esto es una prueba|
|Archivo Adjunto|Archivo adjunto que se desea enviar.|C:\User\Desktop\test.txt|
|Carpeta (Varios archivos)|Carpeta que contiene archivos adjuntos que se desea enviar.|C:\User\Desktop\Files|
|Incluir archivos adjuntos recibidos|Incluye en la respuesta el/los archivos adjuntos recibidos en el mail.|True|

### Reenviar Email
  
Reenvia un email usando el Entry ID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|EntryID|ID del email que se desea reenviar.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Para|Email de los destinatarios.|to@mail.com, to2@mail.com|

### Guardar Email
  
Guarda un email usando el Entry ID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|EntryID|ID del email que se desea guardar.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Ruta donde guardar|Ruta en la cual se desea guardar el archivo.|C:/Users/Documents/mail.msg|

### Extraer tabla por EntryID
  
Extrae una table del correo electrónico por EntryID
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|EntryID|ID del email que se desea extraer la tabla.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Asignar a variable|Guardar el resultado de la lectura de la tabla.|Variable|

### Descargar adjuntos por EntryID
  
Descargar adjuntos por EntryID en una carpeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|EntryID|ID del email que se desea obtener.|EF000000B8EE7A4C31BD6441BF6B59D0B56B93BEC40C2000|
|Descargar adjuntos|Carpeta donde guardar los documentos adjuntos.|C:\User\|

### Leer archivo .msg
  
Leer archivo .msg y almacenar la información en una variable
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo .msg|Ruta del archivo .msg que se desea leer.|C:/Users/User/Desktop/file.msg|
|Asignar resultado a variable|Nombre de la variable donde se almacenará la información del archivo .msg.|Variable|
