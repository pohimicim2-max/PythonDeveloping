

<div align="center">

# Other

## Добро пожаловать в мою лабораторию (папку) с моими личными проектами, которые не связаны с `Python`
</div>

> [!note]
> ### Главный репозиторий всегда находится в конце этого документа (В каждом документе этой репозитории.)

# Project1.luau
```lua
local papka = game.storage.FolderMaksim

local Colors = {
Color3.new(1,0,0),
Color3.new(0,1,0),
Color3.new(0,0,1),
Color3.new(1,1,0),
Color3.new(0,1,1),
Color3.new(1,0,1),
Color3.new(1,1,1),
Color3.new(0,0,0)
}

for i, Part in pairs(papka:GetChildren()) do
if Part:isA("Part") then
local RandomnieColor = Colors[math.random(1, #Colors)]
Part.Color = RandomnieColor
Part.Parent = workspace

end

end
```
>[!tip]
> ### Что делает этот код?
> без остановки и таймера очень быстро меняет цвет

>[!note]
> ### Понятия в коде
```lua
local papka = game.storage.FolderMaksim
```
`papka` - переменная, которая хранит ссылку на папку

`game.storage.FolderMaksim` - путь к папке в `Workspace`

```lua
for i, Part in pairs(papka:GetChildren()) do
```
Цикл со всеми деталями в папке(в папке только один парт)
`papka:GetChildren()` - получить **ВСЕ** парты(parts) из папки

```lua
if Part:isA("Part") then
```
Проверка типа объекта

`isA` - это **определить**, есть ли парт с названием `Part`

если проще то:
**Если** Парт:ЭТО("Парт") тогда
>... И уже запускается цикл

```lua
local RandomnieColor = Colors[math.random(1, #Colors)]
```
Выбор случайного цвета
`#Colors` - Кол-во цветов в таблице (их **8**)

`math.random(1, 8)` - Случайное число от 1 до 8

`Part.color = RandomnieColor` - устанавливает выбранный рандомный цвет для делати

```lua
Part.Parent = workspace
```
Перемещает Парт в `workspace`(чтобы игрок видел этот парт)

>[!warning]
>### ВНИМАНИЕ
> Я не закончил полностью над этим документом, но скоро выложу коммит с добавлением нескольких проектов!


# **[Главный репозиторий](https://github.com/Drugoi-Polz/IservNG)**

>[!warning]
>### ВНИМАНИЕ
> **Главным репозиторием не владею и *никак* не могу редактировать там, что есть.**








