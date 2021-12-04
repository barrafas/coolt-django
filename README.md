# coolt-django
Transição do projeto presente no repositório https://github.com/adamesalles/shelf-lp para plataforma Django. *Atenção*: as análises exploratórias estão disponíveis a partir da página _Sobre_, no nome de cada um. 

# Coolt

Conheça o Coolt: o melhor site de estante de mídias! Organize seus interesses, receba recomendações personalizadas e faça resenhas, relacionando todos os tipos de entretenimento de seu interesse! O Tako, nosso mascote, está aqui para ajudar!

O site conta com suporte para 5 tipos de mídia: Animes, Filmes, Livros, Jogos e Séries.


## Página de Login
Página de entrada do Coolt, onde é possível conhecer melhor o site, buscando atrair mais usuários. Contém uso de tag e filter random no nav.

Partes funcionais:
* Login, que leva à página _home_
* Footer, leva ao repositório do GitHub

## Home
Página central, que tem um carrosel de imagem única com as novidades da semana, carrosséis múltiplos com recomendações e obras em alta.

Partes funcionais:
* Barra de navegação (comum a todas as páginas internas): 
	* Logo do Coolt, retorna à Home
	* Minha Estante, leva ao perfil unificado com a estante
	* Explorar, dropdown com todos os tipos de obra, levando às páginas de exploração de cada um
	* Sair, leva à página de login
* Ícone da série How I Met Your Mother, primeira do "Em Alta", que leva à página da obra
* Footer, adição do Sobre, que leva à página de informações

## Sobre
Página de informações sobre o Coolt, trazendo planos e ideais do site. Além disso, tem informações sobre a equipe. 

A partir do nome de cada integrante, é possível acessar sua análise exploratória com a pergunta de negócio.

Partes funcionais:
* Barra de navegação
* Footer

## Minha Estante
Página do usuário, trazendo à esquerda usuário e informações sobre ele, seus gêneros favoritos, estatísticas do consumo e amigos, que nessa página são, em maioria, pessoas legais!
Além disso, contém a própria estante do usuário, com filtros por tipo de mídia.

Partes funcionais:
* Barra de navegação
* Footer
* Botões de filtro por tipo de obra, cumulativos, para possibilitar a visualização plena do que o usuário busca

## Páginas de exploração por mídia
Acessíveis através do dropdown Explorar, cada uma tem as obras em alta e carrosséis múltiplos em diferentes categorias povoadas com obras incríveis! São elas de Animes, Filmes, Livros, Jogos e Séries.

Partes funcionais:
* Barra de navegação
* Footer
* Gêneros, dropdown com gêneros específicos de cada tipo de obra
* Na página de séries é possivel acessar o ícone da série How I Met Your Mother, primeira do "Em Alta", que leva à página da obra

## Página da obra
Exemplo de obra, nesse caso de How I Met Your Mother, que tem a nota geral da obra e a nota atribuída pelo usuário, com os gêneros dela, barra de progresso do usuário e sugestões de obras semelhantes. Além disso, traz a sinopse da obra e resenhas em alta elaboradas por outros usuários. 

Partes funcionais:
* Barra de navegação
* Footer
* Ver mais, retorna ao topo

## Erro 404
Acessível a partir de qualquer botão não acessível no site

## Base de dados

Elaborada principalmente a partir de web scrapping (filmes, séries, animes) e arquivos csv nos casos em que não havia APIs satisfatórias (livros e jogos):
 * https://www.themoviedb.org/ - Filmes e séries
 * https://myanimelist.net/ - Animes
 * https://www.kaggle.com/nikdavis/steam-store-games/version/3 - Jogos
 * https://data.world/yansian/top-100-young-adult-fiction - Livros
 
 
