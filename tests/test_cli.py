import subprocess


def test_main():
    assert subprocess.check_output(["neuroflow", "foo", "foobar"], text=True) == "foobar\n"
