local Waves = {
	[1] = {enemyType = "Basic", count = 5, interval = 1},
	[2] = {enemyType = "Fast", count = 8, interval = 0.8}, 
}
local CURRENT_STATE = nil
local CURRENT_WAVE = 1

playerStats = {
	{Health = 100, Damage = 10, Speed = 10}
}

function SpawnEnemy(enemyType: string, count: number, interval: number)
	if CURRENT_STATE ~= "Wave" then return "Wait" end
	for i = 1, count do
		local spawnCreat --ACT LIKE WE SPAWENED
		task.wait(interval)
	end
	return "Done"
end

game.Players.PlayerAdded:Connect(function(player)
	if not game:IsLoaded() then
		game.Loaded:Wait()
	end
	CURRENT_STATE = "Wave"
	
	task.spawn(function()
		local wave = Waves[CURRENT_WAVE]
		if not wave then return end
		local result = SpawnEnemy(wave.enemyType, wave.count, wave.interval)
		if result == "Done" then
			CURRENT_WAVE += 1
		end
	end)
	
end)
