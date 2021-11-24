// Estrutura básica de cada carrossel. O código precisa se repetir pois
// caso usasse somente uma vez, as imagens de todos os carrosseis se misturariam

// Não tenho capacidade suficiente de javascript para criar uma função genérica
// que eliminasse a maior parte dessa repetição, então peço desculpas pelo desperdício de espaço

// Detecta todos os items do carrossel específico
let items = document.querySelectorAll('.c-1 .ci-1') 

// Loop que lida com o display de múltiplas imagens de uma vez, 
// o carrossel do Bootstrap 5 não tem suporte a isso por padrão

items.forEach((el) => {
    // define quantos slides devem ser mostrados
    const minPerSlide = 6

    // loop geral da função carrossel
    let next = el.nextElementSibling

    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // lida com o loop quando a ultima imagem encontra com a primeira
        	next = items[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})
// fim da função carrossel

// começo da próxima função carrossel
let items2 = document.querySelectorAll('.c-2 .ci-2')

items2.forEach((el) => {
    const minPerSlide = 6
    let next = el.nextElementSibling
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = items2[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})
// fim da função carrossel

// começo da próxima função carrossel
let items3 = document.querySelectorAll('.c-3 .ci-3')

items3.forEach((el) => {
    const minPerSlide = 6
    let next = el.nextElementSibling
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = items3[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})
// fim da função carrossel

// começo da próxima função carrossel
let items4 = document.querySelectorAll('.c-4 .ci-4')

items4.forEach((el) => {
    const minPerSlide = 6
    let next = el.nextElementSibling
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = items4[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})
// fim da função carrossel

// começo da próxima função carrossel
let items5 = document.querySelectorAll('.c-5 .ci-5')

items5.forEach((el) => {
    const minPerSlide = 6
    let next = el.nextElementSibling
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = items5[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})
// fim da função carrossel



// carrosseis para o home, com mínimo de 1

let items7 = document.querySelectorAll('.c-7 .ci-7')

items7.forEach((el) => {
    const minPerSlide = 1
    let next = el.nextElementSibling
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = items7[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})


let items8 = document.querySelectorAll('.c-8 .ci-8')

items8.forEach((el) => {
    const minPerSlide = 1
    let next = el.nextElementSibling
    for (var i=1; i<minPerSlide; i++) {
        if (!next) {
            // wrap carousel by using first child
        	next = items8[0]
      	}
        let cloneChild = next.cloneNode(true)
        el.appendChild(cloneChild.children[0])
        next = next.nextElementSibling
    }
})
