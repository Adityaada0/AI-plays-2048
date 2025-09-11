# AI plays 2048

In this project, we develop AI that can play the game 2048 (extremely well) using [Monte Carlo tree search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search). 

## Run

Launch the game UI:

```bash
python game_display.py
```

Keyboard controls:

- `w` / `a` / `s` / `d`: manual moves
- `q`: single AI move
- `p`: continuous AI play until game over

Run AI-only simulations in terminal:

```bash
python run_ai.py --runs 5
```