pex_binary(
    name = "foo",
    srcs = ["foo.py"],
)

pex_library(
    name = "libfoo",
    srcs = ["foo.py"],
    reqs = [
        "flask",
        "pyyaml",
    ],
)

pex_pytest(
    name = "foo_test",
    srcs = ["foo_test.py"],
    args = ["--strict"],
    deps = [":libfoo"],
    size = "small",
)

pex_library(
    name = "pythonroot",
    srcs = ["pythonroot.py"],
    # makes it importable with "import pythonroot"
    pythonroot = ".",
)

pex_pytest(
    name = "pythonroot_test",
    srcs = ["pythonroot_test.py"],
    deps = [":pythonroot"],
)
