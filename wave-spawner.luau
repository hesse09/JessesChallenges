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
	if CURRENT_STATE ~= "Wave" then return "Wait" end --if not state we wait
	for i = 1, count do-- spawn enemys
		local spawnCreat --ACT LIKE WE SPAWENED
		task.wait(interval) --wait
	end
	return "Done" --return done
end

game.Players.PlayerAdded:Connect(function(player)
	if not game:IsLoaded() then 
		game.Loaded:Wait() --wait for game to load
	end 
	CURRENT_STATE = "Wave" -- set state to wave

	while true do
		local wave = Waves[CURRENT_WAVE] --get wave
		if not wave then break end --no more waves, stop
		local result = SpawnEnemy(wave.enemyType, wave.count, wave.interval) --spawn enemy
		if result == "Done" then 
			CURRENT_WAVE += 1 --if done we increase wave
		end
	end

end)
