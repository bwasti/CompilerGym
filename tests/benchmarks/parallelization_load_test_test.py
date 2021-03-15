# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
"""Smoke test for //tests/benchmarks:parallelization_load_test."""
from pathlib import Path

from absl import flags

from compiler_gym.util.capture_output import capture_output
from tests.benchmarks.parallelization_load_test import main as load_test
from tests.test_main import main

FLAGS = flags.FLAGS

pytest_plugins = ["tests.pytest_plugins.llvm", "tests.pytest_plugins.common"]


def test_load_test(env, tmpwd):
    del env  # Unused.
    del tmpwd  # Unused.
    FLAGS.unparse_flags()
    FLAGS(
        [
            "arv0",
            "--env=llvm-v0",
            "--benchmark=cBench-v1/crc32",
            "--max_nproc=8",
            "--nproc_increment=4",
            "--num_steps=5",
            "--num_episodes=5",
        ]
    )
    with capture_output() as out:
        load_test(["argv0"])

    assert Path("results.csv").is_file()
    assert "Run 1 threaded workers in " in out.stdout
    assert "Run 1 process workers in " in out.stdout
    assert "Run 4 threaded workers in " in out.stdout
    assert "Run 4 process workers in " in out.stdout
    assert "Run 8 threaded workers in " in out.stdout
    assert "Run 8 process workers in " in out.stdout


if __name__ == "__main__":
    main()
