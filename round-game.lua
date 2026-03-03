local currentNum = 0
local interval = 0.1
local currentRound = 1
local roundPre = 10
local socket = require("socket")

function UpdateRound(roundNumber)
    currentRound = currentRound + 1
    roundPre = roundNumber * 2 + 10
    return { true, currentRound, roundPre }
end

while true do
    socket.sleep(1)
    currentNum = currentNum + interval
    if currentNum >= roundPre then
        local success = UpdateRound(currentRound)
        if success[1] == true then
            print("You are on round", success[2], "with a you must reach", success[3])
        else
          break
        end
    end
end

print("Ending")
