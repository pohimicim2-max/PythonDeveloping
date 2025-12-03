

<div align="center">

# Other

## Добро пожаловать в мою лабораторию (папку) с моими личными проектами, которые не связаны с `Python`


> [!note]
> ### Главный репозиторий всегда находится в конце этого документа (В каждом документе этой репозитории.)

>[!tip]
Сейчас вы находитесь в: 
`pythondeveloping` > `Homework` > `Other` > `README.md`
</div>

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

# Countdown.luau
>[!note]
>для того, чтобы все игроки видели один и тот же таймер, нужно добавить серверный скрипт и локальный скрипт.
>Локальный скрипт - как `css`(палитра с цветами)
>Серверный скрипт - как `JavaScript` или `html`

### Серверный скрипт
```lua
local ServerScriptService = game:GetService("ServerScriptService")
local Lighting = game:GetService("Lighting")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local timerSyncEvent = Instance.new("RemoteEvent")
timerSyncEvent.Name = "TimerSyncEvent"
timerSyncEvent.Parent = ReplicatedStorage

local totalTime = 10
local timeLeft = totalTime
local mainMusicId = "17391640536"
local tickSoundId = "75185889246558"
local warningSoundId = "2124207508"

local lastSecond = math.ceil(timeLeft)
local timerRunning = true
local colonVisible = true

local dayLighting = {
	ClockTime = 14,
	Brightness = 2,
	Ambient = Color3.fromRGB(175, 175, 175)
}

local nightLighting = {
	ClockTime = 0,
	Brightness = 0.1,
	Ambient = Color3.fromRGB(50, 50, 50)
}

local function playSoundForAll(soundId)
	timerSyncEvent:FireAllClients("PlaySound", soundId)
end

local function updateTimerForAll(timeText, isRed, transparency)
	timerSyncEvent:FireAllClients("UpdateTimer", timeText, isRed, transparency)
end

local function updateLighting(progress)
	for property, dayValue in pairs(dayLighting) do
		if typeof(dayValue) == "number" then
			local nightValue = nightLighting[property]
			Lighting[property] = dayValue + (nightValue - dayValue) * progress
		else
			Lighting[property] = dayValue:Lerp(nightLighting[property], progress)
		end
	end
end

local function syncNewPlayer(player)
	local minutes = math.floor(timeLeft / 60)
	local seconds = math.floor(timeLeft % 60)

	local timeText = colonVisible and string.format("%d:%02d", minutes, seconds) or string.format("%d %02d", minutes, seconds)
	local isRed = timeLeft <= 5
	local progress = 1 - (timeLeft / totalTime)

	timerSyncEvent:FireClient(player, "UpdateTimer", timeText, isRed, 0)
	updateLighting(progress)

	if timerRunning and timeLeft > 0 then
		timerSyncEvent:FireClient(player, "PlaySound", mainMusicId)
	end
end

game.Players.PlayerAdded:Connect(function(player)
	player.CharacterAdded:Connect(function()
		task.wait(1)
		if timerRunning then
			syncNewPlayer(player)
		end
	end)
end)

for _, player in pairs(game.Players:GetPlayers()) do
	if timerRunning then
		syncNewPlayer(player)
	end
end

coroutine.wrap(function()
	task.wait(2)

	playSoundForAll(mainMusicId)

	local startTime = os.clock()
	local lastColonBlink = os.clock()

	while timeLeft > 0 and timerRunning do
		local elapsed = os.clock() - startTime
		timeLeft = totalTime - elapsed

		local minutes = math.floor(timeLeft / 60)
		local seconds = math.floor(timeLeft % 60)

		if os.clock() - lastColonBlink >= 0.5 then
			colonVisible = not colonVisible
			lastColonBlink = os.clock()
		end

		local timeText = colonVisible and string.format("%d:%02d", minutes, seconds) or string.format("%d %02d", minutes, seconds)
		local isRed = timeLeft <= 5
		updateTimerForAll(timeText, isRed, 0)

		local progress = 1 - (timeLeft / totalTime)
		updateLighting(progress)

		local currentSecond = math.ceil(timeLeft)

		if currentSecond ~= lastSecond then
			lastSecond = currentSecond

			if currentSecond <= 2 and currentSecond > 0 then
				playSoundForAll(warningSoundId)
			elseif currentSecond > 0 then
				playSoundForAll(tickSoundId)
			end
		end

		task.wait(0.1)
	end

	if timerRunning then
		local fadeDuration = 2
		local fadeStart = os.clock()

		while os.clock() - fadeStart < fadeDuration do
			local alpha = (os.clock() - fadeStart) / fadeDuration
			updateTimerForAll("0:00", true, alpha)
			task.wait(0.1)
		end

		updateTimerForAll("0:00", true, 1)
		timerSyncEvent:FireAllClients("StopMusic")
		timerRunning = false
		timerSyncEvent:FireAllClients("HideTimer")
	end
end)()
```
### Локальный скрипт
```lua
local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Players = game:GetService("Players")
local player = Players.LocalPlayer
local playerGui = player:WaitForChild("PlayerGui")

local timerSyncEvent = ReplicatedStorage:WaitForChild("TimerSyncEvent")

local screenGui = playerGui:WaitForChild("ScreenGui")
local frame = screenGui:WaitForChild("Frame")
local timerLabel = frame:WaitForChild("Timer")
local textLabel = frame:WaitForChild("Text")
local ImageLabel = frame:WaitForChild("ImageLabel")


local mainSound = Instance.new("Sound")
mainSound.SoundId = "rbxassetid://17391640536"
mainSound.Looped = true
mainSound.Parent = workspace

timerSyncEvent.OnClientEvent:Connect(function(action, ...)
	if action == "UpdateTimer" then
		local timeText, isRed, transparency = ...

		timerLabel.Text = timeText
		timerLabel.TextTransparency = transparency
		textLabel.TextTransparency = transparency

		if isRed then
			timerLabel.TextColor3 = Color3.fromRGB(170, 107, 96)
			textLabel.TextColor3 = Color3.fromRGB(170, 107, 96)
			ImageLabel.ImageColor3 = Color3.fromRGB(170, 107, 96)
		else
			timerLabel.TextColor3 = Color3.fromRGB(146, 170, 219)
			textLabel.TextColor3 = Color3.fromRGB(146, 170, 219)
			ImageLabel.ImageColor3 = Color3.fromRGB(146, 170, 219)
		end

	elseif action == "PlaySound" then
		local soundId = ...

		if soundId == "17391640536" then
			mainSound:Play()
		else
			local sound = Instance.new("Sound")
			sound.SoundId = "rbxassetid://" .. soundId
			sound.Parent = workspace
			sound:Play()
			game:GetService("Debris"):AddItem(sound, 5)
		end

	elseif action == "StopMusic" then
		mainSound:Stop()

	elseif action == "HideTimer" then
		frame.Visible = false
	end
end)
```
>[!tip]
> ### Что делает этот код?
> Добавляет простой таймер, где по истечению времени пропадает.

> [!note]
> ### Понятия в коде
Добавляем библиотеки (как в Python: `import time`)
```lua
local ServerScriptService = game:GetService("ServerScriptService")
local Lighting = game:GetService("Lighting")
local ReplicatedStorage = game:GetService("ReplicatedStorage")
```
`ServerScriptService` - **Серверный кабинет**  
Это как кабинет начальника, куда обычные сотрудники (клиенты) не заходят   
`ServerScriptService` нужен для:
1. Хранение серверный скриптов
2. логика игры(механики, система урона, таймер)
3. база данных
4. админ скрипты

`ReplicatedStorage` - **Склад данных**   
Это как холодильник между кухней и гостями    
`ReplicatedStorage` нужен для:
1. Хранение объектов, которые нуны клиенту и серверу
2. перадача данных, между сервером и клиентом
3. `RemoteEvents/RemoteFunctions` живут тут
### Аналогия:
`ReplicatedStorage` - **Общая полка в офисе**    
`ServerScriptStorage` - **Кабинет Начальника** (только для сервера)    
`StarterPack` - **Рюкзак игрока** (только для клиента)



>[!note]
> ### Что такое GetService вообще?
>**GetService** - Это весь, где мы получаем библиотеку или с тем предметом, которым будем работать.
> Это как спросить у роблокса: "Эй, дай мне ту штуковину, чтобы работать с [чем-то]"
> 

# FirstFov.luau

```lua
local players = game:GetService("Players")
local runService = game:GetService("RunService")
local userInputService = game:GetService("UserInputService")

local player = players.LocalPlayer
local camera = workspace.CurrentCamera

local cameraOffset = Vector3.new(0, 1.5, 0)
local mouseSensitivity = 0.5

local mouseDelta = Vector2.new()
local cameraYaw = 0
local cameraPitch = 0
local mouseLocked = true

local function hideAccessories(character)
	for _, item in pairs(character:GetDescendants()) do
		if item:IsA("Accessory") then
			local handle = item:FindFirstChild("Handle")
			if handle then
				handle.Transparency = 1
			end
		end
	end
end

local function getRootPart(character)
	return character:FindFirstChild("HumanoidRootPart") or character:FindFirstChild("Torso") or character:FindFirstChild("UpperTorso")
end

local function updateCamera()
	local character = player.Character
	if not character then return end

	local rootPart = getRootPart(character)
	if not rootPart then return end

	local head = character:FindFirstChild("Head")
	local headPosition = rootPart.Position + cameraOffset
	if head then
		headPosition = head.Position
	end

	cameraYaw = cameraYaw - mouseDelta.X * mouseSensitivity
	cameraPitch = math.clamp(cameraPitch - mouseDelta.Y * mouseSensitivity, -80, 80)

	mouseDelta = Vector2.new()

	local cameraCFrame = CFrame.new(headPosition) *
		CFrame.Angles(0, math.rad(cameraYaw), 0) *
		CFrame.Angles(math.rad(cameraPitch), 0, 0)

	camera.CFrame = cameraCFrame
	camera.Focus = cameraCFrame * CFrame.new(0, 0, -10)
end

local function onMouseDelta(input)
	if userInputService.MouseBehavior ~= Enum.MouseBehavior.LockCenter then
		userInputService.MouseBehavior = Enum.MouseBehavior.LockCenter
	end
	mouseDelta = input.Delta
end

local function toggleMouseLock()
	mouseLocked = not mouseLocked
	if mouseLocked then
		userInputService.MouseBehavior = Enum.MouseBehavior.LockCenter
	else
		userInputService.MouseBehavior = Enum.MouseBehavior.Default
	end
end

local function initializeCamera()
	camera.CameraType = Enum.CameraType.Scriptable

	userInputService.MouseBehavior = Enum.MouseBehavior.LockCenter

	userInputService.InputChanged:Connect(function(input)
		if input.UserInputType == Enum.UserInputType.MouseMovement and mouseLocked then
			onMouseDelta(input)
		end
	end)

	-- Альт клавиша
	userInputService.InputBegan:Connect(function(input)
		if input.KeyCode == Enum.KeyCode.LeftAlt or input.KeyCode == Enum.KeyCode.RightAlt then
			toggleMouseLock()
		end
	end)

	if player.Character then
		hideAccessories(player.Character)
	end

	runService:BindToRenderStep("FirstPersonCamera", Enum.RenderPriority.Camera.Value, updateCamera)
end

player.CharacterAdded:Connect(function(character)
	character:WaitForChild("Humanoid")
	wait(0.5)

	hideAccessories(character)

	character.DescendantAdded:Connect(function(descendant)
		if descendant:IsA("Accessory") then
			local handle = descendant:FindFirstChild("Handle")
			if handle then
				handle.Transparency = 1
			end
		end
	end)

	initializeCamera()
end)

if player.Character then
	wait(0.5)
	initializeCamera()
end

player.CharacterRemoving:Connect(function()
	runService:UnbindFromRenderStep("FirstPersonCamera")
end)
```
>[!tip]
> ### Что делает этот код?
> добавляет режим от первого лица с заблокированной мышью, пользователь может её разблокировать при нажатии на `ALT`

>[!note]
> ### Понятия в коде
> ### GetServices:
> `GetService("Players")` - "Кто в игре?"   
> Что делает: держит всех игроков, знает кто зашел, кто вышел, кто умер, `players.LocalPlayer` - Это игрок.
```lua
local player = players.LocalPlayer  -- Находит тебя в игре
player.CharacterAdded:Connect(...)  -- Ждет, когда у тебя появится тело
```
`GetService("RunService")` - "Таймер для гиперактианых"   
Что делает: тикает как сумашедшие часы (60 раз в секунду)   
запускает код **каждый кадр**    
`RenderStepped` - перед отрисовкой кадра

`GetService("UserInputService")` - "Шпион за клавиатурой      
Что делает: Подслушивает **ВСЁ**, что делает игрок   
Клавиши, мышь, тачскрин - **ВСЁ ЕГО!**   
Мышь в центр экрана засовывает (как в моем коде)
> [!note]
> ### Разбор основных функций кода
> `hideAccessories(character)` - Убирает аксессуары игрока   
> `getRootPart(character)` - Ищет тело   
> `updateCamera()` - Мозг камеры   
> `onMouseDelta(input)` - ловит мышь   
> `toggleMouseLock()` - блокировка мыши

>[!important]
>### Важные переменные
```lua
cameraOffset = Vector3.new(0, 1.5, 0)  -- На 1.5 выше ног (примерно глаза)
mouseSensitivity = 0.5                 -- Чувствительность мыши (поставьте 0.1 если тошнит)
cameraYaw = 0                          -- Поворот влево-вправо (оси Y)
cameraPitch = 0                        -- Поворот вверх-вниз (оси X, ограничен -80..80)
```

>[!warning]
>### ВНИМАНИЕ
> Я не закончил полностью над этим документом, но скоро выложу коммит с добавлением нескольких проектов!


# **[Главный репозиторий](https://github.com/Drugoi-Polz/IservNG)**

>[!warning]
>### ВНИМАНИЕ
> **Главным репозиторием не владею и *никак* не могу редактировать там, что есть.**








