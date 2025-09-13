document.addEventListener('DOMContentLoaded', function () {
    const cepInput = document.getElementById('id_cep');
    if (cepInput) {
        Inputmask('99999-999').mask(cepInput);

        cepInput.addEventListener('blur', function () {
            const rawCep = cepInput.inputmask.unmaskedvalue();
            if (rawCep.length === 8) {
                fetch(`/buscar-cep/?cep=${rawCep}`)
                    .then(response => response.json())
                    .then(data => {
                        if (!data.error) {
                            document.getElementById('id_endereco').value = data.endereco;
                            document.getElementById('id_bairro').value = data.bairro;
                            document.getElementById('id_cidade').value = data.cidade;
                            document.getElementById('id_estado').value = data.estado;
                        } else {
                            alert('CEP não encontrado.');
                        }
                    })
                    .catch(() => alert('Erro ao buscar o CEP.'));
            }
        });
    }
});
