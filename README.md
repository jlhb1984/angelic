# angelic
Software for electronic design calculus.

jlhb1@DESKTOP-1EPJK6L MINGW64 ~ (master)
$ ssh-keygen -t rsa -b 4096 -C "jlhb1984@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/jlhb1/.ssh/id_rsa):
/c/Users/jlhb1/.ssh/id_rsa already exists.
Overwrite (y/n)? y
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/jlhb1/.ssh/id_rsa
Your public key has been saved in /c/Users/jlhb1/.ssh/id_rsa.pub
The key fingerprint is:
#######################
The key's randomart image is:
########################
jlhb1@DESKTOP-1EPJK6L MINGW64 ~ (master)
$ ^C

jlhb1@DESKTOP-1EPJK6L MINGW64 ~ (master)
$ eval $(ssh-agent -s)
Agent pid 2018

jlhb1@DESKTOP-1EPJK6L MINGW64 ~ (master)
$ ñ
bash: ñ: command not found

jlhb1@DESKTOP-1EPJK6L MINGW64 ~ (master)
$ ~
bash: /c/Users/jlhb1: Is a directory

jlhb1@DESKTOP-1EPJK6L MINGW64 ~ (master)
$ pwd
/c/Users/jlhb1

jlhb1@DESKTOP-1EPJK6L MINGW64 ~ (master)
$ ssh add ~/.ssh/id_rsa
ssh: Could not resolve hostname add: Name or service not known

jlhb1@DESKTOP-1EPJK6L MINGW64 ~ (master)
$ ssh-add ~/.ssh/id_rsa
Identity added: /c/Users/jlhb1/.ssh/id_rsa (jlhb1984@gmail.com)


Truble: jlhb984 is not a valid directory.


Solution:

jlhb1@DESKTOP-1EPJK6L MINGW64 ~ (master)
$ cd /c

jlhb1@DESKTOP-1EPJK6L MINGW64 /c
$ cd gitprojects

jlhb1@DESKTOP-1EPJK6L MINGW64 /c/gitprojects (main)
$ cd angelic

jlhb1@DESKTOP-1EPJK6L MINGW64 /c/gitprojects/angelic (main)
$ $ git remote set-url origin git@github.com:jlhb1984/angelic
bash: $: command not found

jlhb1@DESKTOP-1EPJK6L MINGW64 /c/gitprojects/angelic (main)
$ git remote set-url origin git@github.com:jlhb1984/angelic

jlhb1@DESKTOP-1EPJK6L MINGW64 /c/gitprojects/angelic (main)
$ git push origin main
Enumerating objects: 132, done.
Counting objects: 100% (132/132), done.
Delta compression using up to 2 threads
Compressing objects: 100% (129/129), done.
Writing objects: 100% (132/132), 25.64 KiB | 354.00 KiB/s, done.
Total 132 (delta 72), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (72/72), done.
To github.com:jlhb1984/angelic
 * [new branch]      main -> main

jlhb1@DESKTOP-1EPJK6L MINGW64 /c/gitprojects/angelic (main)
$
