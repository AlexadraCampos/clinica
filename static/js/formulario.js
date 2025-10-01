document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form"); // pega o formulário
    const button = document.querySelector("button[type=submit]"); // botão Agendar
  
    form.addEventListener("submit", function (event) {
      event.preventDefault(); // evita envio imediato do form
  
      Swal.fire({
        title: 'Agendamento Realizado!',
        text: 'Seu horário foi marcado com sucesso. Em breve entraremos em contato para confirmar os detalhes.',
        icon: 'success',
        confirmButtonText: 'OK',
        confirmButtonColor: '#ff5c75'
      }).then((result) => {
        if (result.isConfirmed) {
          form.submit(); // só envia de verdade depois do aviso
        }
      });
    });
  });