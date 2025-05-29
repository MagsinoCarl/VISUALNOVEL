# Declare the main character
  # Enables persistent variables in preferences

label before_main_menu:
    $ apply_ui_theme()
    return

$ persistent.ui_theme = "dark"

default persistent.ui_theme = "default"  # This saves the user's selected theme

init python:

    def apply_ui_theme():
        # Use persistent color or default to white
        text_color = persistent.text_color if hasattr(persistent, "text_color") else "#FFFFFF"

        # Change the say dialogue text color
        style.say_dialogue.color = text_color

        # Optionally, change window background text color or other UI elements here too
        # For example, change textbox window text color or font color if needed

        # To refresh styles immediately, call:
        renpy.restart_interaction()


image Carl_normal = im.Scale("images/Carl_normal.png", 1200, 1300)
image Carl_talking = im.Scale("images/Carl_talking.png", 1200, 1300)
image Carl_suggesting = im.Scale("images/Carl_suggesting.png", 1200, 1300)
image Carl_thinking = im.Scale("images/Carl_thinking.png", 1200, 1300)
image bg room = "bg_room.jpg"


define c = Character("Carl", color="#80c4ff")

label start:
    stop music fadeout 1.0
    scene bg_room at Transform(xysize=(3280, 3220))

    show Carl_normal at center with dissolve
    c "Hey there."

    show Carl_talking at center with dissolve
    c "Are you new to visual novels?"

    menu:
        "I'm new at this, sorry.":
            jump tutorial
        "I already know, thank you.":
            jump skip_tutorial

label tutorial:

    show Carl_suggesting at center with dissolve
    c "No worries! I'm here to guide you around."

    show Carl_talking at center with dissolve
    c "This box below me? That's the text box."

    show Carl_thinking at center with dissolve
    c "All the story, dialogue, and narration happens here."

    show Carl_suggesting at center with dissolve
    c "Want a cleaner view of the background? Just press the H key on your keyboard to hide the UI."

    show Carl_suggesting at center with dissolve
    c "You can also roll back to dialogue with ease using your scroll wheel in you mouse!"

    show Carl_thinking at center with dissolve
    c "Want a cleaner view of the background? Just press the H key on your keyboard to hide the UI."

    show Carl_talking at center with dissolve
    c "You can press H again to bring everything back."

    show Carl_thinking at center with dissolve
    c "Now if you press the Esc key, you'll open the game menu."

    show Carl_normal at center with dissolve
    c "Let me explain the buttons there real quick!"

    show Carl_talking at center with dissolve
    c "History – lets you view past dialogue in case you missed something."

    show Carl_suggesting at center with dissolve
    c "Save and Load – save your progress or return to a previous point."

    show Carl_thinking at center with dissolve
    c "Preferences – change text speed, music volume, and other settings."

    show Carl_talking at center with dissolve
    c "About – gives info about the game."

    show Carl_normal at center with dissolve
    c "Help – shows all the controls."

    show Carl_thinking at center with dissolve
    c "And Quit – well... exits the game. Careful with that one."

    show Carl_suggesting at center with dissolve
    c "And don't forget the Return button – it brings you right back to the game."

    show Carl_talking at center with dissolve
    c "Got it? Sweet. Let's get started!"

    jump main_game

label skip_tutorial:

    show Carl_normal at center with dissolve
    c "Ah, a veteran I see. I'll leave you to it then."

    jump main_game

label main_game:

    show Carl_talking at center with dissolve
    c "This is where the real story begins..."

    # Continue your actual visual novel story from here...

    return


# Put this at the bottom of script.rpy
label splashscreen:
    scene black
    show splash_bg
    play music "splash_theme.mp3"

    call screen splash_screen

    stop music fadeout 1.0

    hide splash_bg with dissolve  # Optional: make splash image fade out only
    return

