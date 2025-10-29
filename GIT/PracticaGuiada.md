# Práctica guiada

**Crear repositorio**
```bash
Diego Costa@DESKTOP-LM520H3 MINGW64 ~ mkdir prueba_git
Diego Costa@DESKTOP-LM520H3 MINGW64 ~ cd prueba_git
```

**Creación del nano y del script**
```
//Nano
Diego Costa@DESKTOP-LM520H3 MINGW64 ~/prueba_git (master)
$ nano text.txt

//Script
Diego Costa@DESKTOP-LM520H3 MINGW64 ~/prueba_git (master) 
$ nano script.sh
```

**Pasar a ejecutable y probar**
```
Diego Costa@DESKTOP-LM520H3 MINGW64 ~/prueba_git (master)
$ chmod a+x script.sh
Diego Costa@DESKTOP-LM520H3 MINGW64 ~/prueba_git (master)
$ ./script.sh
```

**Comprobar el estado de mi archivo**
```

Diego Costa@DESKTOP-LM520H3 MINGW64 ~/prueba_git (master)
$ git status
On branch master
Untracked files:
    (use "git add <file>..." to include in what will be committed)
        text.txt

nothing added to commit but untracked files present (use "git add" to track)
```
Solo aparece el documento txt ya que el script esta añadido a git

**Añadir el script a git y ver status**
```
Diego Costa@DESKTOP-LM520H3 MINGW64 ~/prueba_git (master)
$ git add script.sh
Diego Costa@DESKTOP-LM520H3 MINGW64 ~/prueba_git (master)
$git status
On branch master
No commits yet
Changes to be committed:
    (use "git rm --cached <file>..." to unstage)
        new file: script.sh
Untracked files:
    (use "git add <file>..." to include in what will be committed)
        texto.txt
```
**Commit**
```
Diego Costa@DESKTOP-LM520H3 MINGW64 ~prueba_git (master)
$ git commit -m "Confirmacion inicial"
r (root-commit) 972303a] Confirmación inicial
 1 file changed, 2 insertions(+)
 create mode 100644 script.sh

Diego Costa@DESKTOP-LM520H3 MINGW64 ~/prueba_git (master)
$ git status

*Se puede hacer un "$ git commit -F mensaje.txt" si fuera muy largo el mensaje
```
**Modificacion de archivos**
```
Diego Costa@DESKTOP-LM520H3 MINGW64 ~/Desktop/Afondamento/prueba_git (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   text.txt

no changes added to commit (use "git add" and/or "git commit -a")
```
```
Diego Costa@DESKTOP-LM520H3 MINGW64 ~/Desktop/Afondamento/prueba_git (main)
$ git add .

Diego Costa@DESKTOP-LM520H3 MINGW64 ~/Desktop/Afondamento/prueba_git (main)
$ git commit -m "Ampliada la explicacion del texto"
[main 0f42e26] Ampliada la explicacion del texto
 1 file changed, 1 insertion(+)

Diego Costa@DESKTOP-LM520H3 MINGW64 ~/Desktop/Afondamento/prueba_git (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```
**Informacion(gti show / git log)
