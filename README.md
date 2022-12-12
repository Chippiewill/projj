# Projj

CLI commands for quickly setting up new repos and finding them again.

## `pcl` - "project clone"

Project clone performs a git clone (similar to `git clone`) but intentionally puts in in a structured filepath
`~/Developer/<git host>/<git sub path/`. For example, `pcl https://github.com/Chippiewill/projj.git` would perform a
git clone into the directory `~/Developer/github.com/Chippiewill/projj`. This is similar to how go handles its
dependencies for example.

In addition, if it is executed as a source alias (e.g. with `alias pcl='. pcl'` in your shell RC file), it will `cd`
into that directory as well.

## `pcd` - "project cd"

Project CD allows you to quickly navigate to and find a project. Functionally it finds all of the directories that
themselves contain a `.git` directory, and then pipes them into `fzf` where you then do a quick fuzzy search for the
project you have in mind. You can also provide command line arguments to `pcd` that are themselves passed to `fzf`.

For example `pcd projj` would take you straight to `~/Developer/github.com/Chippiewill/projj`. The alias
`alias pcd='. pcd'` is required to make this work.

## Install

Required dependencies:

- Recent Python 3
- fzf

```
$ make

# Vary this for your shell, or do it manually
$ cat <<EOF >> ~/.bashrc
alias pcd='. pcd'
alias pcl='. pcl'
EOF
```
