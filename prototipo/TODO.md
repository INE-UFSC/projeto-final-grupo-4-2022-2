# TODO

## Observações importantes

#### Refatorar a logica de colisão (controlador de entidades remover a cada frame as entidades que estão destruidas?)
#### Atualizar sempre que for modificado o UML

## Checklist

## Outros

#### [ ] - Filtrar caracteres no text input
#### [ ] - Fazer sprites, deixar o jogo bonitão
#### [ ] - Implementar LevelManager e ModeManager
#### [ ] - Otimizar imports (principalmente imports das constantes)


## Histórico

#### [x] - Scores salvos em disco (estilo arcade? nome AAA score 999 nome BBB score 998)
#### [x] - Fazer estados (menu, fim de jogo, pause), deixar o jogo com cara de jogo
#### [x] - Adicionar constantes no arquivo const. Por exemplo, constantes de correção, munição máxima, velocidade máxima e etc
#### [x] - Arrumar singleton, pois ele está permitindo mais de uma instância (instancia como atributo da classe?)
#### [x] - Fabrica de player
#### [x] - Fabricas de entidades (bullet, asteroid), facilitar a criação das entidades
#### [x] - Colocar screen_size dentro das entidades, facilita a lógica de movimentação (Screen size virou uma constante importada)
#### [x] - Fazer classe arma abstrata, para poder implementar modos diferentes
#### [x] - Novas balas, para poder implementar modos diferentes (1)
#### [x] - Tipagem dos retornos dos métodos e potencialmente dos parâmetros (def foo(a: int) -> Type:) (2)
