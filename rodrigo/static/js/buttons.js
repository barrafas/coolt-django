/* Ativam funções quando se clica em um botão específico*/
document.getElementById('animeCheck').addEventListener('click', funcao1);
document.getElementById('livroCheck').addEventListener('click', funcao2);
document.getElementById('filmeCheck').addEventListener('click', funcao3);
document.getElementById('jogoCheck').addEventListener('click', funcao4);
document.getElementById('serieCheck').addEventListener('click', funcao5);

/* Lista2 -> Boxplots de cada tipo */
list2=[document.getElementById('animeplot'), document.getElementById('livroplot'), document.getElementById('filmeplot'), document.getElementById('jogoplot'), document.getElementById('serieplot')]
/* Lista 3 -> Divisórias com ícones de cada tipo*/
list3=[document.getElementById('animeicon'), document.getElementById('livroicon'), document.getElementById('filmeicon'), document.getElementById('jogoicon'), document.getElementById('serieicon')]

/* Começa, por precaução, com todas os botões desativados, divisórias e boxplots invisíveis*/
for (var i = 0; i < 5; i++){
        list1[i].checked = false;
        list2[i].style.display = 'none';
        list3[i].style.display = 'none';
    }

/* Ativa apenas o primeiro botão, boxplot e divisória relativa a anime*/
function funcao1(){
    list1=[document.getElementById('animeCheck'), document.getElementById('livroCheck'), document.getElementById('filmeCheck'), document.getElementById('jogoCheck'), document.getElementById('serieCheck')]
    list2=[document.getElementById('animeplot'), document.getElementById('livroplot'), document.getElementById('filmeplot'), document.getElementById('jogoplot'), document.getElementById('serieplot')]
    list3=[document.getElementById('animeicon'), document.getElementById('livroicon'), document.getElementById('filmeicon'), document.getElementById('jogoicon'), document.getElementById('serieicon')]
    for (var i = 0; i < 5; i++){
        list1[i].checked = false;
        list2[i].style.display = 'none';
        list3[i].style.display = 'none';
    }
    list1[0].checked = true;
    list2[0].style.display = 'inline';
    list3[0].style.display = 'inline';

}

/* Ativa apenas o segundo botão, boxplot e divisória relativa a livro*/
function funcao2(){
    list1=[document.getElementById('animeCheck'), document.getElementById('livroCheck'), document.getElementById('filmeCheck'), document.getElementById('jogoCheck'), document.getElementById('serieCheck')]
    list2=[document.getElementById('animeplot'), document.getElementById('livroplot'), document.getElementById('filmeplot'), document.getElementById('jogoplot'), document.getElementById('serieplot')]
    list3=[document.getElementById('animeicon'), document.getElementById('livroicon'), document.getElementById('filmeicon'), document.getElementById('jogoicon'), document.getElementById('serieicon')]
    for (var i = 0; i < 5; i++){
        list1[i].checked = false;
        list2[i].style.display = 'none';
        list3[i].style.display = 'none';
    }
    list1[1].checked = true;
    list2[1].style.display = 'inline';
    list3[1].style.display = 'inline';
}

/* Ativa apenas o terceiro botão, boxplot e divisória relativa a filme*/
function funcao3(){
    list1=[document.getElementById('animeCheck'), document.getElementById('livroCheck'), document.getElementById('filmeCheck'), document.getElementById('jogoCheck'), document.getElementById('serieCheck')]
    list2=[document.getElementById('animeplot'), document.getElementById('livroplot'), document.getElementById('filmeplot'), document.getElementById('jogoplot'), document.getElementById('serieplot')]
    list3=[document.getElementById('animeicon'), document.getElementById('livroicon'), document.getElementById('filmeicon'), document.getElementById('jogoicon'), document.getElementById('serieicon')]
    
    for (var i = 0; i < 5; i++){
        list1[i].checked = false;
        list2[i].style.display = 'none';
        list3[i].style.display = 'none';
    }
    list1[2].checked = true;
    list2[2].style.display = 'inline';
    list3[2].style.display = 'inline';
}

/* Ativa apenas o quarto botão, boxplot e divisória relativa a jogo*/
function funcao4(){
    list1=[document.getElementById('animeCheck'), document.getElementById('livroCheck'), document.getElementById('filmeCheck'), document.getElementById('jogoCheck'), document.getElementById('serieCheck')]
    list2=[document.getElementById('animeplot'), document.getElementById('livroplot'), document.getElementById('filmeplot'), document.getElementById('jogoplot'), document.getElementById('serieplot')]
    list3=[document.getElementById('animeicon'), document.getElementById('livroicon'), document.getElementById('filmeicon'), document.getElementById('jogoicon'), document.getElementById('serieicon')]
    for (var i = 0; i < 5; i++){
        list1[i].checked = false;
        list2[i].style.display = 'none';
        list3[i].style.display = 'none';
    }
    list1[3].checked = true;
    list2[3].style.display = 'inline';
    list3[3].style.display = 'inline';
}

/* Ativa apenas o quinto botão, boxplot e divisória relativa a série*/
function funcao5(){
    list1=[document.getElementById('animeCheck'), document.getElementById('livroCheck'), document.getElementById('filmeCheck'), document.getElementById('jogoCheck'), document.getElementById('serieCheck')]
    list2=[document.getElementById('animeplot'), document.getElementById('livroplot'), document.getElementById('filmeplot'), document.getElementById('jogoplot'), document.getElementById('serieplot')]
    list3=[document.getElementById('animeicon'), document.getElementById('livroicon'), document.getElementById('filmeicon'), document.getElementById('jogoicon'), document.getElementById('serieicon')]
    for (var i = 0; i < 5; i++){
        list1[i].checked = false;
        list2[i].style.display = 'none';
        list3[i].style.display = 'none';
    }
    list1[4].checked = true;
    list2[4].style.display = 'inline';
    list3[4].style.display = 'inline';
}