

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

# Quiz.html

```html
<html>
	<head>
		<title>Викторина</title>
	</head>
	<body bgcolor=lemonchiffon>
		<img src='quiz.jpg'>
		<h1>Викторина!</h1>
		<button onclick=quiz() style="background: indianred; width: 480; height: 100; font-size: 30; color: white">Начать игру</button>
		<script>
			function quiz() {
				var questions = [
					{
						question: "Сколько дней в году?\n(a) 360\n(b) 370\n(c) 365",
						answer: "c"
					},
					{
						question: "В каком году был основан Санкт-Петербург?\n(a) 1113\n(b) 1703\n(c) 1804",
						answer: "b"	
					},
					{
						question: "Как звали последнего царя в России?\n(a) Николай\n(b) Александр\n(c) Иван",
						answer: "a"					
					},
					{
						question: "Столица Франции?\n(a) Мадрид\n(b) Рим\n(c) Париж",
						answer: "c"	
					},
					{
						question: "Сколько камазов поместится в один спичечный коробочек?\n(a) 0\n(b) 0.1\n(c) я не знаю!!!",
						answer: "b"					
					}
				];
				var score = 0;
				for (let i=0; i < questions.length; i++) {
					var response = prompt(questions[i].question);
					if (response == questions[i].answer) {
						score++;
						alert("Верно!");
					} else {
						alert("Неверно!");
					}
				}
				alert("Игра закончена, у вас " + score + "/" + questions.length);
			}
		</script>
	</body>
</html>
```

>[!tip]
> ### Что делает этот код?
> Это веб-страница с викториной из 5 вопросов на общие знания.

>[!note]
> ### Понятия в коде

Начало HTML документа
```html
<html>
```
Заголовок Страницы
```html
<head>
    <title>Викторина</title>
</head>
```
Тело страницы
```html
<body bgcolor=lemonchiffon>
```
Изображение
```html
<img src='quiz.jpg'>
```
Заголовок викторины
```html
<h1>Викторина!</h1>
```
Кнопка запуска
```html
<button onclick=quiz() style="background: indianred; width: 480; height: 100; font-size: 30; color: white">
    Начать игру
</button>
```






>[!warning]
>### ВНИМАНИЕ
> Я не закончил полностью над этим документом, но скоро выложу коммит с добавлением нескольких проектов!


# **[Главный репозиторий](https://github.com/Drugoi-Polz/IservNG)**

>[!warning]
>### ВНИМАНИЕ
> **Главным репозиторием не владею и *никак* не могу редактировать там, что есть.**








