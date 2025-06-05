from pathlib import Path
import arc_agi_core as arc
import json
import shutil
from tqdm import tqdm


def generate_arc_agi_1_single_test(
    gitignore: bool = False, merge: bool = False, image: bool = False
):
    path = Path("../arc-agi-1-single-test")
    path.mkdir(exist_ok=True)

    training_dataset = arc.ARC1Training.download(
        path / "temp" / "training", git_ignore=gitignore
    )
    evaluation_dataset = arc.ARC1Evaluation.download(
        path / "temp" / "evaluation", git_ignore=gitignore
    )
    filtered_training = arc.Dataset(
        [task for task in training_dataset if len(task.test) == 1]
    )
    filtered_evaluation = arc.Dataset(
        [task for task in evaluation_dataset if len(task.test) == 1]
    )
    filtered_training.save_directory(path / "training", git_ignore=False)
    filtered_evaluation.save_directory(path / "evaluation", git_ignore=False)
    shutil.rmtree(path / "temp")

    if merge:
        filtered_training.challenges.save_json(path / "training-challenges.json")
        (path / "training-solutions.json").write_text(
            json.dumps(
                {
                    task_id: [grid.to_list() for grid in grids]
                    for task_id, grids in training_dataset.solutions.items()
                },
                indent=2,
            )
        )
        filtered_evaluation.challenges.save_json(path / "evaluation-challenges.json")
        (path / "evaluation-solutions.json").write_text(
            json.dumps(
                {
                    task_id: [grid.to_list() for grid in grids]
                    for task_id, grids in evaluation_dataset.solutions.items()
                },
                indent=2,
            )
        )
        shutil.rmtree(path / "training")
        shutil.rmtree(path / "evaluation")
        if gitignore:
            (path / ".gitignore").write_text(
                "training-challenges.json\ntraining-solutions.json\nevaluation-challenges.json\nevaluation-solutions.json"
            )

    if image:
        for task in tqdm(training_dataset, desc="Rendering training tasks"):
            task.save_svg(path / "training" / "images" / f"{task.task_id}.svg")
        for task in tqdm(evaluation_dataset, desc="Rendering evaluation tasks"):
            task.save_svg(path / "evaluation" / "images" / f"{task.task_id}.svg")


def main():
    import argparse
    from dataclasses import dataclass

    @dataclass
    class Args:
        gitignore: bool = False
        merge: bool = False
        image: bool = False

    def parse_args() -> Args:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-g",
            "--gitignore",
            action="store_true",
            help="add generated dataset into .gitignore",
        )
        parser.add_argument(
            "-m",
            "--merge",
            action="store_true",
            help="generate dataset as challenges.json and solutions.json, instead of directories containing task json files",
        )
        parser.add_argument(
            "-i", "--image", action="store_true", help="render tasks as .svg images"
        )
        return Args(**vars(parser.parse_args()))

    args = parse_args()
    generate_arc_agi_1_single_test(args.gitignore, args.merge, args.image)


if __name__ == "__main__":
    main()
