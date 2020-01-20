# [RCTECH] Seleção - Dev Full Stack

Repositório para guardar o código do desafio realizado pela RCTECH a fim de avaliar para contratação.

### Como será o sistema:
- Inicialmente não vai haver nenhum tipo de login no sistema, nem nenhuma tela de administração;
- O primeiro portal que será integrado será o do [Tecmundo](https://www.tecmundo.com.br/), trazendo para o banco de dados somente o título das notícias que aparecem em destaque no inicio da página;
- O sistema deve possuir um banco de dados próprio que guarda as notícias dos outros portais;
- O sistema deve apresentar apenas uma tela com as notícias já capturadas com um filtro geral de pesquisa pelo título, de tal forma que seja possível pesquisar por notícias dentro do portal.

### Requisitos do sistema:
- Precisa ser implementado em Django usando Python 3;
- Precisa ter um arquivo requirements.txt com as dependências do projeto;
- Deve ser criado um django command chamado "capturar_noticias", de tal forma que para alimentar o banco de dados com as notícias dos portais basta rodar o comando "./manage.py capturar_noticias";
- O banco de dados deve ser o sqlite 3.

### Agradecimentos
- Adriano Petrovich e equipe RCTECH pela elaboração do desafio.
- Documentação do Django para solucionar dúvidas
- Cursos da [DevMedia](https://www.devmedia.com.br/) para guiar os passos iniciais com o Django
- Site [SimpleIsBetterThanComplex](https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html)
- Site [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3)
