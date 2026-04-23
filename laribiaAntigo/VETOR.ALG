Algoritmo "vetor"
Var
   Vet:Vetor[0..5] de Caractere
   N,i:Inteiro
Inicio
   Escreval("Quantos nomes você vai digitar?")
   Leia(N)
   Para i de 0 ate N-1 faca
      Escreval("Digite um nome:")
      Leia(Vet[i])
   Fimpara
   Escreval ("")
   Escreval("Nome digitados")
   Para i de 0 ate N-1 faca
      Escreval(Vet[i])
   Fimpara
Fimalgoritmo