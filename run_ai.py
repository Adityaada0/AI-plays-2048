import argparse

from game_ai import ai_play
from game_functions import initialize_game


def main() -> None:
    parser = argparse.ArgumentParser(description="Run an automated 2048 AI game.")
    parser.add_argument(
        "--runs",
        type=int,
        default=1,
        help="Number of full games to simulate (default: 1).",
    )
    args = parser.parse_args()

    best_tile_counts = {}
    for run_index in range(args.runs):
        board = initialize_game()
        best_tile = int(ai_play(board))
        best_tile_counts[best_tile] = best_tile_counts.get(best_tile, 0) + 1
        print(f"Run {run_index + 1}/{args.runs} -> max tile: {best_tile}")

    print("\nSummary:")
    for tile in sorted(best_tile_counts):
        print(f"{tile}: {best_tile_counts[tile]}")


if __name__ == "__main__":
    main()
