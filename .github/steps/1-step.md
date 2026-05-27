## Etapa 1: Peça uma Revisão no VS Code


A Mergington High School possui um site de Atividades Extracurriculares. Nos últimos meses, você adicionou muitos recursos e ele tem sido cada vez mais utilizado por outros professores e alunos.


Agora, vários professores querem ajudar a desenvolver novos recursos. Isso é ótimo, mas sua energia é limitada e, se você não tiver tempo para revisar as mudanças, teme que a aplicação fique bagunçada. Para escalar sua disponibilidade de "revisão", vamos implementar o **GitHub Copilot code review**!


Antes de implementarmos revisões automáticas com o Copilot, faz sentido experimentar as revisões localmente no VS Code. Isso nos ajudará a entender melhor, construir nossos critérios de revisão e garantir que todos os professores-colaboradores recebam feedback consistente ao começar a contribuir.

### 📖 Teoria: Revisão de Código Local com GitHub Copilot


O GitHub Copilot pode revisar seu código diretamente no VS Code, fornecendo feedback imediato sobre alterações não commitadas. Ele até adiciona comentários semelhantes ao feedback de um pull request! Essa capacidade de revisão local permite que desenvolvedores encontrem problemas antes mesmo de chegarem ao controle de versão, melhorando a qualidade do código desde o início. E talvez até pegue aqueles erros de digitação constrangedores! 😅


Principais recursos:


- **Análise local** de alterações não commitadas
- **Recomendações de qualidade e estilo de código**
- **Detecção** de vulnerabilidades de segurança comuns
- **Sugestões de otimização de performance**


Esse feedback imediato ajuda você a identificar e corrigir problemas cedo no processo de desenvolvimento, tornando seu código mais robusto antes mesmo de chegar a um pull request.

## ⌨️ Atividade: Conheça o site de atividades extracurriculares


Antes de começarmos a desenvolver e revisar, vamos entender o site atual.


1. Clique com o botão direito no botão abaixo para abrir a página **Create Codespace** em uma nova aba. Use a configuração padrão.

   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/{{full_repo_name}}?quickstart=1)


2. Aguarde um tempo para o ambiente ser preparado. Ele instalará automaticamente todos os requisitos e serviços.


3. Valide que as extensões **GitHub Copilot** e **Python** estão instaladas e habilitadas.

   <img width="300" alt="copilot extension for VS Code" src="https://github.com/user-attachments/assets/ef1ef984-17fc-4b20-a9a6-65a866def468" /><br/>
   <img width="300" alt="python extension for VS Code" src="https://github.com/user-attachments/assets/3040c0f5-1658-47e2-a439-20504a384f77" />


4. Tente rodar a aplicação. Na barra lateral esquerda, selecione a aba **Run and Debug** e pressione o ícone **Start Debugging**.

   <img width="300" alt="run and debug" src="https://github.com/user-attachments/assets/50b27f2a-5eab-4827-9343-ab5bce62357e" />


   <details>
   <summary>🤷 Está com problemas?</summary><br/>

   Se a área **Run and Debug** estiver vazia, tente recarregar o VS Code: Abra a paleta de comandos (`Ctrl`+`Shift`+`P`) e procure por `Developer: Reload Window`.

   <img width="300" alt="painel run and debug vazio" src="https://github.com/user-attachments/assets/0dbf1407-3a97-401a-a630-f462697082d6" />

   </details>


5. Use a aba **Ports** para encontrar o endereço da página web, abra e verifique se está rodando.

   <img width="350" alt="ports tab" src="https://github.com/user-attachments/assets/8d24d6b5-202d-4109-8174-2f0d1e4d8d44" />

   ![Screenshot of Mergington High School WebApp](https://github.com/user-attachments/assets/5e1e7c1e-1b0e-4378-a5af-a266763e6544)

### ⌨️ Atividade: Peça uma revisão ao Copilot


Vamos adicionar um banner simples para professores fazerem comunicados e pedir feedback ao Copilot.


6. No VS Code, crie um novo branch com o nome abaixo.

   ```txt
   add-announcement-banner
   ```


7. Abra o arquivo `src/static/index.html`. Adicione o seguinte após a tag `<body>`.

   ```html
    <div class="announcement-banner">
       📢 As inscrições para atividades estão abertas até o final do mês. Não perca sua vaga!
    </div>
   ```


8. Abra o arquivo `src/static/styles.css`. Adicione o seguinte ao final do arquivo.

   ```css
   .announcement-banner {
     background-color: #4caf50;
     color: white;
     text-align: center;
     padding: 15px;
     font-weight: bold;
   }
   ```


9. (opcional) Atualize o app rodando para ver a mudança.

   <img width="400" alt="screenshot of site with announcement banner" src="https://github.com/user-attachments/assets/39de7fe0-58f2-4eba-a163-d3037b2b3b06"/>


10. No VS Code, abra o painel de controle de versão e garanta que há alterações não commitadas.



11. Peça uma revisão ao Copilot usando a paleta de comandos do VS Code:

   - Pressione `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (Mac) para abrir a paleta de comandos.
   - Digite `Chat: Review` e selecione a opção correspondente.
   - Aguarde o Copilot analisar suas alterações e adicionar comentários de revisão.


> [!TIP]
> Você pode escolher revisar alterações não commitadas, staged ou todas as alterações não enviadas. Certifique-se de salvar os arquivos antes de pedir a revisão.


12. Expanda o painel **Comments** para ver a lista de feedbacks do Copilot.


   <img width="300" alt="painel de problemas com comentários do Copilot" src="https://github.com/user-attachments/assets/64c5efb6-9071-4511-b2a2-2dc85c9e929b"/>

13. Use os botões **Aplicar** ou **Descartar** para tratar o feedback do Copilot.

   <img width="300" alt="captura de tela de comentário inline com botões para tratar feedback" src="https://github.com/user-attachments/assets/aef73097-acaf-4f5b-a52f-52a142bb413f"/>

14. Faça commit e push das alterações relacionadas ao Announcement na branch `add-announcement-banner`.

15. Com suas alterações enviadas, aguarde um momento para a Mona checar seu trabalho, fornecer feedback e compartilhar a próxima lição.

<details>
<summary>Está com problemas? 🤷</summary><br/>

- A Revisão do Copilot no VS Code só considera alterações não commitadas. Não faça commit antes de pedir a revisão.
- Se o Copilot não fornecer feedback de revisão, certifique-se de clicar no botão correto para o agrupamento (unstaged, staged, uncommitted).
- Se o Copilot não enxergar suas alterações, certifique-se de salvar os arquivos antes.

</details>
