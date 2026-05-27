## Etapa 2: Solicite uma Revisão de Pull Request


Agora que você testou as capacidades de revisão local do Copilot e fez algumas melhorias no site de atividades, é hora de criar um pull request e obter o feedback do Copilot sobre suas mudanças antes de mesclá-las na branch principal, assim como outro professor faria. Vamos ver como o Copilot revisa mudanças no processo de pull request.

### 📖 Teoria: Revisão de Código em Pull Requests


O GitHub Copilot analisa seu código e fornece feedback inteligente com sugestões acionáveis que você pode aplicar instantaneamente. Cada revisão de código consome uma [Unidade de Solicitação Premium (PRU)](https://docs.github.com/en/copilot/concepts/billing/copilot-requests) do solicitante.


> [!IMPORTANT]
> Use a [revisão de código de forma responsável](https://docs.github.com/en/copilot/responsible-use/code-review) - O Copilot foi treinado para conhecer muitas preocupações comuns de segurança, mas não deve substituir ferramentas, diretrizes e padrões dedicados. Use sempre as ferramentas corretas para cada situação.


**Principais Capacidades:**


- **Análise automatizada**: Revisa o código em busca de problemas de qualidade, segurança e performance
- **Sugestões acionáveis**: Fornece recomendações específicas com sugestões de alteração de código
- **Integração**: Funciona perfeitamente com o fluxo nativo de pull requests do GitHub, igual ao feedback de colegas
- **Não bloqueante**: Fornece revisões do tipo "Comentário" que não bloqueiam a mesclagem nem contam para aprovações obrigatórias
- **Personalizável**: Suporta instruções customizadas para alinhar com os padrões do time
- **Seguro**: Opera dentro da infraestrutura segura do GitHub


Para mais informações, veja a [documentação de revisão de código do GitHub Copilot](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review).

### ⌨️ Atividade: Solicite uma revisão


1. Se necessário, abra outra aba do navegador e acesse este repositório do exercício.


2. Inicie um novo pull request. Preencha os detalhes abaixo e clique em **Create pull request**.


   - **compare:** `add-announcement-banner`
   - **target:** `main`
   - **title:** `Add announcement banner`


3. Na área de detalhes à direita, encontre o menu **Reviewers**. Clique no **ícone de configurações** para mostrar a lista de revisores disponíveis e selecione **Copilot**.

   <img width="300" alt="screenshot of reviewers menu" src="https://github.com/user-attachments/assets/0f9f2e86-51b7-4542-82a1-afb6a22ab3ca"/>


4. Aguarde um momento para o Copilot revisar as mudanças e adicionar comentários ao seu pull request. Note que uma entrada foi adicionada ao log de conversas.

   <img width="300" alt="new log entry - requested review from copilot" src="https://github.com/user-attachments/assets/3e522bda-e68e-4469-93f4-a7ad103cca97"/>

   <img width="500" alt="new log entry - copilot's PR summary" src="https://github.com/user-attachments/assets/0a870950-560e-4df8-80d5-2b93f1be99ab"/>


5. Com a revisão solicitada, aguarde um momento para a Mona checar seu trabalho, fornecer feedback e compartilhar a próxima lição.


<details>
<summary>Está com problemas? 🤷</summary><br/>

- Se o Copilot não aparecer na lista de revisores, verifique se o repositório tem o Copilot habilitado
- Se o Copilot não aparecer na lista de revisores, confira seu plano de assinatura. Não está disponível no plano gratuito.
- Às vezes, as revisões levam um ou dois minutos para serem concluídas.

</details>
