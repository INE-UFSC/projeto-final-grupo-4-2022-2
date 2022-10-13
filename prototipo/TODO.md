# TODO

## Observações importantes

#### Refatorar a logica de colisão (controlador de entidades remover a cada frame as entidades que estão destruidas?)
#### Atualizar sempre que for modificado o UML

## Checklist

#### [ ] - Fabricas de entidades (bullet, asteroid, player), facilitar a criação das entidades
####    -> Está feito a fábrica de DefaultBullet e de Asteroid
#### [ ] - Placar do usuário e scores salvos em disco (estilo arcade? nome AAA score 999 nome BBB score 998)
#### [ ] - Fazer estados (menu, fim de jogo, pause), deixar o jogo com cara de jogo
#### [ ] - Fazer scores de todos os jogadores, requisito
#### [ ] - Fazer sprites, deixar o jogo bonitão
#### [ ] - Arrumar singleton, pois ele está permitindo mais de uma instância (instancia como atributo da classe?)
#### [ ] - Implementar LevelManager e ModeManager


## Histórico 
#### [x] - Colocar screen_size dentro das entidades, facilita a lógica de movimentação (Screen size virou uma constante importada)
#### [x] - Fazer classe arma abstrata, para poder implementar modos diferentes
#### [x] - Novas balas, para poder implementar modos diferentes (1)
#### [x] - Tipagem dos retornos dos métodos e potencialmente dos parâmetros (def foo(a: int) -> Type:) (2)
