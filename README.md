# Examples and exercises from the book "Python for Network Engineers"

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/) [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

All examples and exercises have been tested in Python 3.7 and 3.8.

## How to create your own repository for tasks

> [Git/Github basics](https://pyneng.readthedocs.io/ru/latest/book/02_git_github/index.html)

### Creating a repository on GitHub

To create your own repository based on a template, you need:

-  open [tasks repo](https://github.com/natenka/pyneng-examples-exercises-en)
-  above the file list, click Use this template
-  type a name for your repository
-  click Create repository from template
-  now you have a new repository with the same directory structure and files as pyneng-examples-exercises-en

![](https://raw.githubusercontent.com/natenka/PyNEng/master/images/git/github_use_template.png)

### Clone repository

To work locally with the repository, you need to clone it.
To do this, use the git clone command:

```
$ git clone git@github.com:natenka/pyneng-examples-exercises-en.git
Cloning into 'pyneng-examples-exercises-en'...
remote: Counting objects: 241, done.
remote: Compressing objects: 100% (191/191), done.
remote: Total 241 (delta 43), reused 239 (delta 41), pack-reused 0
Receiving objects: 100% (241/241), 119.60 KiB | 0 bytes/s, done.
Resolving deltas: 100% (43/43), done.
Checking connectivity... done.
```

Compared to the command shown in this listing, you need to change:

- username natenka to your username on GitHub;
- repository name pyneng-examples-exercises-en to its name
    repository on GitHub.

As a result, in the current directory where the git clone command was executed,
a directory with the name of the repository will appear, in my case -
"pyneng-examples-exercises-en". This directory now contains
local copy of the repository on GitHub.

## Virtual machine

Two versions of virtual machines are prepared for the course: vmware and Vagrant.
The link contains instructions for each option, as well as instructions for completing tasks on Windows:

* https://pyneng.github.io/docs/course-vm/


## Tasks (exercises)

The exercises directory contains tasks with numbers corresponding to the sections of the book.
In addition, there are all auxiliary files (configurations, etc.) that are used in tasks.

> If you have tasks with letters (for example, 5.2a) in a section, it is better to do tasks without letters and then with letters. Tasks with letter tend to be slightly more complex than letter-free tasks and they develop or complicate the idea in the respective task without letter.
> For example, in the section there are tasks 5.1, 5.2, 5.2a, 5.2b, 5.3, 5.3a. First it is better to complete 5.1, 5.2, 5.3 and then 5.2a, 5.2b, 5.3a
> If you can do a task with letters right away, it is better to do it in order.


## Тесты

Starting from section "9. Functions" there are automatic tests for checking tasks. They help to check whether is everything done according to the task and also give feedback on what does not match the task. As a rule, after first period of adaptation to tests, it becomes easier to do tasks with tests.

[How to work with tests (pytest basics)](https://pyneng.readthedocs.io/ru/latest/book/additional_info/pytest.html)

