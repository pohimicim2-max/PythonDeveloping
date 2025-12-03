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