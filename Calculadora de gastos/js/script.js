const botao = document.getElementById('calcular');

botao.addEventListener('click', calcular);

function calcular() {
    const distancia = parseFloat(document.getElementById('distancia').value);
    const consumo = parseFloat(document.getElementById('rendimento').value);
    const preco = parseFloat(document.getElementById('precoGasolina').value);

    if (isNaN(distancia) || isNaN(consumo) || isNaN(preco)) {
        alert("Por favor, preencha todos os campos corretamente.");
        return;
    }

    const valorGasto = (distancia / consumo) * preco;

    const resultadoElement = document.getElementById('resultado');
    resultadoElement.textContent = `O valor gasto será de R$ ${valorGasto.toFixed(2)}`;
}