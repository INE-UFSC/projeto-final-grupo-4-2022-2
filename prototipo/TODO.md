# TODO

## Observações importantes

#### Atualizar sempre que for modificado o UML
#### Os pickups vão ser uma entidade que quando colide com o player, o player ganha munição, muda de arma ou outro powerup. Vale observar que é fácil identificar a colisão do player com um powerup, já que se tem um método nas entidades chamado on_collision
#### Como fazer os estados de cada modo: criar classes concretas que herdaram de stateingame e implementar ou sobreescreve os métodos de acordo com a lógica do modo

## Checklist

## Outros

#### [ ] - Pickups (armas e bullet)
#### [ ] - Fazer os estados para cada modo (Um estado em que o player não tem arma e só desvia dos inimigos; um outro em que o player tem por padrão uma arma com balas limitadas e ao longo do jogo spawna pickups para alterar arma e ganhar munição; um outro ainda que só spawna alien; por fim, um último que spwana sem parar apenas asteroids)
#### [ ] - Telas de Interface Estáticas (Menu, Scoreboard, Game Over/Save Score)
#### [ ] - Melhorar sprites (carregamento e alguns detalhes)
#### [ ] - Otimizar imports (principalmente imports das constantes)


## Histórico

#### [x] - Filtrar caracteres no text input (nem toda key é unicode)
#### [x] - Fazer sprites, deixar o jogo bonitão
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
