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