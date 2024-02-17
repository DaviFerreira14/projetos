function mostrarFilme(filmeSelecionado) {
    const cartaz = document.getElementById("cartaz");
    const descricao = document.querySelector(".filmemostrado p");

    if (filmeSelecionado === "Missão Impossível - Acerto de Contas Parte 1") {
        cartaz.innerHTML = `
            <img src="images/0102047.jpg-c_310_420_x-f_jpg-q_x-xxyxx.jpg" alt="">
            <h2>Missão Impossível - Acerto de Contas Parte 1</h2>
            <p>Ethan Hunt, agente do FMI, aventura-se novamente em "Missão Impossível - Acerto de Contas Parte 1", sétimo longa da série de filmes "Missão Impossível".</p>
        `;
        descricao.textContent = "Ethan Hunt, agente do FMI, aventura-se novamente em 'Missão Impossível - Acerto de Contas Parte 1', sétimo longa da série de filmes 'Missão Impossível'.";
    } else if (filmeSelecionado === "Besouro Azul") {
        cartaz.innerHTML = `
            <img src="images/download.jfif" alt="">
            <h2>Besouro Azul</h2> 
            <p>O adolescente Jaime Reyes ganha superpoderes quando um misterioso escaravelho se prende à sua coluna e lhe fornece uma poderosa armadura alienígena azul.
            </p>
            
        `;
        descricao.textContent = "O adolescente Jaime Reyes ganha superpoderes quando um misterioso escaravelho se prende à sua coluna e lhe fornece uma poderosa armadura alienígena azul.";
    } else if (filmeSelecionado === "The Flash") {
        cartaz.innerHTML = `
            <img src="images/flash.jfif" alt="">
            <h2>The Flash</h2>
            <p>Os mundos colidem quando Flash viaja no tempo para mudar os eventos do passado. No entanto, quando sua tentativa de salvar sua família altera o futuro, ele fica preso em uma realidade na qual o General Zod voltou, ameaçando a aniquilação.
</p>
        `;
        descricao.textContent = "Os mundos colidem quando Flash viaja no tempo para mudar os eventos do passado. No entanto, quando sua tentativa de salvar sua família altera o futuro, ele fica preso em uma realidade na qual o General Zod voltou, ameaçando a aniquilação.";
    } else if (filmeSelecionado === "Os Cavaleiros do Zodíaco - Saint Seiya: O Começo") {
        cartaz.innerHTML = `
            <img src="images/cavaleiros.jpg" alt="">
            <h2>Os Cavaleiros do Zodíaco - Saint Seiya: O Começo</h2>
            <p>Seiya, um obstinado adolescente de rua, passa seu tempo lutando por dinheiro enquanto procura por sua irmã sequestrada. Quando uma de suas lutas inadvertidamente desperta poderes místicos que ele nunca soube que tinha.
</p>
        `;
        descricao.textContent = "Seiya, um obstinado adolescente de rua, passa seu tempo lutando por dinheiro enquanto procura por sua irmã sequestrada. Quando uma de suas lutas inadvertidamente desperta poderes místicos que ele nunca soube que tinha.";
    }
}

