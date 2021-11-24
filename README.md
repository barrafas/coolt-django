# coolt-django
Transição do projeto presente no repositório https://github.com/adamesalles/shelf-lp para plataforma Django.

# Coolt

Conheça o Coolt: o melhor site de estante de mídias! Organize seus interesses, receba recomendações personalizadas e faça resenhas, relacionando todos os tipos de entretenimento de seu interesse! O Tako, nosso mascote, está aqui para ajudar!

O site conta com suporte para 5 tipos de mídia: Animes, Filmes, Livros, Jogos e Séries.


## Página de Login
Página de entrada do Coolt, onde é possível conhecer melhor o site, buscando atrair mais usuários. 

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


## Organização do Trabalho

No começo da semana, fizemos uma reunião e organizamos as primeiras páginas que cada um deveria desenvolver. A divisão ficou a seguinte:

---

 - Tiago e Carol: Montar o padrão para as páginas de exploração dos diversos tipos de mídia, e popular elas manualmente com exemplos
 - Edu: Montar a página "Minha Estante" com efeitos mais interativos usando javascript e json
 - Rodrigo e Vini: Montar as páginas "Chamariz" e "Sobre", além de pensarem sobre a identidade visual do site

Em segunda etapa, nos juntamos em chamada para criar as últimas páginas, e para padronizar o estilo de todas as páginas. 
 Tiago e Carol focaram na criação da página template para a "Home", Rodrigo deu os toques finais no "Chamariz" e no footer, Vini focou na padronização das páginas com a identidade visual, e Edu fez a página template para as obras.

Por fim, fizemos uma call para ajustar tudo que ainda era necessário, padronizar comandos e etc.. 


