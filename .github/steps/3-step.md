## Etapa 3: Personalize Sua Revisão


Os padrões de codificação da escola são cruciais para manter o site de atividades. Você percebeu que os professores estão usando estilos visuais e padrões de código diferentes. Com tanta diversidade de experiências e prioridades entre os professores-colaboradores, vamos personalizar o comportamento de revisão do Copilot para alinhar com os padrões educacionais da escola.

### 📖 Teoria: Instruções Personalizadas do Repositório


As instruções personalizadas do repositório permitem fornecer ao Copilot contexto sobre os padrões e preferências do seu projeto. Criando arquivos de instrução, você garante que as sugestões do Copilot sigam consistentemente as convenções do seu time e foquem nos requisitos específicos. Você pode até pedir para o Copilot analisar seu projeto e [gerar instruções](https://code.visualstudio.com/docs/copilot/customization/custom-instructions#_generate-an-instructions-file-for-your-workspace) para você!


**Tipos de Instruções:**


- **Instruções para o repositório inteiro**: Se aplicam a todo o código do repositório. Ex: `.github/copilot-instructions.md`
- **Instruções específicas por caminho**: Se aplicam a arquivos específicos para criar critérios focados em diferentes partes do código. Ex: `.github/instructions/NOME.instructions.md`.


As instruções são escritas em linguagem natural, no formato Markdown, e normalmente incluem:


- Requisitos e checklists de segurança
- Padrões e convenções de código
- Prioridades de otimização de performance
- Preferências e guias de estilo do time
- Critérios de revisão específicos por linguagem


Arquivos de instrução específicos por caminho incluem [YAML front matter](https://docs.github.com/en/contributing/writing-for-github-docs/using-yaml-frontmatter) com [glob patterns](https://code.visualstudio.com/docs/editor/glob-patterns) para direcionar arquivos e diretórios específicos. Exemplos:

```yaml
---
applyTo: "tests/**/**,docs/*.md"
---
# Testing Guidelines ...
```

```yaml
---
applyTo: "docs/*.md,README.md"
---
# Documentation Guidelines ...
```


> [!TIP]
> As [instruções personalizadas](https://docs.github.com/en/copilot/how-tos/custom-instructions/adding-repository-custom-instructions-for-github-copilot) funcionam tanto para revisões locais no VS Code quanto para pull requests, garantindo consistência em todo o fluxo de desenvolvimento.

### ⌨️ Atividade: Adicione instruções gerais


Vamos personalizar os critérios de revisão do Copilot adicionando instruções customizadas.


1. No VS Code, certifique-se de que ainda está na branch `add-announcement-banner`.


2. Crie um arquivo para as diretrizes gerais do repositório.


   Localização e nome do arquivo:

   ```txt
   .github/copilot-instructions.md
   ```


   Conteúdo:

   ```markdown
   ## Segurança

   - Valide práticas de sanitização de entrada de dados.
   - Procure riscos que possam expor dados de usuários.
   - Prefira carregar configurações e conteúdos do banco de dados ao invés de valores fixos no código. Se for absolutamente necessário, use variáveis de ambiente ou arquivos de configuração não versionados.

   ## Qualidade do Código

   - Use convenções de nomenclatura consistentes.
   - Tente reduzir duplicação de código.
   - Prefira manutenibilidade e legibilidade à otimização prematura.
   - Se um método for muito utilizado, tente otimizá-lo para performance.
   - Prefira tratamento explícito de erros a falhas silenciosas.
   ```

### ⌨️ Atividade: Adicione instruções específicas


Vamos criar critérios de revisão específicos do Copilot para o frontend e backend.


3. Crie um arquivo para as diretrizes específicas do frontend.


> [!IMPORTANT]
> Certifique-se de colocar instruções específicas de arquivo na pasta `.github/instructions/`, não na pasta `.github/`.


   Localização e nome do arquivo:

   ```txt
   .github/instructions/frontend.instructions.md
   ```

   Conteúdo:

   ```markdown
   ---
   applyTo: "*.html,*.css,*.js"
   ---

   ## Diretrizes de Frontend

   - Use atributos de acessibilidade (alt text, aria labels) e esquemas de cores.
   - Use design responsivo para compatibilidade com dispositivos móveis.
   - Valide a estrutura HTML e elementos semânticos
   ```

4. Crie um arquivo para as diretrizes específicas do backend.

   Localização e nome do arquivo:

   ```txt
   .github/instructions/backend.instructions.md
   ```

   Conteúdo:

   ```markdown
   ---
   applyTo: "backend/**/*,*.py"
   ---

   ## Diretrizes de Backend

   - Todos os endpoints de API devem ser definidos na pasta `routers`.
   - Carregue conteúdo de exemplo do banco de dados a partir do arquivo `database.py`.
   - O tratamento de erros deve ser registrado apenas no servidor. Não propague para o frontend.
   - Garanta que todas as APIs estejam explicadas na documentação.
   - Verifique se mudanças no backend se refletem no frontend (`src/static/**`). Se encontrar possíveis breaking changes, mencione ao desenvolvedor.
   ```


5. Faça commit e push dos arquivos de instrução.


> [!TIP]
> O VS Code possui comandos integrados para ajudar a gerenciar instruções. Tente abrir a paleta de comandos e buscar por `instructions`.

### ⌨️ Atividade: Solicite outra revisão

Com nossas novas instruções definidas, o Copilot agora entende melhor o que é importante para nosso projeto. Vamos pedir outra revisão.

6. No VS Code, certifique-se de que as instruções foram realmente commitadas e faça push para o repositório.

7. No navegador, retorne ao pull request criado recentemente.

8. No canto superior direito, encontre o menu **Reviewers** e o botão **Re-request review** ao lado de **Copilot**. Clique nele e aguarde um momento para o Copilot adicionar comentários ao pull request.

   <img width="300" alt="botão de re-revisão" src="https://github.com/user-attachments/assets/c45aa8de-278d-46e7-bfe2-2dc6b574e11e"/>


> [!NOTE]
> Se você for rápido demais após enviar novos commits, talvez precise esperar um pouco para o botão aparecer, ou atualizar a página.

9. Observe que o feedback do Copilot agora é diferente da revisão anterior.

10. Com a revisão solicitada, aguarde um momento para a Mona checar seu trabalho, fornecer feedback e compartilhar a próxima lição.

<details>
<summary>Está com problemas? 🤷</summary><br/>

- Se você esqueceu de adicionar uma instrução personalizada (ou cometeu um erro de digitação), tente corrigir o erro e pedir outra revisão ao Copilot. Isso informará a Mona para checar seu trabalho novamente.

</details>
