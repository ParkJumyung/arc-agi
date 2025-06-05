from .scripts.generate_arc_agi_1 import generate_arc_agi_1
from .scripts.generate_arc_agi_2 import generate_arc_agi_2
from .scripts.generate_arc_agi_1_single_test import generate_arc_agi_1_single_test
from .scripts.generate_arc_agi_2_single_test import generate_arc_agi_2_single_test


def main():
    import argparse
    from dataclasses import dataclass
    from typing import Literal, List

    @dataclass
    class Args:
        dataset: List[
            Literal["arc1", "arc2", "arc1_single_test", "arc2_single_test", "all"]
        ]
        gitignore: bool = False
        merge: bool = False
        image: bool = False

    def parse_args() -> Args:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-d",
            "--dataset",
            type=str,
            choices=["arc1", "arc2", "arc1_single_test", "arc2_single_test", "all"],
            default="all",
            nargs="+",
            required=True,
            help="Dataset to generate.",
        )
        parser.add_argument(
            "-g",
            "--gitignore",
            type=bool,
            action="store_true",
            help="add generated dataset into .gitignore",
        )
        parser.add_argument(
            "-m",
            "--merge",
            type=bool,
            action="store_true",
            help="generate datasets as challenges.json and solutions.json, instead of directories containing task json files. ",
        )
        parser.add_argument(
            "-i",
            "--image",
            type=bool,
            action="store_true",
            help="render tasks as .svg images",
        )

        return Args(**vars(parser.parse_args()))

    def generate_dataset(args: Args) -> None:
        if ("arc1" in args.dataset) or ("all" in args.dataset):
            generate_arc_agi_1(args.gitignore, args.merge, args.image)
        if ("arc2" in args.dataset) or ("all" in args.dataset):
            generate_arc_agi_2(args.gitignore, args.merge, args.image)
        if ("arc1_single_test" in args.dataset) or ("all" in args.dataset):
            generate_arc_agi_1_single_test(args.gitignore, args.merge, args.image)
        if ("arc2_single_test" in args.dataset) or ("all" in args.dataset):
            generate_arc_agi_2_single_test(args.gitignore, args.merge, args.image)

    args = parse_args()
    generate_dataset(args)


if __name__ == "__main__":
    main()
