---
aliases:
  - Version control and collaborative development
---
# Commands

```bash
git branch
git checkout branch-name

# To create and switch to a new branch:
git checkout -b new-branch-name

git switch branch-name


```

This course introduces learners to version control using Git. You will discover the importance of version control when working on data science projects and explore how you can use Git to track files, compare differences, modify and save files, undo changes, and allow collaborative development through the use of branches. You will gain an introduction to the structure of a repository, how to create new repositories and clone existing ones, and show how Git stores data. By working through typical data science tasks, you will gain the skills to handle conflicting files.

# Introduction to Git

In the first chapter, you’ll learn what version control is and why it is essential for data projects. Then, you’ll discover what Git is and how to use it for a version control workflow.

### Version control

- Version control is a group of systems and processes
	- To manage changes made to documents, programs, and directories
	- Useful for anything that change over time or, needs to be shared
- Version control allow
	- Track files in different states
	- Simultaneous file development (Continuous Development)
	- Combine different versions of files
	- Identify a particular version
	- Revert changes

Benefits of Git

- Git stores everything, so nothing is lost
- Git notifies us when there is conflicting content in files
- Git synchronizes across different people and computers

### Staging and committing

Putting files in the staging area is like placing a letter in an envelope, while making a commit is like putting the envelope in a mailbox. We can add more things to the envelope or take things out as often as we want, but once we put it in the mailbox we can't make further changes.

![[Pasted image 20240909034617.png]]

## Git workflow

So, our Git workflow is to modify a file, save the draft to the staging area, commit the updated file to our repo, and repeat!

==Create the report.md or README.md to log what you do==

###  Comparing files

We've seen the workflow for drafting and saving updates, but if we are making lots of changes we need a way to compare versions as we make modifications

A while later we need to update the file again, this time removing the executive summary task and adding a reminder to cite the funding source. We can compare the last committed version of a file with the unstaged version by using the git diff command followed by the filename.

```bash
git diff file_name
```

What if we had already added the file to the staging area? We can use the git diff command again, but this time we add the dash-r flag to indicate we want to look at a particular revision of the file. Adding HEAD, which is a shortcut for the most recent commit, allows us to see a difference between the report file in the staging area and the version in the last commit. Note that the dash-r flag won't work if we don't put HEAD afterwards.

```bash
git diff -r HEAD file_name

git diff -r HEAD 
```
# Making changes

### The commit structure

The Git commit have 3 parts:

- Commit
	- contains the metadata: author, commit message, and time of the commit
- Tree
	- tracks the names and locations in the repo
- Blob (binary large object)
	- may contain data of any kind
	- compressed snapshot of a file's contents

Next, you’ll examine how Git stores data, learn essential commands to compare files and repositories at different times, and understand the process for restoring earlier versions of files in your data projects.

# Git workflows

In this chapter, you'll learn tips and tricks for configuring Git to make you more efficient! You'll also discover branches, identify how to create and switch to different branches, compare versions of files between branches, merge branches together, and deal with conflicting files across branches.

# Collaborating with Git

This final chapter is all about collaboration! You'll gain an introduction to remote repositories and learn how to work with them to synchronize content between the cloud and your local computer. You'll also see how to create new repositories and clone existing ones, along with discovering a workflow to minimize the risk of conflicts between local and remote repositories.