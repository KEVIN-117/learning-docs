
Para traer todas las ramas remotas a tu repositorio local en Git, usa el siguiente comando:

```sh
git fetch --all
```

Este comando actualizará tu referencia local de todas las ramas remotas sin hacer un **checkout** ni fusionarlas con tu rama actual.

Si además quieres traer todas las ramas y hacerlas accesibles localmente, puedes ejecutar:

```sh
git pull --all
```

Sin embargo, **`git pull --all` no es recomendado** en la mayoría de los casos, porque intenta fusionar cambios en todas las ramas locales al mismo tiempo.

### 🔹 Si quieres listar las ramas remotas después de traerlas:

```sh
git branch -r
```

### 🔹 Si deseas crear una copia local de una rama remota específica:

```sh
git checkout -b nombre-de-la-rama origin/nombre-de-la-rama
```

O con Git 2.23+:

```sh
git switch -c nombre-de-la-rama origin/nombre-de-la-rama
```

Si quieres ver todas las ramas (locales y remotas), usa:

```sh
git branch -a
```
