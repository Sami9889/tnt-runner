player.onDied(function () {
    gameplay.title(mobs.target(NEAREST_PLAYER), player.name(), " You FAILED ")
    mobs.clearEffect(mobs.target(NEAREST_PLAYER))
    gameplay.setGameMode(
    CREATIVE,
    mobs.target(NEAREST_PLAYER)
    )
})
player.onChat("End", function () {
    mobs.kill(
    mobs.target(NEAREST_PLAYER)
    )
    player.tell(mobs.target(NEAREST_PLAYER), "The game ended")
})
player.onChat("TNT", function () {
    mobs.applyEffect(BLINDNESS, mobs.target(NEAREST_PLAYER), 400, 255)
    mobs.clearEffect(mobs.target(NEAREST_PLAYER))
    player.teleport(randpos(
    pos(0, 0, 0),
    randpos(
    positions.groundPosition(pos(100, 100, 100)),
    pos(0, 0, 0)
    )
    ))
    player.tell(mobs.target(NEAREST_PLAYER), "Hi! You got to make sure you don’t get blown up by your friend ")
    gameplay.title(mobs.target(NEAREST_PLAYER), "TNT placer", "RUNNNNNNNN")
    builder.loadStructure("my structure")
    gameplay.timeSet(gameplay.time(DAY))
    gameplay.setWeather(CLEAR)
    gameplay.setDifficulty(HARD)
    gameplay.setGameMode(
    SURVIVAL,
    mobs.target(NEAREST_PLAYER)
    )
    gameplay.xp(99, mobs.target(NEAREST_PLAYER))
    gameplay.setGameRule(FIRE_DAMAGE, true)
    gameplay.setGameRule(PV_P, true)
    gameplay.setGameRule(WEATHER_CYCLE, false)
    gameplay.setGameRule(DROWNING_DAMAGE, true)
    gameplay.setGameRule(MOB_LOOT, false)
    gameplay.setGameRule(WEATHER_CYCLE, false)
    gameplay.setGameRule(DAYLIGHT_CYCLE, false)
    blocks.fill(
    GRASS,
    pos(100, 100, 100),
    pos(100, 100, 100),
    FillOperation.Replace
    )
    loops.pause(150)
    mobs.applyEffect(SPEED, mobs.target(NEAREST_PLAYER), 600, 40)
    mobs.give(
    mobs.target(NEAREST_PLAYER),
    TNT,
    90
    )
    mobs.executeDetect(
    TNT,
    pos(0, 0, 0),
    "/fill ~~~3~3~3~tnt"
    )
    mobs.spawnParticle(EXPLOSION_SINGLE, pos(0, 0, 0))
    while (true) {
        blocks.place(TNT, pos(1, 0, 1))
    }
})
player.onItemInteracted(FLINT_AND_STEEL, function () {
    gameplay.xp(10, mobs.target(NEAREST_PLAYER))
})
loops.forever(function () {
    mobs.applyEffect(SPEED, mobs.target(NEAREST_PLAYER), 600, 40)
    mobs.applyEffect(REGENERATION, mobs.target(NEAREST_PLAYER), 600, 20)
})
mobs.give(
mobs.target(RANDOM_PLAYER),
TNT,
90
)
mobs.teleportToPlayer(
mobs.target(NEAREST_PLAYER),
mobs.target(NEAREST_PLAYER)
)
