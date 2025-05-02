from flask import Flask

app = Flask(__name__)


# Home base
@app.route("/")
def home():
    return """
    <h1>🏕️ Welcome to Adventure Zone!</h1>
    <p>Choose your quest:</p>
    <ul>
        <li><a href="/quest/forest">🌳 The Enchanted Forest</a></li>
        <li><a href="/quest/dungeon">🗝️ The Dark Dungeon</a></li>
    </ul>
"""


# Nested routing
@app.route("/quest/<location>")
def quest(location):
    if location == "forest":
        return """
            <h1>🌲 Enchanted Forest</h1>
            <p>You see two paths ahead:</p>
            <ul>
                <li><a href="/quest/forest/left">👣 Take the left path</a></li>
                <li><a href="/quest/forest/right">👣 Take the right path</a></li>
            </ul>
            <a href="/">🏕️ Back to the beginning.</a>
    """
    elif location == "dungeon":
        return """
            <h1>⚔️ Dark Dungeon</h1>
            <p>You encounter two doors:</p>
            <ul>
                <li><a href="/quest/dungeon/blue-door">🚪 Blue Door</a></li>
                <li><a href="/quest/dungeon/red-door">🚪 Red Door</a></li>
            </ul>
            <a href="/">🏕️ Back to the beginning.</a>
    """
    else:
        return "<h1>🗺️ Hmm...that location doesn't exist!</h1>", 404


# Deeper nested routing
@app.route("/quest/forest/<choice>")
def forest_quest(choice):
    if choice == "left":
        return """
            <h2>🐉 You met a friendly dragon! You win!</h2>
            <a href="/quest/forest">🌳 Back to the Forest.</a>
            """
    
    elif choice == "right":
        return """
            <h2>🐺 Oh no! Wolves! Run away!</h2>
            <a href="/quest/forest">🌳 Back to the Forest.</a>
            """
    else:
        return """
            <h2>❓ Lost in the woods, huh?</h2>
            <a href="/">🏕️ Back to the beginning.</a>
            """, 404


@app.route("/quest/dungeon/<choice>")
def dungeon_quest(choice):
    if choice == "blue-door":
        return """
            <h2>💎 Treasure room found! You're rich!</h2>
            <a href="/quest/dungeon">🗝️ Back to the Dungeon.</a>
            """
    elif choice == "red-door":
        return """
            <h2>👻 A ghost! Quick, get out!</h2>
            <a href="/quest/dungeon">🗝️ Back to the Dungeon.</a>
            """
    else:
        return """
            <h2>🚧 That door doesn't exist!</h2>
            <a href="/">🏕️ Back to the beginning.</a>
            """, 404