const chave ='c94aa9a16a0aa23aeee3a0f9314e46b3'
const cidade = document.querySelector('.input-cidade')
const botao = document.querySelector('.botao-busca')
const titulo = document.querySelector('.cidade')
const temperatura = document.querySelector('.temp')
const previsao = document.querySelector('.texto-previsao')

botao.addEventListener('click', buscarCidade)

async function buscarCidade(){

    let ncidade = cidade.value

    const dados = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${ncidade}&appid=${chave}&units=metric&lang=pt_br`)
    .then(resposta=>resposta.json())

    titulo.textContent = "Tempo em "+dados.name
    temperatura.textContent = Math.ceil(dados.main.temp)+" °C"
    previsao.textContent = "Previsão: "+dados.weather[0].description

     console.log(dados);
}