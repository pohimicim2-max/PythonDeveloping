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

