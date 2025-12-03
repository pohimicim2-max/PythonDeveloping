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