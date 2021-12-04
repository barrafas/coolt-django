document.getElementById('animeCheck').addEventListener('click', funcao1);
document.getElementById('livroCheck').addEventListener('click', funcao2);
document.getElementById('filmeCheck').addEventListener('click', funcao3);
document.getElementById('jogoCheck').addEventListener('click', funcao4);
document.getElementById('serieCheck').addEventListener('click', funcao5);



function funcao1(){
    list=[document.getElementById('animeCheck'), document.getElementById('livroCheck'), document.getElementById('filmeCheck'), document.getElementById('jogoCheck'), document.getElementById('serieCheck')]
    for (var i = 0; i < 5; i++){
        list[i].checked = false;
    }
    list[0].checked = true;
}

function funcao2(){
    list=[document.getElementById('animeCheck'), document.getElementById('livroCheck'), document.getElementById('filmeCheck'), document.getElementById('jogoCheck'), document.getElementById('serieCheck')]
    for (var i = 0; i < 5; i++){
        list[i].checked = false;
    }
    list[1].checked = true;
}

function funcao3(){
    list=[document.getElementById('animeCheck'), document.getElementById('livroCheck'), document.getElementById('filmeCheck'), document.getElementById('jogoCheck'), document.getElementById('serieCheck')]
    for (var i = 0; i < 5; i++){
        list[i].checked = false;
    }
    list[2].checked = true;
}

function funcao4(){
    list=[document.getElementById('animeCheck'), document.getElementById('livroCheck'), document.getElementById('filmeCheck'), document.getElementById('jogoCheck'), document.getElementById('serieCheck')]
    for (var i = 0; i < 5; i++){
        list[i].checked = false;
    }
    list[3].checked = true;
}

function funcao5(){
    list=[document.getElementById('animeCheck'), document.getElementById('livroCheck'), document.getElementById('filmeCheck'), document.getElementById('jogoCheck'), document.getElementById('serieCheck')]
    for (var i = 0; i < 5; i++){
        list[i].checked = false;
    }
    list[4].checked = true;
}