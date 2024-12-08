def on_on_died():
    gameplay.title(mobs.target(NEAREST_PLAYER), player.name(), " You FAILED ")
    mobs.clear_effect(mobs.target(NEAREST_PLAYER))
    gameplay.set_game_mode(CREATIVE, mobs.target(NEAREST_PLAYER))
player.on_died(on_on_died)

def on_on_chat():
    mobs.kill(mobs.target(NEAREST_PLAYER))
    player.tell(mobs.target(NEAREST_PLAYER), "The game ended")
player.on_chat("End", on_on_chat)

def on_on_chat2():
    mobs.apply_effect(BLINDNESS, mobs.target(NEAREST_PLAYER), 400, 255)
    mobs.clear_effect(mobs.target(NEAREST_PLAYER))
    player.teleport(randpos(pos(0, 0, 0),
            randpos(positions.ground_position(pos(100, 100, 100)), pos(0, 0, 0))))
    player.tell(mobs.target(NEAREST_PLAYER),
        "Hi! You got to make sure you don’t get blown up by your friend ")
    gameplay.title(mobs.target(NEAREST_PLAYER), "TNT placer", "RUNNNNNNNN")
    builder.load_structure("my structure")
    gameplay.time_set(gameplay.time(DAY))
    gameplay.set_weather(CLEAR)
    gameplay.set_difficulty(HARD)
    gameplay.set_game_mode(SURVIVAL, mobs.target(NEAREST_PLAYER))
    gameplay.xp(99, mobs.target(NEAREST_PLAYER))
    gameplay.set_game_rule(FIRE_DAMAGE, True)
    gameplay.set_game_rule(PV_P, True)
    gameplay.set_game_rule(WEATHER_CYCLE, False)
    gameplay.set_game_rule(DROWNING_DAMAGE, True)
    gameplay.set_game_rule(MOB_LOOT, False)
    gameplay.set_game_rule(WEATHER_CYCLE, False)
    gameplay.set_game_rule(DAYLIGHT_CYCLE, False)
    blocks.fill(GRASS,
        pos(100, 100, 100),
        pos(100, 100, 100),
        FillOperation.REPLACE)
    loops.pause(150)
    mobs.apply_effect(SPEED, mobs.target(NEAREST_PLAYER), 600, 40)
    mobs.give(mobs.target(NEAREST_PLAYER), TNT, 90)
    mobs.execute_detect(TNT, pos(0, 0, 0), "/fill ~~~3~3~3~tnt")
    mobs.spawn_particle(EXPLOSION_SINGLE, pos(0, 0, 0))
    while True:
        blocks.place(TNT, pos(1, 0, 1))
player.on_chat("TNT", on_on_chat2)

def on_item_interacted_flint_and_steel():
    gameplay.xp(10, mobs.target(NEAREST_PLAYER))
player.on_item_interacted(FLINT_AND_STEEL, on_item_interacted_flint_and_steel)

def on_forever():
    mobs.apply_effect(SPEED, mobs.target(NEAREST_PLAYER), 600, 40)
    mobs.apply_effect(REGENERATION, mobs.target(NEAREST_PLAYER), 600, 20)
loops.forever(on_forever)

mobs.give(mobs.target(RANDOM_PLAYER), TNT, 90)
mobs.teleport_to_player(mobs.target(NEAREST_PLAYER), mobs.target(NEAREST_PLAYER))