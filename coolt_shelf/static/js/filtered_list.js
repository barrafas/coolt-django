// Por enquanto, estarei utilizando javascript dentro do HTML.
// Encontrando o grid-container
let grid_container = document.getElementById('grid-container')
// Captando os botões de filtro
const filters = document.forms['filter'].querySelectorAll('input')
// Criando o array filtros
let filter = ['anime', 'filme', 'livro', 'jogo', 'serie']
// Array de objetos com alguns works
let works = [{'name': 'A Silent Voice', 'pic':'https://www.intoxianime.com/wp-content/uploads/2016/09/silent-voice-new-visual.png.jpg','type': 'anime'},{'name': 'Coringa', 'pic':'https://3jm17k957xm280ka42nsilm6-wpengine.netdna-ssl.com/wp-content/uploads/2019/12/The-Joker-DVD-and-Blu-ray-cover-art.jpg','type': 'filme'}, {'name': 'Forza Horizon 4', 'pic':'https://store-images.s-microsoft.com/image/apps.36093.14339303838396367.725ab8dd-f8b7-4a29-a351-45ebd5d66edd.ba2a2523-7f32-4f92-a83d-26097b7b6ca1?mode=scale&q=90&h=300&w=200','type': 'jogo'}, {'name': 'Diário de um Banana', 'pic':'https://m.media-amazon.com/images/I/51NmVKrbhAL.jpg', 'type': 'livro'}, {'name': 'Cowboy Bebop', 'pic': 'https://cdn.myanimelist.net/images/anime/4/19644.jpg', 'type':'anime'}, {'name': 'Sid Meier\'s Civilization VI', 'pic': 'https://upload.wikimedia.org/wikipedia/pt/thumb/3/3b/Civilization_VI_cover_art.jpg/200px-Civilization_VI_cover_art.jpg', 'type': 'jogo'}, {'name': 'Neon Genesis Evangelion', 'pic': 'https://cdn.myanimelist.net/images/anime/1314/108941.jpg', 'type': 'anime'}, {'name': 'Theme Hospital', 'pic': 'https://www.mobygames.com/images/covers/l/1089-theme-hospital-dos-front-cover.jpg', 'type': 'jogo'}, {'name': 'O Rei Leão', 'pic': 'https://a-static.mlcdn.com.br/618x463/dvd-o-rei-leao-novo-disney/videoimpacto/8319872259/aef2f3eb14c0c2fa5ec67ae3529b1883.jpg', 'type': 'filme'}, {'name': 'Mr. Robot', 'pic': 'https://veja.abril.com.br/wp-content/uploads/2016/11/mrrobot11.jpg?quality=70&strip=all', 'type': 'serie'}, {'name': 'Attack on Titan', 'pic': 'https://cdn.myanimelist.net/images/anime/10/47347.jpg', 'type':'anime'}, {'name': 'O Poderoso Chefão', 'pic': 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg', 'type': 'filme'}, {'name': 'Batman Begins', 'pic': 'https://m.media-amazon.com/images/I/51EBZ3Lh+7L.jpg', 'type': 'filme'}, {'name': 'O Cavaleiro das Trevas', 'pic': 'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_.jpg', 'type': 'filme'}, {'name': 'De Volta para o Futuro', 'pic': 'https://m.media-amazon.com/images/I/71BPuv+iRbL._AC_SL1000_.jpg', 'type': 'filme'}, {'name':'De Volta Para o Futuro 2', 'pic': 'https://m.media-amazon.com/images/M/MV5BZTMxMGM5MjItNDJhNy00MWI2LWJlZWMtOWFhMjI5ZTQwMWM3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg', 'type': 'filme'}, {'name': 'De Volta para o Futuro 3', 'pic': 'https://m.media-amazon.com/images/I/71sPGYXUl+L._AC_SY679_.jpg', 'type': 'filme'}, {'name': 'Meditações', 'pic': 'https://images-na.ssl-images-amazon.com/images/I/612B0id4gNL.jpg', 'type': 'livro'}, {'name': 'Sobre a Brevidade da Vida', 'pic': 'https://www.edipro.com.br/wp-content/uploads/2020/10/Sobre-a-brevidade-da-vida_capa-scaled.jpg', 'type':'livro'}, {'name': 'Star Wars: Episódio V', 'pic': 'https://m.media-amazon.com/images/I/51nwJJf3IjL.jpg', 'type': 'filme'}, {'name': 'Simcity 2000', 'pic': 'https://www.mobygames.com/images/covers/l/3370-simcity-2000-cd-collection-dos-front-cover.jpg', 'type': 'jogo'}, {'name': 'Diablo III', 'pic': 'https://s2.gaming-cdn.com/images/products/1795/271x377/jogo-battle-net-diablo-iii-battle-chest-cover.jpg', 'type': 'jogo'}, {'name': 'Monty Python', 'pic':'https://m.media-amazon.com/images/I/71bXBpvGniL._AC_SY550_.jpg', 'type':'filme'}, {'name': 'O Gâmbito da Rainha', 'pic': 'https://media.fstatic.com/hD6fE2hKtel8v4KGeXyX7vXyiwM=/290x478/smart/media/movies/covers/2020/09/queens_gambit.jpg', 'type': 'serie'}]

// Função para ordenar objetos em lista por key.
function sortObj(list, key) {
    function compare(a, b) {
        a = a[key];
        b = b[key];
        var type = (typeof(a) === 'string' ||
                    typeof(b) === 'string') ? 'string' : 'number';
        var result;
        if (type === 'string') result = a.localeCompare(b);
        else result = a - b;
        return result;
    }
    return list.sort(compare);
}

let ordered_works = sortObj(works, 'name')

// Faz com que cada botão, ao ser clicado, chame a função para alterar o filtro
filters.forEach((button) => button.addEventListener('click', () => change_filter(button)))
// Altera o filtro se baseando no botão apertado ou não
function change_filter(btn) {
    let pos = filter.indexOf(btn.value)
    if (pos == -1){
        filter.push(btn.value)
    } else{
        filter.splice(pos, 1)
    }
    console.log(filter)
    // Chama a função que (re)cria o grid
    create_grid()
}

// Contador para a quantidade de itens em uma coluna
let counter = 3;
// Função principal: cria o grid baseado nos filtros
function create_grid(){
    // Destroi o antigo grid
    while (grid_container.firstChild) {
        grid_container.removeChild(grid_container.lastChild);
    }
    counter = 3
    for (const work of ordered_works){
        // Filtra os dados
        if (!filter.includes(work['type'])){
            continue;
        }
        // Verifica a necessidade de uma nova linha e a cria, se preciso
        counter++
        if (counter > 3){
            grid_row = document.createElement('div')
            grid_row.className = 'grid-row row'
            counter = 0
        }
        // Criando elemento agrupador do item
        let item = document.createElement('div')
        item.className = 'grid-item col-sm-3'
        // Criando imagem
        let img = document.createElement('img')
        img['src'] = work['pic']
        img['alt'] = work['name']
        // Criando camada de efeito
        let hover = document.createElement('div')
        hover.className = 'img-overlay'
        // Criando título 
        let title = document.createElement('div')
        title.className = 'img-title'
        title.innerText = work['name']
        // Hover <- Title
        hover.appendChild(title)
        // Item <- Img
        item.appendChild(img)
        // Item <- Hover
        item.appendChild(hover)
        // Grid-Row <- Item
        grid_row.appendChild(item)
        // Grid-Container <- Grid-Row
        grid_container.appendChild(grid_row)
    }
}
// Chama a função ao entrar na página pela primeira vez.
create_grid()