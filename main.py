def on_overlap_tile(sprite, location):
    tiles.set_tile_at(location, assets.tile("""
        transparency16
    """))
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        instrument4
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    tiles.set_tile_at(location2, assets.tile("""
        transparency16
    """))
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        instrument1
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    tiles.set_tile_at(location3, assets.tile("""
        transparency16
    """))
    info.change_score_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        fan2
    """),
    on_overlap_tile3)

def on_overlap_tile4(sprite4, location4):
    tiles.set_tile_at(location4, assets.tile("""
        transparency16
    """))
    info.change_score_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        fan1
    """),
    on_overlap_tile4)

def on_overlap_tile5(sprite5, location5):
    tiles.set_tile_at(location5, assets.tile("""
        transparency16
    """))
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        instrument0
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite6, location6):
    tiles.set_tile_at(location6, assets.tile("""
        transparency16
    """))
    info.change_score_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        fan3
    """),
    on_overlap_tile6)

def on_overlap_tile7(sprite7, location7):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        exit
    """),
    on_overlap_tile7)

scene.set_background_color(13)
tiles.set_tilemap(tilemap("""
    level1
"""))
jeery = sprites.create(assets.image("""
    rockstar
"""), SpriteKind.player)
controller.move_sprite(jeery)
tiles.place_on_random_tile(jeery, assets.tile("""
    stage
"""))
scene.camera_follow_sprite(jeery)
info.start_countdown(30)