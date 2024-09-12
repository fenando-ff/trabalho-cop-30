// A função faz a comparação das senhas e envia para algum lugar
function confirmarSenha() {
    let senha = document.getElementById('senha').value.trim();/* '.trim' tira os possíveis espaços que podem ter antes e depois da senha */
    let conf = document.getElementById('conf').value.trim();

    if (conf === senha) {
        botao.setAttribute('type', 'submit'); /* adiciona a o atributo submit ao botão para enviar o formulário */
    } else if (conf === "" || senha === "") /* confere se as senhas estão vazias */ {
        alert('Preencha todos os campos');
    } else {
        alert('As senhas não são iguais');
    }
}