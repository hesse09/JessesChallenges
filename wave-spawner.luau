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
