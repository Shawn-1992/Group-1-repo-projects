# Testing the CI/CD Lab

## Main.py file contents

```
def hello():
    print("hi")


def bye():
  print("bye")


print(hello())
```

## Catching errors

The following file contents contain an indentation error on line 6. The indentation is not a multiple of four. However, it does not keep the file from running successfully.

A test asserting the following:

```
def test_bye_function():
    assert bye() == "bye"
```
**Will pass.** <br>
The code is still accessible, but the problem with the indentation persists. In a sizeable application, such an error could likely go unnoticed and result in bugs that could prevent the program's execution. 

## Super-linter and formatting issues 

GitHub's Super Linter catches many formatting discrepancies that would later cause issues down the line. The Super-Linter finds errors such as these and reports them to the console output. The user fixes the errors manually, but a status check will show failed on the pull request, so no broken code gets merged. A combination of various linters will help validate your source code. The main goal of this tool is to prevent code from breaking upon uploading to a branch.