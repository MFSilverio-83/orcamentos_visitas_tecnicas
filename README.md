A ideia do projeto foi ter uma janela para poder inserir as informações para um atendimento, o valor a ser cobrado e ter o retorno do cálculo final, sem ficar fazendo conta em uma calculadora.

Código criado em Python com Tkinter.

A parte visual do sistema foi criada com os itens do tkinter, a estrutura do aplicativo, local dos botões, tamanho das fontes, caixa de retorno, tudo usando os métodos disponíveis do tkinter.

O código recebe as informações da cidade a ser visitada, a distância da sede até esta cidade, em Km, e o valor de serviço. O código faz o cálculo da viagem (ida e volta) e multiplica o resultado pelo valor cobrado do Km rodado. 

Como retorno, ele exibe os dizeres que serão inseridos no e-mail, com o nome da cidade, o valor do deslocamento técnico e o valor do serviço. Essa informação fica pronta para ser colada em qualquer local, sem precisar fazer uma cópia, pois foi utilizado o método pyperclip.copy da biblioteca pyperclip do python, basta apenas abrir o local que deseja colar o retorno e fazer um 'ctrl + v', ou clicar com o botão direito do mouse e colar.
